import time, connection
from datetime import datetime


def generate_question_id():
    ids=[]
    for row in connection.get_all_questions():
        ids.append(int(row['id']))
    new_id = max(ids)+1
    return new_id


generate_question_id()

def get_timestamp():
    time_stamp = int(time.time())
    return time_stamp


def readable_time_stamp(time_stamp):
    converted_time_stamp = int(time_stamp).strftime("%Y-%m-%d %H:%M:%S")
    return converted_time_stamp


def get_vote_num():
    pass


def get_view_num():
    pass