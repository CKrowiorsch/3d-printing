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
stars = [(330,95,13),(690,105,11),(135,450,13),(895,440,12),(145,585,11),(880,580,13),(335,915,12),(685,915,13)]
for x,y,r in stars:
    points=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5
        radius=r if i%2==0 else r*0.43
        points.append((x+radius*math.cos(a),y+radius*math.sin(a)))
    draw.polygon(points, fill=0)
canvas.save(p / 'motiv-v4.png')

