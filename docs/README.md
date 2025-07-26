# HTWG Grade Calculator - Documentation

🎥 [Demo Video auf Panopto](https://video.htwg-konstanz.de/Panopto/Pages/Viewer.aspx?id=c90020c7-7cbb-4800-b5fb-b326012e2d2c)

1. Punkte in Excel oder tab-separierte Textdatei eintragen. Die erste Spalte muss "mtknr" heißen.
2. Excel-Datei hochladen (Upload Grading File). 
3. Schieberegler für P1 (1.0) (Anzahl der Punkte für Note 1.0) und P4 (4.0) (Anzahl der Punkte für Note 4.0) anpassen.
4. Die App berechnet automatisch die Noten und zeigt sie in einer Tabelle an.
5. Matrikelnummern aus der offiziellen Excel-Vorlage der Hochschule kopieren und in die App einfügen.
6. Die App sortiert die Matrikelnummern und berechnet die Noten entsprechend der Hochschule
7. Noten in die offizielle Excel-Vorlage der Hochschule kopieren.


#### Excel Datei Format:
| mtknr | Task1 | Task2 | Task3 | Task4 |
|-------|-------|-------|-------|-------|
| 12345 | 8.5   | 7.2   | 9.1   | 6.8   |
| 67890 | 6.8   | 8.9   | 7.5   | 8.2   |   

Eine anonymisierte Excel-Datei mit Testdaten ist im Repository enthalten (`docs/Matrikel_Punkte.xlsx`). Eine Anonymisierte HTWG HIS-in-one 🤮 Excel-Datei ist in (`docs/his_in_one_demo.xlsx`).


Eine (autogenerierten) detaillierte Anleitung ist in `docs/user-guide.md` zu finden.