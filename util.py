import time, connection
from datetime import datetime

def get_timestamp():
    time_stamp = int(time.time())
    return time_stamp


def readable_time_stamp(any_list):
    for row in any_list:
        row['submission_time'] = datetime.fromtimestamp(int(row['submission_time'])).strftime("%Y-%m-%d %H:%M:%S")
    return any_list


def get_vote_num():
    pass


def get_view_num():
    pass