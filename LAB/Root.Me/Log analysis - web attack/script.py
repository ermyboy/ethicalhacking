#!/usr/bin/env python
# -*- coding:Utf-8 -*-

#==========================================================#
# [+] Title:   Logs analysis - web attack                  #
# [+] Author:  Baptiste M. (Creased)                       #
# [+] Website: bmoine.fr                                   #
# [+] Email:   contact@bmoine.fr                           #
# [+] Twitter: @Creased_                                   #
#==========================================================#

import urllib, base64, re, time
from datetime import datetime, timedelta

tstamp = None
url = 'http://challenge01.root-me.org/forensic/ch13/ch13.txt'
file = urllib.urlopen(http://challenge01.root-me.org/forensic/ch13/ch13.txt)
data = []
i = 0

# Split log lines to retrieve:
#  - delta since the last request,
#  - request (only for debug purpose)
for line in file:
    regex = '[(\d\.?)]+ - - \[(.*?)\] ".+order=([^ ]+).+" \d+ \d+ ".*?" ".*?"'
    res   = re.match(regex, line).groups()
    req   = base64.b64decode(urllib.unquote(res[1]))
    t     = datetime.strptime(res[0][1:res[0].find(' ')], "%d/%b/%Y:%H:%M:%S")

    if tstamp is not None:
        start = tstamp
    else:
        start = t

    tstamp = t

    req = req.replace("char(48)", "'0'")
    req = req.replace("char(49)", "'1'")

    data += [{'delta': '0:00:00', 'request': req}]

    if i > 0:
        data[i-1]['delta'] = tstamp - start

    i+=1

i = 1
binarray = []
binstr = '0b'

# Get flag bytes from deltas
for req in data:
    delta = int(str(req['delta']).split(':')[-1])
    if i % 4 == 0:  # LSB
        if delta == 2:
            binstr += '0'
        elif delta == 4:
            binstr += '1'

        binarray += [int(binstr, 2)]
        binstr = '0b'
    else:
        if delta == 0:
            binstr += '00'
        elif delta == 2:
            binstr += '01'
        elif delta == 4:
            binstr += '10'
        elif delta == 6:
            binstr += '11'

    i+=1

# Print flag
flag = ''
for char in binarray:
    flag += chr(char)

print('Flag: {flag}'.format(flag=flag))