# Gaming-Wandbilder

Sammlung sechseckiger Wandbilder für abgeschlossene Spiele. `ahsoka/` enthält die unveränderten Vorlagendateien; `patrizier2/` enthält das neue Motiv und sein Modell.

## Patrizier II

Das Motiv ist eine KI-generierte, von Patrizier II und der Hanse inspirierte Darstellung eines Kaufmanns, keine überprüfte Reproduktion einer konkreten Spielfigur. Das STL ist ein aus Grauwerten erzeugtes Höhenrelief im HueForge-Stil; es wurde nicht in HueForge erstellt oder auf bestimmte Filamente kalibriert.

- Außenmaße: 165,982 × 143,544 × 2,55 mm. Breite und Höhe entsprechen dem Ahsoka-STL; der hervorgehobene Schriftzug ragt 0,23 mm über die maximale ursprüngliche Reliefhöhe von 2,32 mm hinaus.
- `motiv.png`: Ausgangsmotiv; `motiv_mit_schrift.png`: Motiv mit Schriftzug vor dem Zuschnitt auf das Sechseck; `erzeuge_modell.py`: bearbeitbare Erzeugung (Python, NumPy, Pillow und Windows-Schrift Georgia Bold); `patrizier2.stl`: exportiertes Modell.
- Flache Unterseite auf die Druckplatte, Motiv nach oben. Stützen sind für die Geometrie voraussichtlich nicht erforderlich.
- Ausgangspunkt: PLA von dunkel nach hell, z. B. Schwarz, Dunkelgrau, Hellgrau und Weiß. Die Ahsoka-3MF enthält Farbwechsel bei 0,96, 1,28 und 1,76 mm; diese Höhen können als Ausgangspunkt dienen, sind für dieses neue Motiv aber nicht kalibriert. Im Slicer Schichtvorschau und tatsächliche Farben prüfen und bei Bedarf anpassen.
- Kein G-Code oder fertiges Bambu-Studio-Profil enthalten. Düse, Schichthöhe, Materialien und Farbwechsel vor dem Druck im Slicer einstellen; ein kleiner Probedruck hilft bei der Farbabstimmung.

Die Modellprüfung ergab die genannten Abmessungen und eine geschlossene Dreiecksoberfläche (jede Netzkante hat zwei angrenzende Dreiecke). Eine Slicer- oder Druckprüfung wurde noch nicht durchgeführt.



