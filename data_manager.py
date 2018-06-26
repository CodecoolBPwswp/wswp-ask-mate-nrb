

DATA_HEADER_ANSWER = ['id' ,'submisson_time','vote_number','question_id','message,image']
DATA_HEADER_QUESTION = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

connection.get_all_answers("answer.csv")

connection.get_all_questions("question.csv")