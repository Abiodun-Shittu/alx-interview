#!/usr/bin/python3
'''
Write a script that reads stdin line by line and computes metrics:
'''

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            ip, _, _, path, status, size = line.split(' ')
            if path != '/projects/260':
                continue
            status = int(status)
            if status not in status_codes:
                continue
            size = int(size)
            total_size += size
            status_counts[status] += 1
        except:
            continue
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print(f'{code}: {count}')
            print('---')
except KeyboardInterrupt:
    print(f'Total file size: {total_size}')
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f'{code}: {count}')
