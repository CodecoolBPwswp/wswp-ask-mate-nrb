import connection

DATA_HEADER_ANSWER = ['id' ,'submission_time','vote_number','question_id','message', 'image']
DATA_HEADER_QUESTION = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
QUESTION_HEADER_TITLES = ['ID', 'Submission Time', 'Viewed', 'Title', 'Question']

def read_all_questions():
    all_questions = connection.get_all_questions()
    return all_questions

def read_all_answers():
    all_answers = connection.get_all_answers()
    return all_answers