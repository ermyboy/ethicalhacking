#!usr/bin/env python

import re
import requests

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

risultato = session.get(url, auth = (username, password))
contenuto = risultato.text

print (contenuto)
#print (re.findall('natas7 is (.*)', contenuto) [0])