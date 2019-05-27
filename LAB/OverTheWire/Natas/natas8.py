#!usr/bin/env python

import re
import requests

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

risultato = session.post(url, data = {"secret" : "oubWYf2kBq", "submit" : "submit" }, auth = (username, password))
contenuto = risultato.text

#print (contenuto)
print (re.findall('natas9 is (.*)', contenuto) [0])