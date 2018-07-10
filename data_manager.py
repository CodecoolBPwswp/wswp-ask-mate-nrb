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
def get_question_by_id(cursor, id):
    query = """
                SELECT * FROM question
                WHERE id=%(id)s"""
    cursor.execute(query, {'id': id})
    question_by_id=cursor.fetchone()
    return question_by_id


@connection.connection_handler
def get_answer_by_question_id(cursor, id):
    query = """
                SELECT * FROM answer
                WHERE question_id = %(id)s"""
    cursor.execute(query, {'id': id})
    answer_by_question_id=cursor.fetchall()
    return answer_by_question_id


def write_question(question):
    return connection.save_question(question, DATA_HEADER_QUESTION)


def read_all_answers():
    return connection.get_all_answers()

@connection.connection_handler
def add_answer_by_question_id(cursor, new_answer):

    query = """
            INSERT INTO answer (vote_number, question_id, message, image)
            VALUES (%(vote_number)s, %(question_id)s, %(message)s, %(image)s)
            """
    cursor.execute(query, new_answer)
