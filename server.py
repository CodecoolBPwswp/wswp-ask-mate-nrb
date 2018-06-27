from flask import Flask, request, url_for, session, render_template, redirect
import connection
import util
import data_manager
import util, data_manager



app = Flask(__name__)


@app.route('/')
@app.route('/list')
def index():
    old_data = data_manager.read_all_questions()
    data_header = []
    for item in data_manager.DATA_HEADER_QUESTION:
        if item == "vote_number" or item == "image":
            continue
        else:
            data_header.append(item)
    return render_template('list.html', data=old_data,
                                        question_headers=data_manager.QUESTION_HEADER_TITLES,
                                        data_header=data_header)


@app.route('/question/<question_id>')
def display_question(question_id):

    all_question = data_manager.read_all_questions()
    all_answer = data_manager.read_all_answers()

    display_question = None
    display_answer = []

    for question in all_question:
        if question_id == question['id']:
            display_question = question
    for answer in all_answer:
        if question_id == answer['question_id']:
            display_answer.append(answer)


    return render_template('question_id_answer.html', question=display_question, all_display_answer=display_answer)


@app.route('/add-question')
def add_question():
    return render_template('/add-question.html')


@app.route('/add-question', methods=['POST'])
def saving_add_question():
    if request.method == 'POST':
        id = util.generate_id(data_manager.read_all_questions())
        submission_time= util.get_timestamp()
        view_number= '0'
        vote_number = '0'
        title = request.form["title"]
        message = request.form["message" ]
        image = request.form["image_path"]
        row ={'id':id, 'submission_time': submission_time, 'view_number': view_number,'vote_number': vote_number,'title':title, 'message': message,'image':image}
        data_manager.write_question(row)
        return redirect('/question/{}'.format(id))



@app.route('/question/<question_id>/new-answer')
def add_answer(question_id):
    all_question = data_manager.read_all_questions()
    all_answer = data_manager.read_all_answers()

    display_question = None
    display_answer = []

    for question in all_question:
        if question_id == question['id']:
            display_question = question
    for answer in all_answer:
        if question_id == answer['question_id']:
            display_answer.append(answer)

    new_answer = True
    return render_template("question_id_answer.html", new_answer=new_answer, question_id=question_id, question=display_question, all_display_answer=display_answer)


@app.route('/question/<question_id>/new-answer', methods=['POST'])
def adding_answer(question_id):
    id = '0'
    submission_time = util.get_timestamp()
    vote_number= '0'
    question_id = question_id
    message = request.form['message']
    image = request.form['image_path']
    # new_answer = {'id':id ,'submission_time':submission_time,'vote_number':vote_number,'question_id':question_id,'message':message, 'image':image}



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )