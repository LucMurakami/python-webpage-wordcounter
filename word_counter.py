#!/usr/local/bin/python3.7
import requests
from bs4 import BeautifulSoup, Comment
import sys
r = requests.get(str(sys.argv[1]))
s = BeautifulSoup(r.content, 'html.parser')
for sc in s(['script', 'style']):
    sc.extract()
for cm in s.find_all(string=lambda t: isinstance(t, Comment)):
    cm.extract()
txt = s.find_all(text=True)
out = []
for t in txt:
    out += t.replace('\n', '').replace('\r', '').split(' ')
out = [t for t in out if t]
print(len(out))