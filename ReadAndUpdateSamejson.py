#!/usr/bin/python

import json
import smtplib
import sys
from datetime import datetime
from pprint import pprint

with open('lastReportingTime.json') as report_time_file:
    try:
        report_time_data  = json.load(report_time_file)
    except Exception as exp:
        pprint(str(exp))

reporting = report_time_data['reporting']
#reporting_times = { topology_time_pair['topology'] : topology_time_pair for topology_time_pair in reporting}
#print(json.dumps(reporting_times, indent = 4))

with open('lastReportingTime.json', 'w+') as report_time_file:
    for eachTopology in reporting:
        eachTopology["reportingGapHrs"] = 24
    #report_time_file.write(json.dumps(reporting))
    #report_time_file.write(pprint(reporting))
    json.dump(report_time_data, report_time_file, indent = 8)

