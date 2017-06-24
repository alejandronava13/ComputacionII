#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
pp=[]
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in s:
  if i in abc:
    y=abc.index(i)
    if (y+k)>25:
      r=(y+k)%26
      r=abc[r]
      pp.append(r)
    else:
      r=abc[y+k]
      pp.append(r)
  else:
    r=s[s.index(i)]
    pp.append(r)
#print pp
cadena="".join(pp)
print cadena