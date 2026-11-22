#!/usr/bin/env python3
"""Build the offline visual skill catalog from the checked-in manifest.json."""
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
records=json.loads((ROOT/'manifest.json').read_text('utf-8'))['skills']
CATS=['styles','palettes','layouts','social-media','meta']
def esc(x):return html.escape(str(x),quote=True)
def relative(p):return '../'+str(p)
REPO='https://github.com/dgylayse/anti-slop-design-skills'
def source(p):return REPO+'/blob/main/'+str(p)
blocks=[]
for r in records:
    image=relative(r['preview'])
    path=source(r['skill'])
    demo=relative(r['demo'])
    badge=r['category'].replace('-',' ').upper()
    blocks.append(f'''<article class="tile" data-group="{esc(r['category'])}" data-keywords="{esc((r['name']+' '+r['description']+' '+r['era']).lower())}" tabindex="-1">
       <a class="tile-image" href="{esc(demo)}" title="Open the source HTML visual demo for {esc(r['name'])}" target="_blank" rel="noopener"><img src="{esc(image)}" alt="Visual preview for {esc(r['name'])}" width="1280" height="800" loading="lazy"></a>
       <div class="tile-bottom"><div class="tile-topline"><span class="group">{esc(badge)}</span><span class="era">{esc(r['era'])}</span></div><div class="tile-title">{esc(r['name'].replace('-',' '))}</div><p>{esc(r['description'])}</p><div class="tile-actions"><a href="{esc(path)}">Read skill ↗</a><a href="{esc(demo)}" target="_blank" rel="noopener">HTML demo ↗</a></div></div>
    </article>''')
