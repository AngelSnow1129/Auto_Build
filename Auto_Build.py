#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import re
import sys
import requests
import json
import ast


sI=os.environ.get('sI')
bI=os.environ.get('bI')
bN=os.environ.get('bN')
aT=os.environ.get('aT')
text=os.environ.get('text')



def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())


# url=url.isprintable()

# print(url)
url=text.format(scriptID=sI)
url = remove_upprintable_chars(url)
data='''{{"robots": [{{ "_id": "{0}", "name": "{1}"}}]}}'''.format(bI,bN)
headers_str='''{{"Authorization":"{0}","Content-Type":"application/json"}}'''.format(aT)

headers=ast.literal_eval(headers_str)

result = requests.post(url, data=json.dumps(data) , headers=headers)
# print(result)
