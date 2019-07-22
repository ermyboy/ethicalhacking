#!usr/bin/env python

import re
import requests

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org' % username

risultato = requests.get(url, auth = (username, password))
contenuto = risultato.text


print (re.findall('<!--The password for natas1 is (.*) -->', contenuto) [0])
