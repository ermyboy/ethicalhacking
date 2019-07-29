#!usr/bin/env python
import requests
import hashlib
import re


url="http://docker.hackthebox.eu:36699/"

r=requests.session()
out=r.get(url)
print (out)
print ("***********************************************************")
out=re.search("<h3 align='center'>+.*?</h3>",out.text)
print (out)
print ("***********************************************************")
out=re.search(">.*<",out[0])
print (out[0])
print ("***********************************************************")
out=re.search("[^|'|>|<]...................",out[0])
print (out[0])
print ("***********************************************************")
out=hashlib.md5(out[0].encode('utf-8')).hexdigest()

print("sending md5 :-{}".format(out))

data={'hash': out}
out = r.post(url = url, data = data)

print(out.text)
