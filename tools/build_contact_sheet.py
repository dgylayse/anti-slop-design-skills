#!/usr/bin/env python3
"""Rebuild the all-style contact sheet after adding previews (requires Pillow)."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,math
ROOT=Path(__file__).resolve().parents[1]
styles=[s for s in json.loads((ROOT/'manifest.json').read_text('utf-8'))['skills'] if s['category']=='styles']
w,h,cols=340,240,4
sheet=Image.new('RGB',(w*cols,h*math.ceil(len(styles)/cols)),'#F3F0E9')
try:font=ImageFont.truetype('DejaVuSans-Bold.ttf',15)
except:font=ImageFont.load_default()
for i,s in enumerate(styles):
 path=ROOT/s['preview']
 im=Image.open(path).convert('RGB').resize((w-16,208),Image.Resampling.LANCZOS)
 x=i%cols*w+8;y=i//cols*h+8
 sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text((x,y+213),s['name'],font=font,fill='#1B1B1B')
output=ROOT/'gallery/contact-sheet.jpg'
sheet.save(output,quality=86,optimize=True)
print('CREATED',output.relative_to(ROOT),sheet.size)
