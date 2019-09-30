# Script for starting/stopping NodeManagers
# An example:
#  python prepare_env.py --hosts  cdh-slave-02.c.getindata-training.internal,cdh-slave-03.c.getindata-training.internal --user admin --password admin --url http://localhost --port 7180 --action start

import optparse

parser = optparse.OptionParser()

from cm_api.api_client import ApiResource

import cm_client
from cm_client.rest import ApiException
from pprint import pprint


parser.add_option('--hosts',
                  action="store", dest="hosts",
                  help="Node managers to stop")

parser.add_option('--user',
                  action="store", dest="user",
                  help="Username")

parser.add_option('--password',
                  action="store", dest="password",
                  help="Password")


parser.add_option('--url',
                  action="store", dest="url",
                  help="CM URL")

parser.add_option('--port',
                  action="store", dest="port",
                  help="CM Port")

parser.add_option('--action',
                  action="store", dest="action",
                  help="Start/stop node managers")


options, args = parser.parse_args()

hosts = options.hosts.split(',')

print 'NodeManagers to start/stop:', hosts


api = ApiResource(options.url.replace('http://','').replace('https://',''), options.port, options.user, options.password)

host_ids_action = [h.hostId for h in api.get_all_hosts() if h.hostname in hosts]


cm_client.configuration.username = options.user
cm_client.configuration.password = options.password

# Create an instance of the API class
api_host = options.url
port = options.port
api_version = 'v19'
api_url = api_host + ':' + port + '/api/' + api_version
api_client = cm_client.ApiClient(api_url)
cluster_api_instance = cm_client.ClustersResourceApi(api_client)

#

# Lists all known clusters.
api_response = cluster_api_instance.read_clusters(view='SUMMARY')
cluster = api_response.items[0]
services_api_instance = cm_client.ServicesResourceApi(api_client)
services = services_api_instance.read_services(cluster.name, view='FULL')
for service in services.items:
    # print service.display_name, "-", service.type
    if service.type == 'YARN':
        yarn = service
        # roles = services_api_instance.read_roles(cluster.name, hdfs.name)
roles_api_instance  = cm_client.RolesResourceApi(api_client)
command_api_instance = cm_client.RoleCommandsResourceApi(api_client)
roles = roles_api_instance.read_roles(cluster.name,yarn.name)
# print (roles)



dn_roles = [role.name for role in roles.items if role.type == 'NODEMANAGER' and role.host_ref.host_id in host_ids_action]
print(dn_roles)
role_names = cm_client.ApiRoleNameList(dn_roles)

cm_client.RoleCommandsResourceApi(api_client)
if options.action.lower() == 'stop':
    cmd_list = command_api_instance.stop_command(cluster.name, yarn.name, body=role_names)
elif options.action.lower() == 'start':
    cmd_list = command_api_instance.start_command(cluster.name, yarn.name, body=role_names)
