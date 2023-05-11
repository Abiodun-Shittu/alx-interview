#!/usr/bin/python3
"""A script for parsing HTTP request logs."""
import re
from typing import Dict


LOG_PATTERN = (
    r'\s*(?P<ip>\S+)\s*'
    r'\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]'
    r'\s*"(?P<request>[^"]*)"\s*'
    r'\s*(?P<status_code>\S+)'
    r'\s*(?P<file_size>\d+)'
)


def extract_log_info(log_line: str) -> Dict[str, int]:
    """Extracts sections of a line of an HTTP request log."""
    info = {'status_code': 0, 'file_size': 0}
    match = re.fullmatch(LOG_PATTERN, log_line)
    if match:
        info['status_code'] = int(match.group('status_code'))
        info['file_size'] = int(match.group('file_size'))
    return info


def print_statistics(total_file_size: int, status_codes_stats: Dict[str, int]) -> None:
    """Prints the accumulated statistics of the HTTP request log."""
    print(f'File size: {total_file_size}', flush=True)
    for status_code, count in sorted(status_codes_stats.items()):
        if count > 0:
            print(f'{status_code}: {count}', flush=True)


def update_metrics(log_line: str, total_file_size: int, status_codes_stats: Dict[str, int]) -> int:
    """Updates the metrics from a given HTTP request log.

    Args:
        log_line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary containing the
        count of each status code.

    Returns:
        int: The new total file size.
    """
    log_info = extract_log_info(log_line)
    status_code = str(log_info.get('status_code', '0'))
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + log_info['file_size']


def run() -> None:
    """Starts the log parser."""
    line_num = 0
    total_file_size = 0
    status_codes_stats = dict.fromkeys(('200', '301', '400', '401', '403', '404', '405', '500'), 0)
    try:
        while True:
            log_line = input()
            total_file_size = update_metrics(
                log_line, total_file_size, status_codes_stats
                )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
