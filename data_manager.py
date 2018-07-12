import connection
import util


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


@connection.connection_handler
def write_question(cursor, question):
    question['vote_number'] = 0
    question['view_number'] = 0
    query = """
               INSERT INTO question(submission_time, view_number, vote_number, title, message, image)
               VALUES (%(submission_time)s,%(view_number)s,%(vote_number)s, %(title)s, %(message)s, %(image)s)
               """
    cursor.execute(query, question)


@connection.connection_handler
def get_question_id(cursor, title):
    queryID ="""
        SELECT id FROM question
        WHERE title = %(title)s"""
    cursor.execute(queryID, {'title': title})
    question_id = cursor.fetchall()
    return question_id





def read_all_answers():
    return connection.get_all_answers()

@connection.connection_handler
def add_answer_by_question_id(cursor, new_answer):
    submission_time = util.get_timestamp()
    new_answer['submission_time'] = submission_time
    new_answer['vote_number'] = 0
    timestamp = util.get_timestamp()
    new_answer['timestamp'] = timestamp
    new_answer['vote'] = 0


    query = """
            INSERT INTO answer (submission_time, vote_number, question_id, message, image)
            VALUES (%(submission_time)s,%(vote_number)s, %(question_id)s, %(message)s, %(image)s)
            """
    cursor.execute(query, new_answer)


@connection.connection_handler
def search_by_words(cursor, search_words):
    search_words_dict = {}
    condition_list = []
    query = 'SELECT * FROM question WHERE '
    for index in range(len(search_words)):
        condition = '(title ILIKE %(phrase' + str(index) + ')s OR message ILIKE %(phrase' + str(index) + ')s)'
        search_words_dict['phrase' + str(index)] = new_answer[index]
        condition_list.append(condition)

    query += ' AND '.join(condition_list)

    cursor.execute(query, search_words_dict)

    return cursor.fetchall()


@connection.connection_handler
def read_the_last_five_question(cursor):
    query = """
            SELECT * FROM question
            LIMIT 5"""
    cursor.execute(query)
    last_five_question=cursor.fetchall()
    return last_five_question
