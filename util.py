from datetime import datetime
import time
import bcrypt

def get_timestamp():
    time_stamp = int(time.time())
    submission_time = datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")

    return submission_time

def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)