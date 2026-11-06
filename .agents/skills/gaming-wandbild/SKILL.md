---
name: gaming-wandbild
description: Erstellt aus einem Computerspielnamen ein sechseckiges, mehrfarbiges 3D-Wandbild für die Gaming-Sammlung. Verwenden, wenn ein neues Spielmotiv im Stil der vorhandenen Gaming-Wandbilder gewünscht ist.
---

# Gaming-Wandbild erstellen

Erstelle für ein abgeschlossenes Spiel ein Wandbild in `models/gaming/<spielname>/`. Orientiere dich an `models/gaming/ahsoka/` als Maßvorlage und an `models/gaming/patrizier2/` als Beispiel für Motiv, erhabenen Titel und reproduzierbares Höhenrelief. Lies `models/gaming/README.md` für den aktuellen Stand. Bestehende Vorlagen und Varianten erhalten.

## Vom Spiel zum Motiv

1. Identifiziere das gewünschte Spiel und recherchiere bei Bedarf dessen charakteristische Figuren und Bildsprache. Wenn der Spielname mehrdeutig ist oder mehrere Figuren gleich naheliegen, kläre die Auswahl; andernfalls wähle ein erkennbares Motiv und dokumentiere die Wahl. Behaupte keine originalgetreue Figur, wenn die Darstellung nur inspiriert ist.
2. Erzeuge mit dem verfügbaren Bildgenerierungswerkzeug ein kontrastreiches Motiv mit wenigen gut unterscheidbaren Helligkeitsstufen, geeignet für ein flaches Mehrfarbenrelief. Die Figur soll das Sechseck gut ausfüllen; orientiere dich an der ursprünglichen Patrizier-Komposition. Bewahre das Ausgangsbild auf.
3. Integriere den Spieltitel gut lesbar in das Motiv. Hebe die Buchstaben im Relief hervor; setze standardmäßig keinen rechteckigen Hintergrund um den Schriftzug. Übernimm ausdrücklich geäußerte Wünsche zu Motiv, Rand und Schrift vor diesen Vorgaben.

## Modell und Druck

- Miss die tatsächliche Ahsoka-STL-Vorlage oder verifiziere die dokumentierten Abmessungen: ungefähr 165,982 × 143,544 mm, flaches Sechseck mit horizontalen Ober- und Unterseiten. Verwende dieselbe Grundfläche. Die Höhe der Ahsoka-Vorlage beträgt 2,32 mm; eine hervorgehobene Schrift darf darüber hinausragen.
- Erzeuge eine editierbare oder reproduzierbare Quelle und ein STL oder ein anderes gewünschtes Druckformat. Das Skript `models/gaming/patrizier2/erzeuge_modell.py` ist ein anpassbares Beispiel für die Umwandlung eines Bildes in ein geschlossenes Höhenrelief. Parameter, Bild und Schrift sollen austauschbar bleiben; vorhandene Spielmodelle nicht überschreiben.
- Richte das Modell mit flacher Rückseite auf dem Druckbett und dem Motiv nach oben aus. Berücksichtige die Druckbarkeit von Details und Schrift. Gib sinnvolle Material- und Farbwechselvorschläge, aber behaupte keine Kalibrierung: Das Ergebnis ist ein Relief im HueForge-Stil, sofern es nicht tatsächlich mit HueForge und konkreten Filamenten erstellt wurde.
- Prüfe Abmessungen und geschlossenes Netz mit verfügbaren Werkzeugen, möglichst auch die Slicer-Schichtvorschau. Dokumentiere genau, was geprüft wurde und was noch offen ist. Nenne Ausrichtung, Materialien, Farbwechsel und gegebenenfalls einen Probedruck. Erstelle G-Code nur auf ausdrücklichen Wunsch mit bekanntem passenden Profil.
- Zeige dem Nutzer das Motiv und verlinke das Modell sowie die Quelldateien. Dokumentiere relevante Annahmen und alle Abweichungen von der Vorlage im Projekt.
