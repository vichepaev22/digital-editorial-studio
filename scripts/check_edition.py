#!/usr/bin/env python3
"""Static HTML smoke check; not a WCAG or fact-verification tool."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit, unquote
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.anchors=[]; self.assets=[]; self.missing_alt=[]; self.h1=0; self.lang=None; self.main=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='main': self.main+=1
        if tag=='h1': self.h1+=1
        if tag=='a' and a.get('href','').startswith('#'): self.anchors.append(a['href'][1:])
        if tag=='img' and 'alt' not in a: self.missing_alt.append(a.get('src','?'))
        if tag in ('img','script') and a.get('src'): self.assets.append(a['src'])
        if tag=='link' and 'stylesheet' in a.get('rel','').split() and a.get('href'): self.assets.append(a['href'])
def check(path):
    p=Page(); p.feed(path.read_text(encoding='utf-8')); problems=[]
    if not p.lang: problems.append('Missing html lang')
    if p.h1!=1: problems.append(f'Expected one h1; found {p.h1}')
    if p.main!=1: problems.append(f'Expected one main; found {p.main}')
    problems += ['Duplicate id: '+x for x,n in Counter(p.ids).items() if n>1]
    problems += ['Broken static fragment: '+x for x in p.anchors if x and unquote(x) not in p.ids]
    problems += ['Image missing alt: '+x for x in p.missing_alt]
    for asset in p.assets:
        u=urlsplit(asset)
        if u.scheme or u.netloc or not u.path or u.path.startswith('/'): continue
        if not (path.parent/unquote(u.path)).is_file(): problems.append('Missing local asset: '+asset)
    return problems
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('html',type=Path); args=parser.parse_args()
    errors=check(args.html)
    for e in errors: print(e)
    print(f'Static smoke check: {len(errors)} issue(s). Browser, evidence and accessibility tests still required.')
    raise SystemExit(bool(errors))
