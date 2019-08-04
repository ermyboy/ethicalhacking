#!usr/bin/env python

import re
import requests
import urllib
import base64
import binascii

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

cookies = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}
risultato = session.get(url, auth = (username, password), cookies = cookies )

#passo = binascii.b2a_hex(base64.b64decode(urllib.parse.unquote(session.cookies['data'])))

#print(passo)
contenuto = risultato.text

#print (contenuto)
#print (re.findall('<pre>\n(.*)\n', contenuto) [0])
print (re.findall('natas12 is (.*)<br>', contenuto) [0])