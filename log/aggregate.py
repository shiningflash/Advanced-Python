from datetime import datetime
from typing import Optional, Dict, Tuple
from collections import defaultdict


class LogAggregator:
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path

    def parse_log_line(self, log: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        try:
            timestamp = log[:19]
            level, message = log[20:].split(' ', 1)
            return timestamp, level, message.strip()
        except ValueError:
            return None, None, None

    def aggregate_logs(self) -> Tuple[Dict[str, int], Optional[datetime], Optional[datetime]]:
        log_counts_by_level = defaultdict(int)
        earliest_log_time = None
        latest_log_time = None
        
        with open(self.log_file_path, 'r') as logs:
            for log in logs:
                timestamp, level, _ = self.parse_log_line(log)
                if not timestamp or not level:
                    continue  # skip invalid log
                
                log_counts_by_level[level] += 1
                
                if not earliest_log_time or timestamp < earliest_log_time:
                    earliest_log_time = timestamp
                if not latest_log_time or timestamp > latest_log_time:
                    latest_log_time = timestamp
        
        return log_counts_by_level, earliest_log_time, latest_log_time

    def display_aggregated_data(self, log_counts: Dict[str, int], earliest: Optional[datetime], latest: Optional[datetime]) -> None:
        print('Aggregated Log Data:')
        for level, count in log_counts.items():
            print(f'{level}: {count} entries')
        
        most_frequent_log = max(log_counts.items(), key=lambda log:log[1])[0]
        print(f'\nMost frequent log level: {most_frequent_log}\n')
        
        print(f'Earliest log timestamp: {earliest}')
        print(f'Latest log timestamp: {latest}')

    def run(self):
        try:
            log_counts, earliest, latest = self.aggregate_logs()
            self.display_aggregated_data(log_counts=log_counts, earliest=earliest, latest=latest)
        except FileNotFoundError:
            print(f'Error: Log file {self.log_file_path} not found!')


if __name__ == '__main__':
    log_file_path = 'logs.txt'
    aggregator = LogAggregator(log_file_path)
    aggregator.run()
