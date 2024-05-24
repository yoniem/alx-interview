#!/usr/bin/python3
import sys
import re
import signal

# Dictionary to hold the count of each status code
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
line_count = 0

def print_stats():
    """ Print the accumulated metrics. """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """ Handle keyboard interruption (CTRL + C). """
    print_stats()
    sys.exit(0)

# Set the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>.*?)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'
)

for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        size = int(match.group("size"))
        status = match.group("status")
        
        total_size += size
        if status in status_codes:
            status_codes[status] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

print_stats()
