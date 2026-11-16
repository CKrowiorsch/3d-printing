# Cyberpunk 2077 – Variante 2

Das vorhandene Motiv wurde für ein flaches Sechseck-Relief im Stil der Sammlung weiterverwendet; die Figur ist eine inspirierte Darstellung. Die ursprünglichen Dateien bleiben erhalten. Das Bild ist ein Höhenrelief im HueForge-Stil, nicht mit HueForge oder konkreten Filamenten kalibriert.

- 165,982 × 143,544 × 2,55 mm; Grundfläche wie Ahsoka, mit waagerechter Ober- und Unterkante. Das Bildrelief reicht bis 2,32 mm; helle Pixel im Schriftbereich werden auf 2,55 mm angehoben. Auch andere helle Details in diesem Bereich können angehoben sein.
- `erzeuge_modell_v2.py` erzeugt aus `motiv.png` das STL, die Bildvorschau und das 3MF. Es benötigt Python, NumPy, Pillow und das jeweils mitgelieferte 3MF als Projektvorlage. Raster 513 × 513; Gamma 1,65. Die Vorschau zeigt den Bildzuschnitt, keine simulierten Filamentfarben oder Slicer-Schichten.
- Das 3MF übernimmt das P2S-Projekt und die Palette der Patrizier-Vorlage: Schwarz, Blau, Silber und Weiß. Farbwechsel liegen bei 0,96, 1,28 und 1,76 mm; diese sind ein unkalibrierter Ausgangspunkt. Filamente und AMS-Zuordnung in Bambu Studio prüfen. Kein geslicter Druckauftrag enthalten.
- Flache Rückseite auf die Druckplatte, Motiv nach oben; Stützen voraussichtlich nicht nötig. PLA ist ein Ausgangspunkt. Feine Schrift und Details sowie Farbwiedergabe in der Schichtvorschau prüfen; ein Probedruck ist sinnvoll.
- Geometrieprüfung: 1.052.672 Dreiecke, jede indizierte Netzkante genau zweimal vorhanden; Abmessungen wie oben. 3MF-ZIP und relevante XML-Dateien erfolgreich geprüft. Kein Import in Bambu Studio, keine Schichtvorschau und kein Drucktest durchgeführt.

## Variante 3

Die KI-Bildbearbeitung verkleinert die Figur und ergänzt eine futuristische Stadtkulisse. Ausgefranste Pinselstriche laufen in einen weißen Rand aus, angelehnt an Patrizier II. `motiv-v3.png` ist das Ausgangsbild, `erzeuge_modell_v3.py` erzeugt STL, Vorschau und 3MF. Die Maße, Druckorientierung, Farbwechsel und Einschränkungen entsprechen Variante 2. Helle Pixel im Bildbereich des Schriftzugs werden auf 2,55 mm angehoben; einzelne angrenzende helle Bilddetails können eingeschlossen sein. Die Vorschau zeigt den Bildzuschnitt, keine Slicer-Schichten. Netzprüfung: 1.052.672 Dreiecke und jede indizierte Kante zweimal; ein Slicer- und Drucktest stehen aus.

## Variante 4

Das KI-bearbeitete Motiv besitzt einen breiteren hellen Rand und läuft mit Leiterbahnen, Mikrochips, digitalen Fragmenten und kleinen Stadtsilhouetten aus. `motiv-v4.png` ist das Ausgangsbild, `erzeuge_modell_v4.py` erzeugt STL, Vorschau und 3MF. Maße, Orientierung und Farbwechsel entsprechen Variante 2. Helle Pixel im Schriftbereich werden auf 2,55 mm angehoben; angrenzende helle Details können ebenfalls angehoben werden. Die Vorschau ist keine Slicer-Schichtvorschau. Netzprüfung: 1.052.672 Dreiecke, jede indizierte Kante zweimal; 3MF-ZIP und relevante XML-Dateien geprüft. Slicer- und Drucktest stehen aus; besonders feine Leiterbahnen und Schrift prüfen.

## Variante 5

Das Motiv von Variante 4 wurde zentriert um den Faktor 1,35 vergrößert und auf das gleiche Sechseck übertragen; der verbleibende Rand ist visuell an Ahsoka angelehnt, nicht exakt vermessen. Technische Randmotive bleiben erhalten. `motiv-v5.png`, `erzeuge_modell_v5.py`, STL und 3MF bilden die neue Variante. Abmessungen und Farbwechsel wie Variante 4. Netzprüfung: jede indizierte Kante zweimal, 1.052.672 Dreiecke; ZIP und relevante XML-Dateien geprüft. Eine Slicer-Schichtvorschau und ein Drucktest stehen aus.

## Variante 6

Das Bild von Variante 5 wurde mittig um 18 % vertikal gestreckt; die Außenmaße und Farbwechsel des Sechsecks bleiben gleich. `motiv-v6.png` ist das gestreckte Ausgangsbild, `erzeuge_modell_v6.py` erzeugt STL, Vorschau und 3MF. Netzprüfung: 1.052.672 Dreiecke, jede indizierte Kante zweimal; ZIP und relevante XML-Dateien geprüft. Die Bildvorschau zeigt keine Filamentfarben oder Slicer-Schichten. Slicer- und Drucktest stehen aus.
