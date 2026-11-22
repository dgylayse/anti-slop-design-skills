#!/usr/bin/env python3
"""Regenerate each preview PNG from the HTML in the same skill directory.

Requires: pip install playwright; python -m playwright install chromium
Example: python tools/render_previews.py --only styles/art-nouveau-atelier
"""
import argparse,asyncio
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def render(paths,browser_path):
 async with async_playwright() as p:
  kw={'executable_path':browser_path} if browser_path else {}
  browser=await p.chromium.launch(args=['--no-sandbox','--disable-gpu'],**kw)
  page=await browser.new_page(viewport={'width':1280,'height':800},device_scale_factor=1)
  errors=[]
  for path in paths:
   try:
    await page.set_content(path.read_text('utf-8'),wait_until='load')
    await page.screenshot(path=str(path.with_name('preview.png')),animations='disabled')
    print('CREATED',path.with_name('preview.png').relative_to(ROOT))
   except Exception as e:
    errors.append((str(path),str(e)))
  await browser.close()
  for f,msg in errors:print('ERROR:',f,msg)
  return bool(errors)
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--only',help='Skill subpath, e.g. styles/swiss-editorial')
 parser.add_argument('--chromium',help='Optional absolute path to system Chromium binary')
 args=parser.parse_args()
 if args.only:
  item=(ROOT/args.only).resolve()
  if ROOT not in item.parents:parser.error('Path must be within repository')
  paths=[item/'demo.html']
 else:paths=sorted(ROOT.glob('**/demo.html'))
 if not all(p.exists() for p in paths):parser.error('demo.html not found')
 raise SystemExit(int(asyncio.run(render(paths,args.chromium))))
if __name__=='__main__':main()
