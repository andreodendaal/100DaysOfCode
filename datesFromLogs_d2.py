'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''

from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# for you to code:

def convert_to_datetime(line):
    '''Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    time_stamp = line.split(" ", 2)[1]
    strip_time = datetime.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S")

    return strip_time

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''

    times = []
    for line in loglines:
        if "Shutdown initiated" in line:
            time_stamp = line.split(" ", 2)[1]
            times.append(datetime.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S"))

    shutdown_timedelta = times[-1] - times[0]

    return shutdown_timedelta
