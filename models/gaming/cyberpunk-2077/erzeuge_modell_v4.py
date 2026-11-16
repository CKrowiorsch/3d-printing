"""Erzeugt ein geschlossenes Sechseck-Höhenrelief aus motiv.png (mm)."""
from pathlib import Path
import struct
import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

root = Path(__file__).resolve().parent
width, height, max_z, base_z = 165.98218, 143.54388, 2.32, 0.80
n = 513
im = Image.open(root / 'motiv-v4.png').convert('L')

im = ImageOps.fit(im, (1024, 1024), method=Image.Resampling.LANCZOS)
im = im.filter(ImageFilter.GaussianBlur(0.35))
pix = np.asarray(im, dtype=np.float32) / 255
ys = np.linspace(-height/2, height/2, n)
us = np.linspace(-1, 1, n)
y, u = np.meshgrid(ys, us, indexing='ij')
x = u * (width/2 - abs(y) * (width/4)/(height/2))
ix = np.clip(np.rint((x / width + .5) * 1023).astype(int), 0, 1023)
iy = np.clip(np.rint((.5 - y / height) * 1023).astype(int), 0, 1023)
tone = pix[iy, ix]; tone = (tone - tone.min()) / (tone.max() - tone.min())
z = base_z + (max_z - base_z) * tone ** 1.65
# Die Schrift ragt zusätzlich 0,23 mm über die hellsten Bildbereiche hinaus.
mask = (iy >= 610) & (iy <= 695) & (ix >= 350) & (ix <= 675) & (pix[iy, ix] > 0.85)
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
with open(root/'cyberpunk-2077-v4.stl','wb') as f:
    f.write(b'Cyberpunk 2077 height relief'.ljust(80,b'\0')); f.write(struct.pack('<I',len(tri))); tri.tofile(f)
# Every undirected edge must occur twice for a closed manifold.
edges=np.concatenate((faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]])); edges.sort(axis=1)
_, counts=np.unique(edges,axis=0,return_counts=True)
print('Dimensions mm:',np.ptp(v,axis=0),'triangles:',len(faces),'nonmanifold edges:',np.count_nonzero(counts != 2))









# Kopie der Patrizier-Projektvorlage mit neuer Geometrie; das Original bleibt erhalten.
import zipfile, re
from io import StringIO
project = root / 'Cyberpunk_2077_Ahsoka_Farben_v4.3mf'
template = project  # Das vorhandene Projekt liefert Einstellungen und Farbwechsel.
xml = StringIO()
xml.write('<?xml version="1.0" encoding="UTF-8"?><model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" requiredextensions="p"><resources><object id="1" p:UUID="000a0000-81cb-4c03-9d28-80fed5dfa1dc" type="model"><mesh><vertices>')
for px, py, pz in v:
    xml.write(f'<vertex x="{px:.7g}" y="{py:.7g}" z="{pz:.7g}"/>')
xml.write('</vertices><triangles>')
for a, b, c in faces:
    xml.write(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>')
xml.write('</triangles></mesh></object></resources></model>')
with zipfile.ZipFile(template) as source:
    entries = [(entry, source.read(entry.filename)) for entry in source.infolist()]
with zipfile.ZipFile(project, 'w', zipfile.ZIP_DEFLATED) as target:
    for entry, original_data in entries:
        data = xml.getvalue().encode('utf-8') if entry.filename == '3D/Objects/object_10.model' else original_data
        if entry.filename == 'Metadata/model_settings.config':
            data = re.sub(rb'face_count="[0-9]+"', f'face_count="{len(faces)}"'.encode(), data)
            data = data.replace(b'Patrizier II', b'Cyberpunk 2077').replace(b'patrizier2.stl', b'cyberpunk-2077-v4.stl')
        target.writestr(entry, data)
print('3MF erstellt:', project.name)
# Vorschau der Bildfläche innerhalb der Modellkontur.
preview = im.convert('RGBA')
alpha = Image.new('L', preview.size, 0)
ImageDraw.Draw(alpha).polygon([(256,0),(768,0),(1023,512),(768,1023),(256,1023),(0,512)],fill=255)
preview.putalpha(alpha)
preview.save(root / 'vorschau-v4.png')

