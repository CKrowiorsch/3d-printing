# Gaming-Wandbilder

Sammlung sechseckiger Wandbilder für abgeschlossene Spiele. `ahsoka/` enthält die unveränderten Vorlagendateien; `patrizier2/` enthält das neue Motiv und sein Modell.

## Patrizier II

Das Motiv zeigt einen verkleinerten Kaufmann vor einem Kontorhaus. Stark ausgefranste Konturen laufen in die weiße Außenfläche aus; der Schriftzug „Patrizier 2“ ist erhaben. Es ist eine KI-generierte, von Patrizier II und der Hanse inspirierte Darstellung, keine überprüfte Reproduktion einer konkreten Spielfigur. Das STL ist ein aus Grauwerten erzeugtes Höhenrelief im HueForge-Stil; es wurde nicht in HueForge erstellt oder auf bestimmte Filamente kalibriert.

- Außenmaße: 165,982 × 143,544 × 2,55 mm. Breite und Höhe entsprechen dem Ahsoka-STL; der hervorgehobene Schriftzug ragt 0,23 mm über die maximale ursprüngliche Reliefhöhe von 2,32 mm hinaus.
- `motiv.png`: Ausgangsmotiv; `motiv_mit_schrift.png`: Motiv mit Schriftzug vor dem Zuschnitt auf das Sechseck; `erzeuge_modell.py`: bearbeitbare Erzeugung (Python, NumPy, Pillow und Windows-Schrift Georgia Bold); `patrizier2.stl`: exportiertes Modell.
- Flache Unterseite auf die Druckplatte, Motiv nach oben. Stützen sind für die Geometrie voraussichtlich nicht erforderlich.
- Ausgangspunkt: PLA von dunkel nach hell, z. B. Schwarz, Dunkelgrau, Hellgrau und Weiß. Die Ahsoka-3MF enthält Farbwechsel bei 0,96, 1,28 und 1,76 mm; diese Höhen können als Ausgangspunkt dienen, sind für dieses neue Motiv aber nicht kalibriert. Im Slicer Schichtvorschau und tatsächliche Farben prüfen und bei Bedarf anpassen.
- `Patrizier2_Ahsoka_Farben.3mf` enthält das P2S-Profil, die PLA-Palette Schwarz (#000000), Blau (#7288B1), Silber (#C0C0C0) und Weiß (#FFFFFF) sowie die Farbwechsel der Ahsoka-Vorlage. Das Skript aktualisiert die Geometrie dieses Projekts, wenn die 3MF-Datei vorhanden ist. Kein G-Code enthalten; die Farbabstimmung benötigt einen Probedruck.

Die Modellprüfung ergab die genannten Abmessungen und eine geschlossene Dreiecksoberfläche (jede Netzkante hat zwei angrenzende Dreiecke). Bambu Studio hat die 3MF erfolgreich importiert und die Geometrie als STL exportiert. Eine Schichtvorschau oder Druckprüfung wurde noch nicht durchgeführt.




