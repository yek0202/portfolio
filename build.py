#!/usr/bin/env python3
"""把头像 base64 注入到 index.html"""
import json, re

with open('/Users/kun/Desktop/简历/PMC简历.json') as f:
    data = json.load(f)
photo = data['basic']['photo']

with open('/Users/kun/Desktop/简历/portfolio/index.html', 'r') as f:
    html = f.read()

html = html.replace('__AVATAR_BASE64__', photo)

with open('/Users/kun/Desktop/简历/portfolio/index.html', 'w') as f:
    f.write(html)
print('Done, size:', len(html))
