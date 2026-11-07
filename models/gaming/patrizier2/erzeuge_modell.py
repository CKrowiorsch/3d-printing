"""Erzeugt ein geschlossenes Sechseck-Höhenrelief aus motiv.png (mm)."""
from pathlib import Path
import struct
import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

root = Path(__file__).resolve().parent
width, height, max_z, base_z = 165.98218, 143.54388, 2.32, 0.80
n = 257
im = Image.open(root / 'motiv.png').convert('L')
im = ImageOps.fit(im, (1024, 1024), method=Image.Resampling.LANCZOS)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 78)
text_mask = Image.new('L', im.size, 0)
mask_draw = ImageDraw.Draw(text_mask)
mask_draw.text((512, 789), 'Patrizier 2', font=font, fill=255, anchor='mm')
draw.text((512, 789), 'Patrizier 2', font=font, fill=255, anchor='mm', stroke_width=3, stroke_fill=0)
im.save(root / 'motiv_mit_schrift.png')
im = im.filter(ImageFilter.GaussianBlur(1.0))
pix = np.asarray(im, dtype=np.float32) / 255
ys = np.linspace(-height/2, height/2, n)
us = np.linspace(-1, 1, n)
y, u = np.meshgrid(ys, us, indexing='ij')
x = u * (width/2 - abs(y) * (width/4)/(height/2))
ix = np.clip(np.rint((x / width + .5) * 1023).astype(int), 0, 1023)
iy = np.clip(np.rint((.5 - y / height) * 1023).astype(int), 0, 1023)
tone = pix[iy, ix]; tone = (tone - tone.min()) / (tone.max() - tone.min())
z = base_z + (max_z - base_z) * tone
# Die Schrift ragt zusätzlich 0,23 mm über die hellsten Bildbereiche hinaus.
mask = np.asarray(text_mask)[iy, ix] > 127
z = np.where(mask, 2.55, z)
top = np.stack((x, y, z), axis=-1).reshape(-1, 3)
bot = top.copy(); bot[:, 2] = 0
v = np.concatenate((top, bot)).astype('<f4')
a = np.arange((n-1)*(n-1)).reshape(n-1,n-1)
a = (a // (n-1) * n + a % (n-1)).ravel()
b = a+1; c=a+n; d=c+1; off=n*n
faces = [np.stack((a,b,d),1), np.stack((a,d,c),1), np.stack((a+off,d+off,b+off),1), np.stack((a+off,c+off,d+off),1)]
edge = np.concatenate((np.arange(n), np.arange(1,n)*n+n-1, np.arange(n-2,-1,-1)+(n-1)*n, np.arange(n-2,0,-1)*n))
e2=np.roll(edge,-1)
faces += [np.stack((edge+off,e2+off,e2),1), np.stack((edge+off,e2,edge),1)]
faces=np.concatenate(faces)
tri=np.zeros(len(faces), dtype=np.dtype([('normal','<f4',3),('vertices','<f4',(3,3)),('attr','<u2')]))
tri['vertices']=v[faces]
with open(root/'patrizier2.stl','wb') as f:
    f.write(b'Patrizier II height relief'.ljust(80,b'\0')); f.write(struct.pack('<I',len(tri))); tri.tofile(f)
# Every undirected edge must occur twice for a closed manifold.
edges=np.concatenate((faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]])); edges.sort(axis=1)
_, counts=np.unique(edges,axis=0,return_counts=True)
print('Dimensions mm:',np.ptp(v,axis=0),'triangles:',len(faces),'nonmanifold edges:',np.count_nonzero(counts != 2))





# Vorhandenes Bambu-Projekt mit der aktuellen Geometrie aktualisieren.
# Palette, Schichtwechsel und die geprüften Paketverknüpfungen bleiben erhalten.
import zipfile
project = root / 'Patrizier2_Ahsoka_Farben.3mf'
if project.exists():
    from io import StringIO
    xml = StringIO()
    xml.write('<?xml version="1.0" encoding="UTF-8"?><model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" requiredextensions="p"><resources><object id="1" p:UUID="000a0000-81cb-4c03-9d28-80fed5dfa1dc" type="model"><mesh><vertices>')
    for px, py, pz in v:
        xml.write(f'<vertex x="{px:.7g}" y="{py:.7g}" z="{pz:.7g}"/>')
    xml.write('</vertices><triangles>')
    for a, b, c in faces:
        xml.write(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>')
    xml.write('</triangles></mesh></object></resources></model>')
    temporary = project.with_suffix('.tmp')
    with zipfile.ZipFile(project) as source, zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as target:
        for entry in source.infolist():
            data = xml.getvalue().encode('utf-8') if entry.filename == '3D/Objects/object_10.model' else source.read(entry.filename)
            target.writestr(entry, data)
    temporary.replace(project)
    print('3MF-Geometrie aktualisiert:', project.name)
