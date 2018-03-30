"""Parse log entries for datetimes and calculate the time
   between two shutdown initializations"""
from datetime import datetime
import os
import urllib.request

# prep

tempfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', tempfile)

# code


def read_file():
    """Read in tempfile return list of lines"""
    data = []
    with open(tempfile) as fin:
        for line in fin.readlines():
            data.append(line.strip())
    return data


def convert_to_datetime(line):
    """Given a line extract timestamp and convert to datetime"""
    data = line.split(' ')
    line_datetime = data[1].split('T')
    line_date = [int(x) for x in line_datetime[0].split('-')]
    line_time = [int(x) for x in line_datetime[1].split(':')]
    return datetime(line_date[0], line_date[1], line_date[2], line_time[0], line_time[1], line_time[2])



def time_between_shutdowns(lines):
    """Extract shutdown init events and calculate timedelta between
       first and last one"""
    first = 0
    last = 0
    for line in lines:
        if 'Shutdown initiated' in line:
            if first == 0:
                first = convert_to_datetime(line)
            else:
                last = convert_to_datetime(line)
    return last - first

my_lines = read_file()
print(*my_lines, sep="\n")
print(convert_to_datetime(my_lines[0]))
print(time_between_shutdowns(my_lines))