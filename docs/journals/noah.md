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
        * [Shared Memory](#shared-memory)
        * [Message Passing](#message-passing)
        * [Weiterführende Lösungen](#weiterführende-lösungen)
    * [05.02.2026](#05022026)
    * [12.02.2026](#12022026)
    * [26.02.2026](#26022026)
    * [05.03.2026](#05032026)
    * [13.03.2026](#13032026)
    * [19.03.2026](#19032026)

**\[ Nachtrag basierend auf Git-Historie \]**

## 29.10.2025

Am 29.10. habe ich mit der Projektarbeit durch das Erstellen des Git-Repositorys sowie dessen Einrichtung begonnen.
Dabei habe ich mich zuerst um einen Namen für das Projekt gekümmert und bin auf "Avian" (z. Dt. Vogel-), aufgrund der
Verbindung zwischen Vögeln und Freiheit (→ Dezentralisierung & Open Source). Ich habe ebenfalls das Kanban-Board sowie
den Zugriff für Teammitglieder auf das Repository eingerichtet und erste Tickets/Issues erstellt und zugewiesen.

## 12.11.2025

Am 12.11. habe ich angefangen, die Projektstruktur festzulegen und habe dafür erste Module, Dateien und Klassen
erstellt. Anschließend habe ich mich um weitere organisatorische Dinge, wie das Einrichten des Code-Editors meiner
Teammitglieder, sowie deren Verbindung zur Remote, gekümmert.

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
vorgesehen. Hier befinden sich außerdem bei uns viele Typ- bzw. Klassendeklarierungen.

Ein View ist in unserem Fall die grafische Benutzeroberfäche. Der View visualisiert Daten, die er vom Controller
erhält. Außerdem leitet der View Eingaben von Benutzern (darunter Textfeld-Eingaben, Button-Klicks, etc.) an den
Controller weiter.

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
uns entschieden, dieses nur umzusetzen, wenn wir nach dem Erreichen unserer neu abgeänderten Definition of Done noch
ausreichend Zeit für eine solche Implementierung hätten. Ein weiteres Feature, das aufgrund der Retrospektive weichen
musste ist eine Liste an kürzlichen Übertragungen so wie eine Kontaktähnliche Liste für das schnelle Starten von
Übertragungen mit bereits bekannten Partnern. Die wichtigsten Features, die wir in nächster Zeit umsetzen wollen sind im
Frontend die Implementierung eines Fensters für die Einstellungen der App, das Fenster zur Herstellung einer Verbindung,
die Toolbar mit den wichtigsten Aktionen der App an einem Punkt vereint sowie die Sidebar, über dessen Inhalt intern
noch diskutiert wird. Im Backend fehlt die Umsetzung einer festen, geregelten Architektur. Momentan versuche ich Vor-
und Nachteile verschiedener Architekturen abzuwiegen und besonders auch auf unser Projekt hinsichtlich Komplexität und
Zeitaufwand zu beziehen. Die besten Kandidaten zurzeit sind Event-Driven-Architecture (besonders für die Kommunikation
zwischen den Threads), Microservice-Architecture und dem bisher verwendeten MVCS-Paradigma.

## 21.01.2026

Heute habe ich weiter über mögliche Umsetzungen der Thread-Synchronization-Implementierung bzw. die Art und Weise der
Kommunikation zwischen den Threads nachgedacht und habe ebenfalls einige Muster dafür entworfen. Dabei gibt es zwei
Oberkategorien mit Unterpunkten, die abgewogen werden müssen:

### Shared Memory

Shared Memory ist ein Pattern, in dem der gleiche Speicher von unterschiedlichen Threads abgefragt und modifiziert
werden darf. Dabei können verschiedene Herangehensweisen benutzt werden:

- Mutex (Mutual Exclusion Lock): Ein Mutex sorgt dafür, dass jeder Thread, der einen bestimmten Abschnitt des Codes
  aufruft, ein sogenannten *Lock* vom Mutex abzurufen (*acquire*), welcher verhindert, dass ein anderer Thread auf den
  Abschnitt zugreifen kann. Wenn der Thread mit dem Abschnitt fertig ist, muss der *Lock* des Mutexes freigegeben
  werden (*release*), sodass der andere Thread auf den Bereich mit der gleichen Herangehensweise zugreifen kann.
- Konditionsvariablen: Konditionsvariablen werden gemeinsam mit einem Mutex benutzt, um nur auf eine Variable
  zuzugreifen, wenn ein bestimmter Fall eintrifft.
- Semaphoren: Semaphoren werden dafür benutzt, dass lediglich eine begrenzte Anzahl an Threads gleichzeitig Zugriff
  erhalten.

### Message Passing

Message Passing beschreibt den Austausch von Daten, der nicht über die vorher beschriebenen Wege von geteiltem Speicher
läuft, sondern über das Senden von Daten über eine Brücke. Auch diese Herangehensweise ist in verschiedene
Unterkategorien aufgeteilt:

- Queues: Eine Queue ist eine Möglichkeit zum Datenaustausch durch das Übergeben (*passing*) von Daten. Das
  System ist mit einer Art Briefkasten vergleichbar, auf den permanent zugegriffen werden kann. Eine Seite kann etwas in
  die Queue hereingeben (*put*) und die andere kann
- Channels: Ein Channel basiert auf einer Queue und bietet zusätzliche Struktur und Sicherheit. Dieser kann für weitere
  High-Level Implementierungen, wie beispielsweise einen EventBus benutzt werden.

### Weiterführende Lösungen

Weiterführend werden diese Mechanismen für die Implementierung einer der folgenden Lösungen für die
Cross-Thread-Kommunikation genutzt:

- EventBus: Ein EventBus ist ein Interface, welches Messages/Events annimmt (*emit*/*post*) und an die zuständigen
  *Event Handler* (*subscribe*) anbindet. Die hinterlegte Funktion wird, sobald ein Event emittiert wird, ausgeführt.
  Gegebenenfalls ist der gezielte Event-Handler keine Funktion, sondern ein *Consumer* mit Typ *T*, der die Klasse des
  Ziels des Event Handlers darstellt.
- Dispatcher/Invocation Queue: Mithilfe des Dispatching-Systems kann man Code, der in einem Thread definiert ist, durch
  den Dispatcher auf einem anderen Thread (bzw. in einem anderen Event Loop) ausführen. Für dieses Design muss auf
  beiden Seiten ein Event Loop vorliegen und eine Polling/Tick Rate festgelegt werden.

## 05.02.2026

Heute habe ich die Struktur des Git-Repositories noch einmal überarbeitet, indem ich den `next`-Branch erstellt habe.
Der `master`-Branch wird nur noch Stable-Versionen beinhalten, der neue `next`-Branch agiert hingegen als
Development-Environment. Und mich final für eine EventBus-ähnliche Implementierung (High-Level Interface für Message
Passing mittels Channels) als Lösung für die Thread Synchronization entschieden. Außerdem habe ich versucht, das Team
trotz der Probleme mit dem Git Server zu organisieren und unsere nächsten Schritte bezüglich zeitlicher Planung
festzustellen.

## 12.02.2026

Heute habe ich mich wieder um das Warten der Module gekümmert und verschiedene alte Module, die wir nicht mehr benötigt
haben, gelöscht. Außerdem habe ich die Implementierung des Thread-Safe-Channels finalisiert und den anderen bei ihren
Problemen mit dem Loadingwindow und der Toolbar geholfen. Zudem habe ich unsere Dependencies upgegradet, um eine
High-Severity CVE, [2026-26007](https://nvd.nist.gov/vuln/detail/CVE-2026-26007), zu beheben. Dabei habe ich
gleichzeitig noch unseren Language Server und Linter auf die neuste Version upgegradet. Weiterführend habe ich weiter
das Projekt aufgeräumt, indem ich einige ungenutzte Teile des Projektes zunächst gelöscht habe. Ebenso habe ich aus
Kompatibilitätsgründen die minimale Python-Version des Projektes auf 3.11.0 geändert (vorher 3.14) und
Interpreter-Versionsspezifisches Syntax und anderes angepasst, sowie die Jahreszahl in LICENSE angepasst. Ich habe auch
verschiedene Scripts erstellt, um die App in verschiedenen Umgebungen schnell starten zu können und um einige
Kompatibilitätsprobleme zu beheben.

## 26.02.2026

Heute habe ich mich letztendlich gegen die Nutzung von `trio` und somit Asynchroner Programmierung entschieden, da diese
Konzepte das Projekt wahrscheinlich unnötig verkomplizieren und in die Länge ziehen. Deshalb habe ich auch zuerst alle
damit zusammenhängenden Abhängigkeiten entfernt und eine weitere kleine Bibliothek hinzugefügt: Das `attrs` Paket bietet
einige für uns nützliche Utils, für die Erstellung von Dataclasses. Dieses war in `trio` enthalten und bereits in Teilen
der Codebase eingebaut. Außerdem habe ich heute die ersten `Message`-Klassen erstellt, die als Event fungieren sollen
und zwischen Frontend und Backend für die Kommunikation benutzt werden sollen. Zudem habe ich `constants.py` als
zentralen Speicherort von Konstanten wie der Protokollversion oder dem Logger erstellt sowie einige Helper-Funktionen
für das Generieren und Verifizieren von Checksums erstellt. Heute habe ich ebenfalls mit der Netzwerk-Layer des
Programms angefangen. Dazu habe ich zuerst einen einfachen TCP-Wrapper in `protocol.py` definiert, der das
Streamorientierte Protokoll zu einem Paket-/Frameorientiertem Protokoll umfunktionieren soll. TCP ist für unseren Fall
perfekt, da es nahezu überall Adaption hat, Reliability aufweist und Ordered Delivery unterstützt aber auch
hauptsächlich, weil es Verbindungsorientiert ist, was bedeutet, dass unser Programm über die gleiche etablierte
Verbindung einzelne Teile einer Datei schicken kann, ohne sich dabei um andere Faktoren wie Connection State,
Out-of-Order-Delivery sowie Congestion- und Flow Control kümmern zu müssen.

Zusätzlich zu den ersten Fortschritten im Bereich Netzwerk habe ich mit dem Service-System des Backends angefangen und
dazu die abstrakte Basisklasse `Service` erstellt, von denen jeder Service, der in Zukunft erstellt wird, erben wird. Um
die Funktionalität der Basisklasse und den dazugehörigen Funktionalitäten zu prüfen, habe ich außerdem mit der ersten
Iteration des Receiver-Services angefangen.

Zuletzt habe ich noch einige Fehler bezüglich Imports gefixt, darunter einige Circular Imports und mit dem Setup
inkompatible Imports.

## 05.03.2026

Heute habe ich zunächst einige der Netzwerkkomponenten neu organisiert und den Receiver-Service komplettiert. Außerdem
habe ich `constants.py` geändert und weitere Werte hinzugefügt. Zudem habe ich an der Entwicklung des Sender-Services
angefangen und anschließend einige Aspekte, die ich bei der ersten Iteration des Receiver-Services vergessen hatte, von
der neuen Sender Implementierung zu übernehmen. Zusätzlich habe ich durch die Fertigstellung beider Seiten die
Möglichkeit, mein vorher definiertes Protokoll auf Fehler zu überprüfen, wobei ich auf den Fehler gestoßen bin, dass die
`socket.recv(bufsize: int)` Methode nicht exact `bufsize` Bytes empfängt, sondern maximal. Dies habe ich mit der
Implementierung einer `recv_exact(...)` Funktion behoben, die die empfangenen Bytes in einem internen Puffer speichert
und erst zurückgibt, wenn die gegebene Anzahl an Bytes im Puffer vorhanden ist. Ebenso habe ich die Funktionalität
eingebaut, Receiver und Sender über das Backend zu starten und die Implementierung des Channels umgeschrieben, um
HOL-Blocking in Receiver und Sender durch das Erreichen der Puffergröße des Channels zu verhindern, indem ich die
Puffergröße bei negativen Eingaben ignoriere und somit eine theoretisch unlimitierte Anzahl an Messages in dem Channel
gespeichert werden können. Außerdem habe ich im Frontend mit der Event-Handler Funktionalität angefangen und die erste
Iteration des Event-Consumers im Frontend festgelegt. Ich habe ebenso im Frontend den File Dialog implementiert und
Enrico bei der Implementierung des groben Systems der Settings zugeschaut und geholfen sowie Luca einige Tipps zum
Einsetzen von Einträgen in den TreeView im Mainframe gegeben. Danach hatten wir unsere Projektvorstellung. Zuletzt habe
ich heute eine weitere Util-Klasse für das formattieren von Binär- und Dezimalzahlen mit Präfixen erstellt, die bspw.
für die Geschwindigkeit und Dateigröße in der Mainframe Anzeige benötigt werden und den Event-Consumer im Frontend
fertiggestellt und mit weiteren Event Handlern versehen, die Definition of Done dem Repository als Markdown-Datei
überarbeitet hinzugefügt und das grundlegende Branding Material für das Programm erstellt sowie eine Helper-Funktion für
das Öffnen von Ordnern hinzugefügt.

## 13.03.2026

Heute haben wir uns um einige kleinere Aspekte der App gekümmert, um organisatorisch Platz für das Backlog Refinement
und das letzte Sprint Planning zu schaffen. Im Refinement habe ich hauptsächlich Tickets gelöscht, die unwichtig
und/oder unrealistisch für den letzten Sprint sind und im Planning habe ich mit den anderen die letzten Tickets, die
realistisch zu schaffen, oder für den letzten Sprint als absolut notwendig erachtet sind, erstellt. Dazu zählen auch die
Aufgaben der anderen, die ich ihnen bereits vor dem Refinement/Planning gegeben habe: Enrico sollte weiterhin die
Probleme an den Settings beheben, Dominik hat sich um einen Button gekümmert, der die heruntergeladenen Dateien öffnet
und Luca hat an einem Spike gearbeitet, der die Möglichkeit der Implementierung von Icons in der gesamten App
feststellen sollte. Der Spike hat sich als Erfolg bewiesen, da Luca zwei Icons zu dem _New Connection_-Button und dem
_Settings_-Button hinzufügen konnte; beide davon in einer anderen Ausführung. Dafür hat Luca zuerst Platzhalter-Icons
benutzt. Diese habe ich anschließend durch unsere eigenen Icons ersetzt und noch ein weiteres Icon zu dem von Dominik
neu erstellten _Saves_-Button hinzugefügt. Ich habe derzeit an dem Updaten und Löschen von Items in Mainframe's TreeView
gearbeitet und zwei Helper-Methoden dafür aufgestellt, eine Überschrift zu der Anhangsliste im `ConnectionWindow`
hinzugefügt und einen Berechnungsfehler in Sender und Receiver behoben. Außerdem habe ich die Rate, in der Sender und
Receiver ihre Updates senden, zeitlich limitiert.

## 19.03.2026