style_count=len([r for r in records if r['category']=='styles'])
page=f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#EDEAE2"><title>Anti-Slop Design Skills — Visual Catalog</title>
<style>
:root{{--bg:#EDEAE2;--ink:#1C2527;--red:#B84631;--muted:#576467;--panel:#F8F7F2;--edge:#C2C5BF}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;color:var(--ink);background:var(--bg);font-family:Arial,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:inherit}}a:focus-visible,button:focus-visible,input:focus-visible{{outline:3px solid var(--red);outline-offset:4px}}
.masthead{{border-bottom:1px solid var(--ink);background:#1B2527;color:#F6F4EA;padding:24px clamp(18px,5vw,88px) 25px}}
.mini{{display:flex;align-items:center;justify-content:space-between;gap:20px;font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase}}.mini a{{text-decoration:none;border:1px solid #879094;padding:11px 13px}}
.masthead h1{{font-size:clamp(3.6rem,8.4vw,9.2rem);letter-spacing:-.085em;line-height:.94;margin:65px 0 22px;font-weight:800;max-width:1300px}}.masthead h1 em{{font-style:normal;color:#D7AF77}}.lead{{font-size:clamp(16px,1.7vw,23px);line-height:1.5;max-width:940px;color:#C9D0CA}}
.stats{{margin-top:68px;display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid #728084}}.stats>div{{padding:22px 26px 3px;border-right:1px solid #728084}}.stats strong{{font-size:38px;display:block}}.stats span{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#AEB9BA}}
.controls{{padding:32px clamp(18px,5vw,88px);display:flex;gap:25px;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;border-bottom:1px solid var(--ink);position:sticky;top:0;z-index:9;background:rgba(237,234,226,.97);backdrop-filter:blur(8px)}}.controls label{{font-size:12px;letter-spacing:.13em;font-weight:700;display:block;text-transform:uppercase;margin-bottom:9px}}.search{{width:min(430px,80vw);border:0;border-bottom:2px solid var(--ink);background:transparent;padding:9px 2px;font-size:20px;color:var(--ink);border-radius:0}}.filters{{display:flex;gap:7px;flex-wrap:wrap}}button{{cursor:pointer;background:transparent;border:1px solid #818A88;border-radius:0;padding:11px 15px;font-size:12px;font-weight:700;letter-spacing:.035em}}button[aria-pressed=true]{{background:var(--ink);color:#fff;border-color:var(--ink)}}button:hover{{border-color:var(--red)}}.count{{font-weight:700;font-family:monospace;letter-spacing:.03em}}
main{{padding:42px clamp(18px,5vw,88px) 100px}}.banner{{margin-bottom:24px;display:flex;align-items:center;justify-content:space-between;gap:24px}}.banner h2{{font-size:clamp(26px,4vw,48px);letter-spacing:-.06em;margin:0}}.banner p{{max-width:450px;color:var(--muted);line-height:1.4}}.gallery{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}}.tile{{background:var(--panel);border:1px solid var(--edge);min-width:0;display:flex;flex-direction:column}}.tile-image{{overflow:hidden;display:block;background:#D3D5D0;aspect-ratio:1.6}}.tile-image img{{display:block;width:100%;height:100%;object-fit:cover;transition:transform .25s ease}}.tile:hover img{{transform:scale(1.027)}}.tile-bottom{{padding:23px;display:flex;flex-direction:column;flex:1}}.tile-topline{{display:flex;gap:12px;justify-content:space-between;flex-wrap:wrap;font-size:10px;letter-spacing:.1em;font-weight:700;text-transform:uppercase}}.group{{color:#A44630}}.era{{color:#65706B}}.tile-title{{text-transform:capitalize;font-size:26px;letter-spacing:-.045em;font-weight:700;margin:19px 0 8px}}.tile p{{color:#52605E;font-size:14px;line-height:1.56;margin:0;flex:1;min-height:66px}}.tile-actions{{border-top:1px solid var(--edge);padding-top:18px;display:flex;justify-content:space-between;gap:18px;margin-top:25px;font-size:13px;font-weight:700}}.tile-actions a{{text-decoration:underline;text-underline-offset:4px}}.tile-actions a:hover{{color:var(--red)}}.empty{{border:2px dashed #999;padding:44px;text-align:center;display:none}}footer{{background:#1B2527;padding:52px clamp(18px,5vw,88px);color:#EAE8DE;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}}footer a{{color:#E9BE79}}
@media(max-width:1100px){{.gallery{{grid-template-columns:repeat(2,minmax(0,1fr))}}.controls{{position:static}}}}@media(max-width:690px){{.gallery{{grid-template-columns:1fr}}.stats strong{{font-size:27px}}.stats>div{{padding:14px 10px 6px}}.masthead h1{{margin-top:38px}}.controls{{padding:22px 18px}}.banner{{flex-direction:column;align-items:start}}.tile p{{min-height:auto}}.mini{{font-size:10px}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}.tile-image img{{transition:none}}}}
</style></head><body>
<header class="masthead"><div class="mini"><span>AN OPEN LIBRARY OF ART DIRECTION</span><a href="{REPO}">GITHUB REPO ↗</a></div><h1>MORE<br>CHARACTER.<br><em>LESS SLOP.</em></h1><p class="lead">These are not prompt buzzwords. Explore {len(records)} practical Agent Skills through original, browser-rendered design studies. Choose by composition, not just color.</p><div class="stats"><div><strong>{len(records)}</strong><span>Agent Skills</span></div><div><strong>{style_count}</strong><span>Visual Styles</span></div><div><strong>100%</strong><span>With previews</span></div></div></header>
<div class="controls" role="region" aria-label="Catalog controls"><div><label for="search">Find a design language</label><input class="search" id="search" type="search" placeholder="Try hotel, travel, Swiss, magazine…" autocomplete="off"></div><div class="filters" role="group" aria-label="Filter by collection"><button type="button" aria-pressed="true" data-filter="all">All {len(records)}</button><button type="button" aria-pressed="false" data-filter="styles">{style_count} styles</button><button type="button" aria-pressed="false" data-filter="palettes">Palettes</button><button type="button" aria-pressed="false" data-filter="layouts">Layouts</button><button type="button" aria-pressed="false" data-filter="social-media">Social</button><button type="button" aria-pressed="false" data-filter="meta">Director</button></div><div class="count" id="count" aria-live="polite">{len(records)} shown</div></div>
<main><div class="banner"><h2>VISUAL INDEX / 01—{len(records)}</h2><p>Each card opens a real HTML composition. Its paired SKILL.md describes how to translate the visual language into an accessible, responsive interface.</p></div><section class="gallery" id="gallery" aria-label="Design skill previews">{''.join(blocks)}</section><div class="empty" id="empty">No matching styles. Try a different term or category.</div></main>
<footer><strong>GOOD DESIGN IS A DECISION.</strong><span>Locally rendered previews • No external fonts or image services • MIT · <a href="{REPO}/blob/main/README.tr.md">Türkçe rehber</a></span></footer>
<script>
const tiles=[...document.querySelectorAll('.tile')],filters=[...document.querySelectorAll('[data-filter]')];
const input=document.getElementById('search');let active='all';
function apply(){{const q=input.value.toLocaleLowerCase('en').trim();let count=0;for(const tile of tiles){{const match=(active==='all'||tile.dataset.group===active)&&tile.dataset.keywords.includes(q);tile.hidden=!match;tile.style.display=match?'flex':'none';if(match)count++;}}document.getElementById('count').textContent=count+' shown';document.getElementById('empty').style.display=count?'none':'block';}}
input.addEventListener('input',apply);for(const b of filters)b.addEventListener('click',()=>{{active=b.dataset.filter;filters.forEach(f=>f.setAttribute('aria-pressed',String(f===b)));apply();}});
</script></body></html>'''
(ROOT/'gallery/index.html').write_text(page,encoding='utf-8')
(ROOT/'index.html').write_text('<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=gallery/index.html"><title>Visual Design Skills</title></head><body><p><a href="gallery/index.html">Open the design gallery</a></p></body></html>','utf-8')
print('Built offline gallery:',len(records),'cards')
