import connection

DATA_HEADER_ANSWER = ['id' ,'submission_time','vote_number','question_id','message', 'image']
DATA_HEADER_QUESTION = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
QUESTION_HEADER_TITLES = ['ID', 'Submission Time', 'Viewed', 'Title', 'Question']

def read_all_questions():
    return connection.get_all_questions()

def write_question(question):
    return connection.save_question(question, DATA_HEADER_QUESTION)