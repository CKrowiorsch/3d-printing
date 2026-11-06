# Hinweise für die Arbeit in diesem Projekt

## Projekt und Drucker

Dieses Repository sammelt Druckvorlagen und 3D-Modelle. Der Drucker heißt **Bambi** und ist ein **Bambu Lab P2S mit AMS Pro**. Antworte und dokumentiere standardmäßig auf Deutsch.

## Modelle erstellen und ändern

- Kläre bei fehlenden, funktionsentscheidenden Angaben die benötigten Maße, den Einsatzzweck, das Material und gegebenenfalls die Montage. Triff einfache Annahmen selbst und kennzeichne sie.
- Verwende Millimeter als Einheit. Berücksichtige Wandstärke, Belastungsrichtung, Druckorientierung, Überhänge, Auflagefläche und bei Bedarf Stützstrukturen.
- Konstruiere Passungen, bewegliche Teile und Verbindungen mit geeigneten, ausdrücklich dokumentierten Spielmaßen. Schlage bei kritischen Passungen einen kleinen Testdruck vor; tatsächliche Toleranzen hängen von Material und Druckeinstellungen ab.
- Bevorzuge editierbare, parametrische Quelldateien, wenn ein Modell neu erstellt oder wesentlich verändert wird. Wähle das Werkzeug passend zur Aufgabe und halte wichtige Maße und Parameter leicht auffindbar.
- Lege neue Projekte in einem passend benannten Unterordner von `models/` ab. Bewahre Quelldateien zusammen mit exportierten Druckdateien auf. Nutze `tryouts/` für Versuche und `settings/` für zugehörige Einstellungen, sofern passend.
- Überschreibe keine vorhandenen Modelle oder Varianten ohne Anlass. Respektiere vorhandene Dateinamen und die bestehende Projektstruktur.

## Druckvorbereitung und Prüfung

- Liefere je nach Aufgabe ein geeignetes Druckformat, etwa STL oder 3MF, zusätzlich zur editierbaren Quelle. Erstelle G-Code nur, wenn er ausdrücklich verlangt wird und ein passendes Drucker-, Düsen-, Material- und Slicerprofil bekannt ist.
- Prüfe erzeugte Geometrie soweit mit den verfügbaren Werkzeugen möglich auf korrekte Abmessungen, geschlossene und druckbare Körper sowie offensichtliche Geometriefehler. Berichte nachvollziehbar, was tatsächlich geprüft wurde und was nicht.
- Prüfe, ob das Modell in den verfügbaren Bauraum passt; verifiziere konkrete Druckerspezifikationen und Profile, bevor du sie als Grenze verwendest. Bei großen Modellen schlage bei Bedarf eine sinnvolle Teilung vor.
- Berücksichtige das AMS Pro bei Material- und Mehrfarbentscheidungen. Behaupte keine Materialkompatibilität, ohne sie für die konkrete Kombination geprüft zu haben.
- Gib bei neuen Modellen knapp Maße, vorgesehene Druckorientierung, empfohlene Materialien, notwendige Stützen und wichtige Annahmen an. Druckeinstellungen sind Vorschläge und müssen zu Material, Düse und Profil passen.

## Sicherheit und vorhandene Dateien

- Versprich keine Eignung für lebensmittelberührende, sicherheitskritische oder stark belastete Anwendungen allein aufgrund des Modells. Weise bei entsprechendem Einsatzzweck auf nötige Materialwahl und praktische Prüfung hin.
- Behandle vorhandene STL-, 3MF- und G-Code-Dateien als Projektdaten. Verändere oder lösche sie nur im Rahmen des konkreten Auftrags.
