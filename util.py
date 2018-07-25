import time
from datetime import datetime
import bcrypt

def get_timestamp():
    time_stamp = int(time.time())
    submission_time = datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")

    return submission_time


def get_vote_num():
    pass


def get_view_num():
    pass


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

    return hashed_bytes.decode('utf-8')