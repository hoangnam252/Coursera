#! /usr/bin/env python3

import os
import requests

text_dir = 'supplier-data/descriptions/'
txt_file = [f for f in os.listdir(text_dir) if f.endswith('.txt')]
image_dir = 'supplier-data/images/'
image_file = [f for f in os.listdir(image_dir) if f.endswith('.jpeg')]

list_data=[]

for text in os.listdir(text_dir):
        with open(text_dir+text) as file:
                data = {"name":file.readline().rstrip("\n"),
                        "weight":int(file.readline().rstrip("\n").split(' ')[0]),
                        "description":file.readline().rstrip("\n")}

                for image in image_file:
                        if image.split('.')[0] in text.split('.')[0]:
                                data["image_name"] = image

                list_data.append(data)

for item in list_data:
        response = requests.post('http://34.29.47.57/fruits', json=item)
        if response.ok:
                print('Upload ok!')
        else:
                print(f'error: {response.status_code}')