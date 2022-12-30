#! /usr/bin/env python3

import os
import requests

dir = '/data/feedback/'

keys = ["title", "name", "date", "feedback"]
for filename in os.listdir(dir):
        dict = {}
        print(filename)

        with open(dir+filename) as f:
                x = 0
                for line in f:
                        dict[keys[x]] = line.strip()
                        x += 1
        print(dict)
        response = requests.post("http://35.222.160.66/feedback/", json=dict);
print(response.request.body)
print(response.status_code)