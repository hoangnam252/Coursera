#!/usr/bin/env python3

import re
import csv
import operator
import sys

per_user = {}
error = {}

logfile = 'syslog.log'
error_file = 'error_message.csv'
user_file = 'user_statistic.csv'
    
with open(logfile) as f:    
    for line in f:
        pattern = r"ticky: ([LOG|ERROR]) ([\w' ]*) [\[[#0-9]\]?]? \([.*]\)"
        result = re.search(pattern, line)
        
        if result.group(2) not in error.key():
            error[result.group(2)] = 0
            
        error[result.group(2)] += 1
        
        if result.group(3) not in per_user.key():
            per_user[result.group(3)] = {}
            per_user[result.group(3)]["INFO"] = 0
            per_user[result.group(3)]["ERROR"] = 0
            
        if result.group(1) == "INFO":
            per_user[result.group(3)]["INFO"] += 1
        elif result.group(1) == "ERROR":
            per_user[result.group(3)]["ERROR"] += 1
            
    error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    per_user = sorted(per_user.item())
    
error.insert(0, ("Error", "Count"))

with open(error_file, "w") as err:
    for count in error:
        a,b = count
        err.write(str(a)+','+str(b)+'\n')