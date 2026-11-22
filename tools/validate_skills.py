#!/usr/bin/env python3
"""CI-friendly checks for frontmatter, asset integrity and contrast of declared canonical tokens."""
import json,re,hashlib,sys
from pathlib import Path
import yaml
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'name','description','license','metadata','compatibility','allowed-tools'}
CATEGORIES={'meta','styles','palettes','layouts','social-media'}
REQUIRED_TOKENS=('bg','surface','ink','muted','accent','border')
errors=[]
def err(context,msg):errors.append(f'{context}: {msg}')
def light(h):
 v=[int(h[i:i+2],16)/255 for i in (1,3,5)]
 c=[t/12.92 if t<=0.04045 else ((t+0.055)/1.055)**2.4 for t in v]
 return c[0]*0.2126+c[1]*0.7152+c[2]*0.0722
def ratio(a,b):
 x,y=sorted((light(a),light(b)));return (y+0.05)/(x+0.05)
manifest=json.loads((ROOT/'manifest.json').read_text('utf-8'))
skills=manifest.get('skills',[]);names=set();images=set();previews={}
for s in skills:
 ctx=f'{s.get("category")}/{s.get("name")}'
 if s.get('category') not in CATEGORIES:err(ctx,'Unknown category')
 if s['name'] in names:err(ctx,'Duplicate skill name')
 names.add(s['name'])
 folder=ROOT/s['category']/s['name']
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',s['name']):err(ctx,'Invalid folder/name')
 for key in ('skill','preview','demo'):
  f=ROOT/s[key]
  if not f.is_file():err(ctx,'Missing '+key+' file: '+str(f))
 try:
  raw=(folder/'SKILL.md').read_text('utf-8')
  if not raw.startswith('---\n'):raise ValueError('Missing frontmatter fence')
  match=re.match(r'^---\s*\n(.*?)\n---\s*\n',raw,re.S)
  if not match:raise ValueError('Malformed YAML fences')
  data=yaml.safe_load(match.group(1))
  if not isinstance(data,dict):raise ValueError('Expected frontmatter mapping')
  if set(data)-ALLOWED:err(ctx,'Non-standard frontmatter fields: '+str(set(data)-ALLOWED))
  if data.get('name')!=s['name']:err(ctx,'Name mismatch')
  desc=data.get('description','')
  if not isinstance(desc,str) or not 20<=len(desc)<=1024:err(ctx,'Description length out of bounds')
  meta=data.get('metadata',{})
  if not isinstance(meta,dict) or any(not isinstance(v,str) for v in meta.values()):err(ctx,'metadata must be string mapping')
  if meta.get('category')!=s['category']:err(ctx,'Metadata category mismatch')
  if meta.get('preview')!='preview.png':err(ctx,'Metadata preview path must be preview.png')
  if s['category'] in ('styles','palettes'):
   vals={}
   for n in REQUIRED_TOKENS:
    matches=re.findall(r'--color-'+n+r':\s*(#[A-Fa-f0-9]{6})\s*;',raw)
    if not matches:err(ctx,'Missing canonical color token '+n)
    else:vals[n]=matches[-1]
   if len(vals)==6:
    for which in ('ink','muted'):
     r=ratio(vals[which],vals['bg'])
     if r<4.5:err(ctx,f'{which} vs bg contrast {r:.2f}:1 (<4.5:1)')
  if len(raw)<600:err(ctx,'Skill too short for useful guidance')
 except Exception as e:err(ctx,f'SKILL.md parse failure: {e}')
 try:
  path=folder/'preview.png'
  with Image.open(path) as im:
   if im.format!='PNG':err(ctx,'Preview is not a PNG')
   if im.size!=(1280,800):err(ctx,'Preview must be 1280x800')
   pixels=im.convert('RGB').resize((25,15)).tobytes()
   if len({pixels[i:i+3] for i in range(0,len(pixels),3)})<12:err(ctx,'Preview looks mostly blank')
  digest=hashlib.sha256(path.read_bytes()).hexdigest()
  if digest in images:err(ctx,'Duplicate preview bytes')
  images.add(digest)
 except Exception as e:err(ctx,f'Invalid preview: {e}')
 if not (folder/'demo.html').read_text('utf-8').lstrip().lower().startswith('<!doctype html>'):
  err(ctx,'demo.html missing doctype')
actual={p.parent.name for p in ROOT.glob('**/SKILL.md')}
if len(actual)!=len(skills):err('manifest',f'Found {len(actual)} named directories but {len(skills)} manifest entries')
if len(skills)!=manifest.get('skill_count'):err('manifest','skill_count mismatch')
gallery=(ROOT/'gallery/index.html')
if not gallery.is_file():err('gallery','Missing index.html')
else:
 source=gallery.read_text('utf-8')
 for s in skills:
  if s['preview'] not in source:err('gallery','Missing preview '+s['preview'])
print(f'Validated {len(skills)} skill manifests and {len(images)} unique preview images.')
if errors:
 print('FAILED',len(errors),'check(s):')
 for item in errors:print(' -',item)
 sys.exit(1)
print('PASS: metadata, semantic contrast, previews and gallery catalog.')
