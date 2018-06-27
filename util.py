import time
from datetime import datetime, timezone

def get_id():
    pass


def get_timestamp():
    time_stamp = time.time()
    return time_stamp


def readable_time_stamp(time_stamp):
    converted_time_stamp = int(time_stamp).strftime("%Y-%m-%d %H:%M:%S")
    return converted_time_stamp


def get_vote_num():
    pass


def get_view_num():
    pass