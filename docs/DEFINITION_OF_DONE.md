# Definition of Done

Eine Liste von Akzeptanzkriterien, die erfüllt werden müssen, damit das Projekt den MVP Status erreicht hat.

## Pflichtkriterien

- [x] Der Code auf dem `master`-Branch läuft bei normaler Nutzung flüssig und ohne Fehler.
- [x] Der Code ist sinnvoll formatiert, kommentiert und klar lesbar.
- [x] Das Programm bietet eine visuelle Oberfläche, die für Eingaben und Ausgaben der nötigen Informationen benutzt
  wird.

## Spezifische Kriterien

- [x] Das Programm bietet die Möglichkeit, eine Dateienübertragung zu initiieren, wobei der Benutzer die Zieladresse
  eingeben kann und die Dateien, die übertragen werden sollen, auswählt.
- [x] Das Programm bietet die Möglichkeit, eine Dateienübertragung zu akzeptieren, wobei die Dateien vom Peer übertragen
  und anschließend in einem vordefinierten Ordner gespeichert.
- [x] Das Programm kommuniziert die für den Benutzer als wichtig erachteten Informationen bezüglich den Übertragungen
  klar und übersichtlich über die grafische Benutzeroberfläche.
- [x] Die Dateien werden nachträglich per Checksum auf Integrität überprüft.
- [x] Dateioperationen (i.d.F. Reads) bei diesen benutzerdefinierten Dateien werden immer in Chunks durchgeführt, um das
  Laden von großen Datenmengen in den Arbeitsspeicher zu verhindern.