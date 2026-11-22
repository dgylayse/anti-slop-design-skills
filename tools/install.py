#!/usr/bin/env python3
"""Copy selected self-contained Agent Skills into a project's skills directory."""
from pathlib import Path
import argparse,json,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))['skills']
INDEX={s['name']:s for s in DATA}
def main():
 p=argparse.ArgumentParser(description='Install Design Skills into a local agent skills directory.')
 p.add_argument('--list',action='store_true',help='List skills and exit')
 p.add_argument('--skill',action='append',default=[],help='Skill slug; repeat to install multiple')
 p.add_argument('--category',choices=['styles','palettes','layouts','social-media','meta'],help='Install all skills within one category')
 p.add_argument('--all',action='store_true',help='Install all available skills')
 p.add_argument('--target',type=Path,help='Target directory such as ./my-project/.agents/skills')
 p.add_argument('--force',action='store_true',help='Replace previously installed folders')
 p.add_argument('--dry-run',action='store_true',help='Print planned copies only')
 args=p.parse_args()
 if args.list:
  for s in DATA:print(f"{s['category']:12} {s['name']}")
  return 0
 selected=set(args.skill)
 if args.category:selected.update(s['name'] for s in DATA if s['category']==args.category)
 if args.all:selected=set(INDEX)
 unknown=sorted(selected-set(INDEX))
 if unknown:p.error('Unknown skill(s): '+', '.join(unknown))
 if not selected:p.error('Pick --skill, --category or --all, or use --list')
 if not args.target:p.error('--target is required when installing')
 target=args.target.expanduser().resolve()
 for name in sorted(selected):
  entry=INDEX[name]
  src=ROOT/entry['category']/name
  dest=target/name
  if dest.exists() and not args.force:
   print('SKIP (exists, add --force):',dest)
   continue
  if args.dry_run:print('COPY:',src,'->',dest);continue
  dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists():shutil.rmtree(dest)
  shutil.copytree(src,dest)
  print('INSTALLED:',dest)
 return 0
if __name__=='__main__':sys.exit(main())
