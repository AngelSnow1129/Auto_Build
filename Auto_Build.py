#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import re
import sys
import requests
import json
import post

sI=os.getenv(secrets.sI)
bI=os.getenv(secrets.bI)
bn=os.getenv(secrets.bN)
aT=os.getenv(secrets.aT)


text=os.getenv(text)
url=text.format(scriptID=sI)
data={"robots": [{ "_id": "{botId}", "name": "{botName}" }]}.format(bI=bI,botName=bN)
headers={"Authorization":"{account_token}","Content-Type":"application/json"}.format(account_token=aT)


result = requests.post(url, data=json.dumps(data) , headers=headers)
# print(result)
