from pathlib import Path
from PIL import Image, ImageOps
p = Path(__file__).resolve().parent
im = ImageOps.fit(Image.open(p/'ausgangsmotiv-v6.png').convert('L'), (1024, 1024), method=Image.Resampling.LANCZOS)
im = im.resize((850, 960), Image.Resampling.LANCZOS)
canvas = Image.new('L',(1024,1024),255)
canvas.paste(im, ((1024-im.width)//2,(1024-im.height)//2))
canvas.save(p/'motiv-v6.png')
