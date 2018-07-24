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
    question['submission_time'] = util.get_timestamp()

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


@connection.connection_handler
def add_answer_by_question_id(cursor, new_answer):
    submission_time = util.get_timestamp()
    new_answer['submission_time'] = submission_time
    new_answer['vote_number'] = 0
    timestamp = util.get_timestamp()

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
        search_words_dict['phrase' + str(index)] = '%' + search_words[index] + '%'
        condition_list.append(condition)

    query += ' AND '.join(condition_list)

    cursor.execute(query, search_words_dict)
    results = cursor.fetchall()
    return results


@connection.connection_handler
def read_the_last_five_question(cursor):
    query = """
            SELECT * FROM question
            ORDER BY submission_time DESC 
            LIMIT 5"""
    cursor.execute(query)
    last_five_question=cursor.fetchall()
    return last_five_question


@connection.connection_handler
def get_answer_by_id(cursor, answer_id):

    query_answer = """SELECT message, image, id, question_id FROM answer
                WHERE id= %(id)s"""
    cursor.execute(query_answer, {'id': answer_id})
    answer_by_id= cursor.fetchall()

    return answer_by_id


@connection.connection_handler
def edit_question(cursor, edited_question):
    cursor.execute("""UPDATE question
                        SET title=%(title)s, message=%(message)s
                        WHERE id=%(id)s""", edited_question)


@connection.connection_handler
def delete_answer(cursor, id):
    cursor.execute("""DELETE FROM answer
                        WHERE id = %(id)s""", {"id": id})


@connection.connection_handler
def delete_question(cursor, id):
    cursor.execute("""DELETE FROM answer
                        WHERE question_id = %(id)s""", {"id": id})
    cursor.execute("""DELETE FROM question
                        WHERE id = %(id)s""", {"id": id})



@connection.connection_handler
def edit_answer(cursor, edited_answer):
    query = """ UPDATE answer
                SET submission_time= %(submission_time)s, message= %(message)s, image=%(image)s
                WHERE id= %(id)s"""
    cursor.execute(query, edited_answer )

@connection.connection_handler
def sort_question(cursor, order_by):

    query = """SELECT * FROM question
            ORDER BY {} {}""".format(order_by['column'], order_by['order'], order_by)
    cursor.execute(query)
    new_order= cursor.fetchall()
    return new_order


@connection.connection_handler
def list_all_users(cursor):
    query = """SELECT username.id, username.name, username.submission_time
            FROM username
            """
    cursor.execute(query)
    all_users = cursor.fetchall()
    return all_users