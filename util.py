import time, connection
from datetime import datetime

def get_timestamp():
    time_stamp = int(time.time())
    submission_time = datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")

    return submission_time







def get_vote_num():
    pass


def get_view_num():
    pass