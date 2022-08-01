# re_register_data

Dieses Datenrepository umfasst die Rohdaten der [Register für Paulys Realencyclopädie der classischen Altertumswissenschaft](https://de.wikisource.org/wiki/Paulys_Realencyclop%C3%A4die_der_classischen_Altertumswissenschaft/Register).
Diese werden mithilfe eines nächtlichen Bots aktualisiert und generiert. 
Die Quellen dieses Bots finden sich in einem [seperaten Repositorys](https://github.com/the-it/WS_THEbotIT).

## Nutzung

Die Daten der Register können in diesem Repository korrigiert werden. 
Dazu können Tests ausgeführt werden um die Integrität der Daten sicherzustellen.

* Python3 und Git müssen installiert sein und im Pfad des entsprechenden Systems vorhanden sein. (Momentan nur unter Linux, Windows ist in Arbeit)
* Führe `setup.py` aus um eine virtuelle Umgebung und den Testcode runterzuladen
* Führe `test.py` aus um die Tests abzuspielen
