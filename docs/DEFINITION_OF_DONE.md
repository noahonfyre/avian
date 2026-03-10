# Definition of Done

Eine Liste von Akzeptanzkriterien, die erfüllt werden müssen, damit das Projekt den MVP Status erreicht hat.

## Pflichtkriterien

- [ ] Der Code auf dem `master`-Branch läuft bei normaler Nutzung flüssig und ohne Fehler.
- [ ] Der Code ist sinnvoll formatiert, kommentiert und klar lesbar.
- [ ] Das Programm bietet eine visuelle Oberfläche, die für Eingaben und Ausgaben der nötigen Informationen benutzt
  wird.

## Spezifische Kriterien

- [ ] Das Programm bietet die Möglichkeit, eine Dateienübertragung zu initiieren, wobei der Benutzer die Zieladresse
  eingeben kann und die Dateien, die übertragen werden sollen, auswählt.
- [ ] Das Programm bietet die Möglichkeit, eine Dateienübertragung zu akzeptieren, wobei die Dateien vom Peer übertragen
  und anschließend in einem vordefinierten Ordner gespeichert.
- [ ] Das Programm kommuniziert die für den Benutzer als wichtig erachteten Informationen bezüglich den Übertragungen
  klar und übersichtlich über die grafische Benutzeroberfläche.
- [ ] Die Dateien werden nachträglich per Checksum auf Integrität überprüft.
- [ ] Dateioperationen (i.d.F. Reads) bei diesen benutzerdefinierten Dateien werden immer in Chunks durchgeführt, um das
  Laden von großen Datenmengen in den Arbeitsspeicher zu verhindern.