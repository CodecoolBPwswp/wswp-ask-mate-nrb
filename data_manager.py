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
def add_answer_by_question_id(cursor, new_answer):
    timestamp = util.get_timestamp()
    new_answer['timestamp'] = timestamp
    new_answer['vote'] = 0


    query = """
            INSERT INTO answer (vote_number, question_id, message, image)
            VALUES (%(vote_number)s, %(question_id)s, %(message)s, %(image)s)
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