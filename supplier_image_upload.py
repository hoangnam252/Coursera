#!/usr/bin/python3

import os
import requests

url = "http://34.123.95.35/upload/"
path = "supplier-data/images/"
for file in os.listdir(path):
        if '.jpeg' in file and '.' not in file[0]:
                with open(path+file, 'rb') as f:
                        r = requests.post(url, files={'file':f})