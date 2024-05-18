#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0

def print_stats():
    """ Print the current statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """ Handle the keyboard interruption signal """
    print_stats()
    sys.exit(0)

# Attach signal handler to SIGINT
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        
        # Validate the line format
        if len(parts) != 9:
            continue
        
        # Extract status code and file size
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue

        # Update total file size
        total_size += file_size

        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print stats after every 10 lines
        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print the final stats at the end of input
print_stats()
