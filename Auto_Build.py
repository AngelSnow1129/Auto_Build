#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import re
import sys
import requests
import json

sI=os.environ.get('sI')
bI=os.environ.get('bI')
bN=os.environ.get('bN')
aT=os.environ.get('aT')
text=os.environ.get('text')

url=text.format(scriptID=sI)
data='''{{"robots": [{{ "_id": "{0}", "name": "{1}"}}]}}'''.format(bI,bN)
headers='''{{"Authorization":"{0}","Content-Type":"application/json"}}'''.format(aT)


result = requests.post(url, data=json.dumps(data) , headers=headers)
# print(result)