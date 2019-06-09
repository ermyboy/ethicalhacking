#!usr/bin/env python

import re
import requests

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

risultato = requests.get(url, auth = (username, password))
contenuto = risultato.text

#print (contenuto)
print (re.findall('natas4:(.*)', contenuto) [0])