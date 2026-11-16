# Gaming-Wandbilder

Sammlung sechseckiger Wandbilder für abgeschlossene Spiele. `ahsoka/` enthält die unveränderten Vorlagendateien; `patrizier2/` enthält das neue Motiv und sein Modell.

## Patrizier II

Das Motiv zeigt einen verkleinerten Kaufmann vor einem dunklen Kontorhaus und einem Handelsschiff rechts oberhalb der Figur. Kräftige schwarze Hintergrundflächen betonen die hellen Details. Eine dunklere Höhenabstimmung (Gamma 1,65) erhöht den Schwarzanteil; isolierte weiße Inseln unter 0,8 mm² werden auf den weißen Schichten abgesenkt. Der Schriftzug ist von dieser Filterung ausgenommen. Stark ausgefranste Konturen laufen in die weiße Außenfläche aus; der Schriftzug „Patrizier 2“ ist erhaben. Es ist eine KI-generierte, von Patrizier II und der Hanse inspirierte Darstellung, keine überprüfte Reproduktion einer konkreten Spielfigur. Das STL ist ein aus Grauwerten erzeugtes Höhenrelief im HueForge-Stil; es wurde nicht in HueForge erstellt oder auf bestimmte Filamente kalibriert.

- Außenmaße: 165,982 × 143,544 × 2,55 mm. Breite und Höhe entsprechen dem Ahsoka-STL; der hervorgehobene Schriftzug ragt 0,23 mm über die maximale ursprüngliche Reliefhöhe von 2,32 mm hinaus.
- `motiv.png`: Ausgangsmotiv; `motiv_mit_schrift.png`: Motiv mit Schriftzug vor dem Zuschnitt auf das Sechseck; `erzeuge_modell.py`: bearbeitbare Erzeugung (Python, NumPy, Pillow und Windows-Schrift Georgia Bold); `patrizier2.stl`: exportiertes Modell.
- Flache Unterseite auf die Druckplatte, Motiv nach oben. Stützen sind für die Geometrie voraussichtlich nicht erforderlich.
- Ausgangspunkt: PLA von dunkel nach hell, z. B. Schwarz, Dunkelgrau, Hellgrau und Weiß. Die Ahsoka-3MF enthält Farbwechsel bei 0,96, 1,28 und 1,76 mm; diese Höhen können als Ausgangspunkt dienen, sind für dieses neue Motiv aber nicht kalibriert. Im Slicer Schichtvorschau und tatsächliche Farben prüfen und bei Bedarf anpassen.
- `Patrizier2_Ahsoka_Farben.3mf` enthält das P2S-Profil, die PLA-Palette Schwarz (#000000), Blau (#7288B1), Silber (#C0C0C0) und Weiß (#FFFFFF) sowie die Farbwechsel der Ahsoka-Vorlage. Das Skript aktualisiert die Geometrie dieses Projekts, wenn die 3MF-Datei vorhanden ist. Kein G-Code enthalten; die Farbabstimmung benötigt einen Probedruck.

Die Modellprüfung ergab die genannten Abmessungen und eine geschlossene Dreiecksoberfläche (jede Netzkante hat zwei angrenzende Dreiecke). Bambu Studio hat die 3MF erfolgreich importiert und die Geometrie als STL exportiert. Eine Schichtvorschau oder Druckprüfung wurde noch nicht durchgeführt.







## Patrizier II – Variante 3

Das vorhandene Motiv wurde mit dem integrierten Bildgenerator bearbeitet. Anker, Koggen, Fässer, Münzen, Speicherhäuser, Wellen und Tauwerk ergänzen den Rand als von Hanse und Handel inspirierte Symbole; das Ergebnis ist keine originalgetreue Darstellung aus dem Spiel. Die Bildbearbeitung bildet einen zusammenhängenden Schmuckrand; feine Details können beim Druck verloren gehen. Der Schriftzug wird im Skript ergänzt.

- `patrizier2/motiv-v3.png`: Ausgangsbild; `motiv-mit-schrift-v3.png` und `vorschau-v3.png`: Bild und Sechseckvorschau; `erzeuge_modell_v3.py`: reproduzierbare Quelle; `patrizier2-v3.stl` und `Patrizier2_Ahsoka_Farben_v3.3mf`: Druckdateien. Das Skript benötigt Python, NumPy, Pillow, Georgia Bold und die 3MF-Datei als Vorlage.
- 165,982 × 143,544 × 2,55 mm. Flache Rückseite auf das Druckbett, Motiv nach oben; Stützen voraussichtlich nicht nötig. PLA ist ein möglicher Ausgangspunkt. Das Bild ist ein unkalibriertes Höhenrelief im HueForge-Stil.
- Das 3MF übernimmt die vorhandene Palette und Farbwechsel bei 0,96, 1,28 und 1,76 mm aus der Projektvorlage. Filamente, AMS-Zuordnung und Farbwirkung im Slicer prüfen. Die Bildvorschau zeigt keine simulierten Schichten oder Filamentfarben.
- Geprüft: 1.052.672 Dreiecke, jede indizierte Netzkante zweimal; ZIP und Modell- und Verknüpfungs-XML geprüft. Kein Slicerimport, keine Schichtvorschau und kein Drucktest. Feine Symbole, Schrift und Farbwechsel vor dem Druck prüfen; ein Probedruck ist sinnvoll.
- Bildbearbeitungsauftrag: bestehendes Motiv und Bildstil erhalten; generische Ausfransungen durch Hanse-Handelsmotive ersetzen, angelehnt an die thematischen Randfragmente von Cyberpunk 2077.

## Patrizier II – Variante 4

Das Motiv von Variante 3 ist im Bild auf 70 % Breite und 85 % Höhe skaliert; bezogen auf das physische Sechseck wirkt es dadurch etwas höher als breit. Acht schwarze Sterne ergänzen den Außenbereich. Die Schrift wird separat in ursprünglicher Größe ergänzt. Die Außenmaße bleiben 165,982 × 143,544 × 2,55 mm.

`patrizier2/gestalte_motiv_v4.py` erzeugt aus `motiv-v3.png` das Bild `motiv-v4.png`; `erzeuge_modell_v4.py` erzeugt daraus `patrizier2-v4.stl` und aktualisiert `Patrizier2_Ahsoka_Farben_v4.3mf`. `vorschau-v4.png` zeigt das Bild innerhalb der Sechseckkontur, keine Slicer-Schichten. Die vorhandene 3MF-Datei dient dem Skript als Projektvorlage. Druckorientierung und Farbwechsel entsprechen Variante 3.

Geprüft: 1.052.672 Dreiecke, jede indizierte Netzkante zweimal; 3MF-ZIP und relevante Modell- und Verknüpfungs-XML geprüft. Slicerimport, Schichtvorschau und Drucktest stehen aus; besonders kleine Sterne und Bilddetails kontrollieren.

## Patrizier II – Variante 5

Variante 4 mit unregelmäßig angeordneten Sterngruppen unterschiedlicher Größe. `patrizier2/gestalte_motiv_v5.py` erzeugt `motiv-v5.png` aus dem Motiv von Variante 3; `erzeuge_modell_v5.py` erzeugt `patrizier2-v5.stl` und aktualisiert `Patrizier2_Ahsoka_Farben_v5.3mf`. `vorschau-v5.png` zeigt das Motiv innerhalb der Sechseckkontur, keine Schichtsimulation. Außenmaße, Ausrichtung und Farbwechsel entsprechen Variante 4.

Geprüft: 1.052.672 Dreiecke, jede indizierte Netzkante zweimal; ZIP und relevante XML-Dateien des 3MF sind lesbar. Slicerimport, Schichtvorschau und Drucktest stehen aus; besonders die kleinsten Sterne auf Druckbarkeit prüfen.

## Patrizier II – Variante 6

Der geschlossene Schmuckrand wurde mit dem integrierten Bildgenerator durch auslaufende Fragmente aus Handelssymbolen, Wellen und Tauwerk ersetzt; Sterngruppen bleiben erhalten. Als Bildreferenz diente Variante 5 und für die ausfransende Randgestaltung Cyberpunk 2077. Das Motiv ist eine inspirierte Darstellung. Das Ausgangsbild `ausgangsmotiv-v6.png` wird durch `gestalte_motiv_v6.py` auf die Bildfläche skaliert; `erzeuge_modell_v6.py` ergänzt die Schrift und erstellt `patrizier2-v6.stl` sowie das 3MF aus der vorhandenen Projektvorlage. Die Bildvorschau `vorschau-v6.png` ist keine Slicer-Schichtsimulation.

Außenmaße 165,982 × 143,544 × 2,55 mm; flache Rückseite auf das Bett, Motiv nach oben, Stützen voraussichtlich nicht nötig. PLA ist ein Ausgangspunkt. Die vorhandenen Farbwechsel bei 0,96, 1,28 und 1,76 mm sind nicht auf dieses Motiv kalibriert. Farbwirkung und AMS-Zuordnung im Slicer prüfen. Geprüft: 1.052.672 Dreiecke, jede indizierte Netzkante zweimal; 3MF-ZIP und relevante XML-Dateien lesbar. Slicerimport, Schichtvorschau und Drucktest stehen aus. Feine Fragmente und Sterne vor dem Druck prüfen.

Bildbearbeitungsauftrag: Kaufmann, Kontor, Schiff, Sterngruppen und monochromen Stil erhalten; den geschlossenen Rand in unregelmäßig auslaufende hanseatische Handelssymbole auflösen, angelehnt an die Randgestaltung von Cyberpunk 2077.
