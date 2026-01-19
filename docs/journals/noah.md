# Forschungstagebuch von Noah

* [Forschungstagebuch von Noah](#forschungstagebuch-von-noah)
    * [29.10.2025](#29102025)
    * [12.11.2025](#12112025)
    * [19.11.2025](#19112025)
    * [26.11.2025](#26112025)
    * [03.12.2025](#03122025)
    * [10.12.2025](#10122025)
    * [22.12.2025](#22122025)
    * [14.01.2026](#14012026)
    * [21.01.2026](#21012026)

**\[ Nachtrag basierend auf Git-Historie \]**

## 29.10.2025

Am 29.10. habe ich mit der Projektarbeit durch das Erstellen des Git-Repositorys sowie dessen Einrichtung begonnen.
Dabei habe ich mich zuerst um einen Namen für das Projekt gekümmert und bin auf "Avian" (z. Dt. Vogel-), aufgrund der
Verbindung zwischen Vögeln und Freiheit (→ Dezentralisierung & Open Source). Ich habe ebenfalls das Kanban-Board und
Zugriff für Teammitglieder eingerichtet, erste Tickets/Issues erstellt und zugewiesen.

## 12.11.2025

Am 12.11. habe ich angefangen, die Projektstruktur festzulegen und habe dafür erste Module, Dateien und Klassen
erstellt. Anschließend habe ich mich um weitere organisatorische Dinge, wie das Einrichten des Code-Editors von meinen
Teammitgliedern, sowie deren Verbindung mit dem Git-Server, gekümmert.

## 19.11.2025

Am 19.11. habe ich Luca zuerst bei dem Einstieg in den `grid`-Geometry-Manager von `tkinter` geholfen, mit dem er den
strukturellen Aufbau des GUIs weitgehend alleine bewältigen konnte, sowie mit der allgemeinen Struktur der Klasse.
Außerdem habe ich mich um die Branch Protection Rules für den `master` Branch gekümmert, damit nicht direkt auf den
`master` Branch commited werden kann, sondern für jedes Feature und jeden Bugfix ein einzelner Branch erstellt wird, der
dann per PR auf master gemergt werden kann.

## 26.11.2025

Am 26.11. habe ich eine verbesserte Projektstruktur angewendet, welche zum größten Teil bis heute besteht, sowie die
Code-Reviews für Luca durchgeführt und daraufhin diese Pull-Requests entsprechend gemergt und ggf. Merge-Konflikte
behoben.

## 03.12.2025

Am 03.12. habe ich die erste Iteration der Projektstruktur für das Backend mit den Anderen besprochen und diese
anschließend gemergt. Daraufhin habe ich Luca bei dem Outsourcing von den verschiedenen Komponenten des GUIs in eigene
Klassen geholfen. Ebenso habe ich durch die Behebung des Problems, dass das Projekt unter VS Code nicht ausgeführt
werden kann, Luca der Problemerkennung und -behebung näher gebracht. Zudem habe ich Recherche zu einer neuen
Projektstruktur betrieben: dem MVCS-Paradigma (Model-View-Controller-Service), in dem Code in verschiedene Abschnitte
gegliedert wird:

Das Model enthält hauptsächlich Anwendungslogik, ist aber auch für State Management und Datenspeicherung bzw. -austausch
vorgesehen. Hier befinden sich außerdem bei uns viele Typ- bzw. Klassendeklarierungen. Ein Beispiel in unserer
Implementierung ist der `EventBus`.

Ein View ist in unserem Fall die grafische Benutzeroberfäche. Der View visualisiert Daten, die er vom Controller
erhält. Außerdem leitet der View Eingaben von Benutzern (darunter Textfeld-Eingaben, Button-Klicks, etc.) an den
Controller weiter. Hierbei handelt es sich bei uns um `App` und dessen Unterklassen.

Der Controller dient als Brücke zwischen Models und View. Er leitet Informationen von den Models und Services zum View
weiter und Informationen vom View zu den Models und Services.

Ein Service hingegen dient zur Zusammenfassung von Anwendungslogik, die Informationen von Modellen zusammensammelt oder
von außenstehenden Quellen bezieht. Services können Netzwerkanfragen und Dateioperationen (CRUD) durchführen.

(Das Paradigma könnte in einigen Aspekten für unseren Anwendungsfall leicht abgewandelt sein.)

Wir fügen zudem noch die Network-Layer hinzu, die eher Low-Level Netzwerkanfragen durchführen, die von den Services
interpretiert, ausgewertet und zusammengesammelt werden können.

**\[ Ende Nachtrag \]**

## 10.12.2025

Heute habe ich gemeinsam mit Luca die dynamische Darstellung von Informationen mithilfe von `tkinter` Variablen
erarbeitet. Anschließend habe ich mich nach erneuter Recherche dafür entschieden, die Projektstruktur noch einmal
abzuändern. Dafür habe ich mich an dem MVCS-Paradigma, zu dem ich am 03.12.2025 recherchiert habe, orientiert.
Zusätzlich habe ich die Helper-Klasse `DynamicTemplate` erstellt, die mithilfe eines vorgegebenen Formats und Variablen
eine bessere und einfachere Darstellung von Daten im View bereitstellt und mithilfe dieser Klasse ein Refactor der
View-Ebene durchgeführt. Außerdem habe ich mittels der Implementierung eines `ttk.TreeView`-Widgets, den Grundbaustein
für die Anzeige der aktuellen Übertragungen gelegt und ein Extra-Fenster durch `tk.Toplevel` für das Herstellen einer
neuen Verbindung erstellt. Zudem habe ich nach der ersten Ausführung von `DynamicTemplate` noch einen Fehler behoben,
der verursacht hat, dass der Text erst nach der ersten Änderung von einer der unterliegenden Variablen angezeigt wird,
indem ich die `update()`-Methode bereits im Constructor aufrufe und habe den Datei-Input von Dominik von der Sidebar
in das neue `ConnectionWindow` verschoben, sowie die Größe der drei von Dominik neu angelegten Bereiche in `Statistics`
vereinheitlicht.

## 22.12.2025

Heute habe ich das Setup vom Paket- und Projektmanager [uv](https://github.com/astral-sh/uv) fertiggestellt, wofür ich
die Python-Version in `.python-version` festlegen musste und durch `uv lock` die Lock-Datei für die Abhängigkeiten des
Projektes erstellen musste. Zusätzlich habe ich einige wichtige Abhängigkeiten für das Weitergehen des Projektes
hinzugefügt, darunter `trio` für asynchrone Operationen, die vor allem im Backend benötigt werden, `ruff`, um schnell
und übersichtlich Code zu formatieren und zu linten, um Probleme bereits for der Ausführung des Programmes zu
identifizieren und `ty`, für Type Checking und als schnellere Language Server Implementierung. Ich habe zudem
angefangen, Teile des Backends mittels Docstrings zu dokumentieren.

Ich habe außerdem festgelegt, dass wir wieder [Conventional Commits](https://www.conventionalcommits.org/de/v1.0.0/)
(bzw. [commitlint Konventionen](https://gist.github.com/Zekfad/f51cb06ac76e2457f11c80ed705c95a3)) benutzen sollten,
obwohl ich dies zuerst der Einfachheit halber vermeiden wollte, aber denke nun, dass sie vorteilhafter sind, da diese
Art der Commitnachrichten einfach strukturierter und aussagekräftiger sind.

## 14.01.2026

Heute habe ich hauptsächlich versucht, die durch die Abwesenheit einiger Gruppenmitglieder entstandenen Merge-Konflikte
zu beheben und die Gruppe wieder in das Projekt nach der Pause der Ferien einzuführen. Zudem haben wir gemeinsam über
die Zukunft des Projektes im Zusammenhang mit der Zeitplanung nachgedacht und auf Basis dieser, gegebenenfalls Features
abgeändert oder für den Release als nicht zwingend nötig abgehandelt. Features, die darunter fallen, sind beispielsweise
die Implementierung von einem eigenen, verbindungsorientierten, UDP-basierten Application-Layer Netzwerkprotokoll mit
Flow und Congestion Control, Reliability und ggf. asymmetrisch und symmetrischer Verschlüsslung welches Multiplexing,
Variable Length Integers und Out-of-order Delivery unterstützen und dadurch HOL-Blocking verhindern sollte. Wir haben
uns entschieden, dieses nur umzusetzen, wenn wir nach dem Erreichen unserer Definition of Done noch ausreichend Zeit für
eine solche Implementierung hätten. Ein weiteres Feature, das aufgrund der Retrospektive weichen musste ist eine Liste
an kürzlichen Übertragungen so wie eine Kontaktähnliche Liste für das schnelle Starten von Übertragungen mit bereits
bekannten Partnern. Die wichtigsten Features, die wir in nächster Zeit umsetzen wollen sind im Frontend die
Implementierung eines Fensters für die Einstellungen der App, das Fenster zur Herstellung einer Verbindung, die Toolbar
mit den wichtigsten Aktionen der App an einem Punkt vereint sowie die Sidebar, über dessen Inhalt intern noch diskutiert
wird. Im Backend fehlt die Umsetzung einer festen, geregelten Architektur. Momentan versuche ich Vor- und Nachteile
verschiedener Architekturen abzuwiegen und besonders auch auf unser Projekt hinsichtlich Komplexität und Zeitaufwand zu
beziehen. Die besten Kandidaten zurzeit sind Event-Driven-Architecture (besonders für die Kommunikation zwischen den
Threads), Microservice-Architecture und dem bisher verwendeten MVCS-Paradigma.

## 21.01.2026