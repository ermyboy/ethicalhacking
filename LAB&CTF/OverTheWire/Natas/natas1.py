#!usr/bin/env python

import re
import requests

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % username

risultato = requests.get(url, auth = (username, password))
contenuto = risultato.text

#print (contenuto)
print (re.findall('<!--The password for natas2 is (.*) -->', contenuto) [0])
