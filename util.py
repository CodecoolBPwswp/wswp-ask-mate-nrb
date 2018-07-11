import time, connection
from datetime import datetime


def generate_id(data_list):
    ids=[]
    for row in data_list:
        ids.append(int(row['id']))

    if ids == []:
        return '1'

    new_id = max(ids)+1
    return new_id


def get_timestamp():
    time_stamp = int(time.time())
    submission_time = datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")

    return submission_time







def get_vote_num():
    pass


def get_view_num():
    pass