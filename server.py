from flask import Flask, request, url_for, session, render_template, redirect
import connection
import util
import data_manager
import util, data_manager



app = Flask(__name__)


@app.route('/')
@app.route('/list')
def index():
    all_questions = data_manager.read_all_questions()
    print(all_questions)
    return render_template('list.html', all_questions=all_questions)


@app.route('/question/<question_id>')
def display_question_by_id(question_id):
    question_by_id = data_manager.get_question_by_id(question_id)
    answers_by_question_id = data_manager.get_answer_by_question_id(question_id)

    return render_template('question_id_answer.html', question_by_id=question_by_id, answers_by_question_id=answers_by_question_id)


@app.route('/question/<question_id>/new-answer')
def add_answer(question_id):
    question_by_id = data_manager.get_question_by_id(question_id)
    answers_by_question_id = data_manager.get_answer_by_question_id(question_id)
    new_answer = True

    return render_template("question_id_answer.html", new_answer=new_answer, question_id=question_id, question_by_id=question_by_id, answers_by_question_id=answers_by_question_id)


@app.route('/question/<question_id>/new-answer', methods=['POST'])
def adding_answer(question_id):
    question_id = question_id
    message = request.form['message']
    image = request.form['image_path']
    new_answer = {'question_id':question_id,'message':message, 'image': image}
    data_manager.add_answer_by_question_id(new_answer)

    return redirect('/question/{}'.format(question_id))


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

        row ={'id':id, 'submission_time': submission_time, 'view_number': view_number,'vote_number': vote_number,'title':title, 'message': message,'image':''}
        data_manager.write_question(row)
        return redirect('/question/{}'.format(id))


@app.route('/list', methods=['GET'])
def search():
    search_phrase = request.form["search"]
    search_words = search_phrase.split(' ')

    result_search = data_manager.search_by_words(search_words)

    return redirect('/search?q=<{}>'.format(search_phrase))





if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )