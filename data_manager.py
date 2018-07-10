import connection

DATA_HEADER_ANSWER = ['id' ,'submission_time','vote_number','question_id','message', 'image']
DATA_HEADER_QUESTION = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
QUESTION_HEADER_TITLES = ['ID', 'Submission Time', 'Viewed', 'Title', 'Question']


@connection.connection_handler
def read_all_questions(cursor):
    query = """ 
                SELECT * FROM  question"""
    cursor.execute(query)
    questions=cursor.fetchall()
    return questions


@connection.connection_handler
def



def write_question(question):
    return connection.save_question(question, DATA_HEADER_QUESTION)


def read_all_answers():
    return connection.get_all_answers()

def write_answer(answer):
    return connection.save_answer(answer, DATA_HEADER_ANSWER)