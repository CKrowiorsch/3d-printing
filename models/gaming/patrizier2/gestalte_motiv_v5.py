from pathlib import Path
from PIL import Image, ImageDraw, ImageOps
import math
p = Path(__file__).resolve().parent
# Das Bild ist quadratisch; unterschiedliche Skalierung kompensiert das Seitenverhältnis des Sechsecks.
scale_x, scale_y = 0.70, 0.85
canvas = Image.new('L', (1024, 1024), 255)
source = ImageOps.fit(Image.open(p / 'motiv-v3.png').convert('L'), (1024, 1024), method=Image.Resampling.LANCZOS)
source = source.resize((round(1024*scale_x), round(1024*scale_y)), Image.Resampling.LANCZOS)
canvas.paste(source, ((1024-source.width)//2, (1024-source.height)//2))
draw = ImageDraw.Draw(canvas)
# Positionen in Bildkoordinaten; die Sterne liegen innerhalb der Sechseckkontur.
stars = [(318,92,12),(350,113,7),(371,81,5),(701,96,11),(672,75,6),(724,125,7),(128,423,11),(151,455,7),(114,468,5),(903,446,12),(875,416,7),(919,478,5),(137,604,9),(161,630,5),(892,608,10),(866,634,6),(324,919,11),(352,946,6),(302,947,5),(693,917,12),(665,946,7),(720,941,5)]
for x,y,r in stars:
    points=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5
        radius=r if i%2==0 else r*0.43
        points.append((x+radius*math.cos(a),y+radius*math.sin(a)))
    draw.polygon(points, fill=0)
canvas.save(p / 'motiv-v5.png')


