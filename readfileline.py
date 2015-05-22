#!/usr/bin/python
#Useful to read file line by line, can be redirected to another file or program as input

with open('error_log_union') as f:
    for line in f:
        print line
