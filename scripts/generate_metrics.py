#!/usr/bin/env python3
"""Public GitHub profile statistics, output a local self-hosted SVG. No dependencies."""
import json
import os
import pathlib
import urllib.request
from datetime import datetime, timezone
from html import escape

USER = 'kernelkill'
OUT = pathlib.Path('assets/github-metrics.svg')
TOKEN = os.environ.get('GH_TOKEN', '')
HEADERS = {'User-Agent': 'kernelkill-profile-metrics', 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
if TOKEN:
    HEADERS['Authorization'] = f'Bearer {TOKEN}'

def fetch(path):
    req = urllib.request.Request('https://api.github.com' + path, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=25) as response:
        return json.load(response)

profile = fetch(f'/users/{USER}')
repos = []
for page in range(1, 6):
    batch = fetch(f'/users/{USER}/repos?per_page=100&page={page}&type=owner')
    repos.extend(batch)
    if len(batch) < 100:
        break
public = [repo for repo in repos if not repo.get('private') and not repo.get('fork')]
stars = sum(r.get('stargazers_count', 0) for r in public)
forks = sum(r.get('forks_count', 0) for r in public)
values = [('PUBLIC REPOS', profile.get('public_repos', 0)), ('TOTAL STARS', stars), ('TOTAL FORKS', forks), ('FOLLOWERS', profile.get('followers', 0))]
date = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 214" role="img" aria-label="Public GitHub statistics">', '<rect x="1" y="1" width="998" height="212" rx="14" fill="#061318" stroke="#00d7a5" stroke-width="2"/>', '<rect x="1" y="1" width="998" height="42" rx="14" fill="#0c2329"/>', '<text x="25" y="28" fill="#00ffab" font-size="17" font-family="monospace">root@kernelkill:~# ./github_telemetry.sh</text>']
for i, (label, num) in enumerate(values):
    x = 125 + i*250
    parts += [f'<text x="{x}" y="118" fill="#e7fff8" font-size="38" font-family="monospace" font-weight="bold" text-anchor="middle">{int(num):,}</text>', f'<text x="{x}" y="148" fill="#00ffab" font-size="14" font-family="monospace" text-anchor="middle">{escape(label)}</text>']
    if i < 3:
        parts.append(f'<path d="M{x+125} 65 V157" stroke="#1a4d51"/>')
parts.append(f'<text x="25" y="192" fill="#789b9b" font-size="12" font-family="monospace">public data • last update: {date} • stars/forks exclude forks</text>')
parts.append('</svg>')
OUT.parent.mkdir(exist_ok=True, parents=True)
OUT.write_text(''.join(parts), encoding='utf-8')
print(f'Wrote {OUT}')
