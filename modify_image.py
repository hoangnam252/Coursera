#!/usr/bin/python3

from PIL import Image
import os

in_dir = 'images/'
out_dir = '/opt/icons'

for filename in os.listdir(in_dir):
	if filename != ".DS_Store":
        im = Image.open(os.path.join(in_dir, filename))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(out_dir,filename+".jpeg"))