https://docs.python.org/3/library/email.parser.html
https://stackoverflow.com/questions/8424317/extract-just-email-headers-in-python


f = open(kwargs['opt_emailfile'])
msg = email.message_from_file(f)
f.close()

parser = email.parser.HeaderParser()
headers = parser.parsestr(msg.as_string())

for h in headers.items():
    print h