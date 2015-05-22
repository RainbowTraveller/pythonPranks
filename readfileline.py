#!/usr/bin/python
#Useful to read file line by line, can be redirected to another file or program as input
#The whole file can be read in one go, but it takes time to get output lines if file is huge

with open('error_log_union') as f:
    for line in f:
        print line
