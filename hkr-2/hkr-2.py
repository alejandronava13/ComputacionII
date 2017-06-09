#!/bin/python
abc="abcdefghijklmnopqrstuvwxyz"
abcmi=list(abc.lower())
abcma=list(abc.upper())
s=list(raw_input())
conter=1
for i in range(len(s)):
  if (s[len(s)-(i+1)] in abcma) is True:
    conter+=1
print conter
