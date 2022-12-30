#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as f:
        for line in f.readlines():
                old_name = line.strip()
                new_name = old_name.replace("jane", "jdoe")
                subprocess.run(["mv",old_name, new_name])
