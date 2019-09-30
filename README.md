# perf-report
```
Instrukcja korzystania z generatora raportu po testach

Przed przystąpieniem do generowania raportu musimy zainstalować Dockera i go uruchomić
Struktura katalogów

Przed uruchomieniem generatora należy stworzyć foldery podfoldery w których umieścimy nasze dane z testów tak jak na schemacie poniżej:

Lokalizacja A zawiera dane z testu bez narzędzi bezpieczeństwa
Lokalizacja B zawiera dane z testu z narzędziami bezpieczeństwa
W obu lokalizacjach tworzymy katalog odpowiadający konkretnemu rodzajowi testu
Np
.
├── A
│   └── hql
│       ├── raw
└── B
   └── hql
       ├── raw
       
W folderze raw umieszczamy dane pozyskane z nmona(zarówno bez narzędzi bezpieczeństwa w lokalizacji A/hql/raw i z narzędziami bezpieczeństwa w lokalizacji B/hql/raw) tak jak w przykładzie poniżej:

├── raw
       │   ├── vxhdpc111_190807_1410.nmon
       │   ├── vxhdpc112_190807_1410.nmon
       │   ├── vxhdpc113_190807_1410.nmon
       │   └── vxhdpc114_190807_1410.nmon
```       
Następnie odpalamy skrypt komendą:
```bash
cd ${REPO}/perf-report/ && bin/run.sh ${DATA_DIR}
```
```
Gdzie pierwsza ścieżka to ścieżka do naszego katalogu z repozytorium a druga ścieżka to ścieżka gdzie znajdują się katalogi A i B z surowymi danymi.
```
