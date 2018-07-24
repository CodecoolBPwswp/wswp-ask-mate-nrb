from flask import Flask, request, url_for, render_template, redirect
import util, data_manager

app = Flask(__name__)


@app.route('/')
def index():
    last_five_question = data_manager.read_the_last_five_question()
    return render_template('index.html', last_five_question=last_five_question)

@app.route('/list')
def all_question():
    all_question = data_manager.read_all_questions()
    return render_template('all_question.html', all_question=all_question)

@app.route('/list/', methods=['GET'])
def sort_question():
    if request.method == 'GET':

        order_by= {'column':request.args.get('column','submission_time'), 'order':request.args.get('order', 'DESC')}

        sort_all_question = data_manager.sort_question(order_by)

    return render_template('all_question.html', all_question=sort_all_question)

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

    return redirect(url_for('display_question_by_id', question_id=question_id))


@app.route('/add-question')
def add_question():
    return render_template('/add-question.html')

@app.route('/question/<id>/edit', methods=['POST', 'GET'])
def edit_question(id):
    if request.method == 'POST':
        edited_question = {"id": id,
                           "title": request.form["title"],
                           "message": request.form["message"]}
        data_manager.edit_question(edited_question)
        return redirect('/question/' + '{}'.format(edited_question['id']))
    else:
        return render_template('edit_question.html', question_by_id=data_manager.get_question_by_id(id))


@app.route('/answer/<id>/delete', methods=['POST'])
def delete_answer(id):
    data_manager.delete_answer(id)
    question_id = request.form['question_id']
    return redirect('/question/' + '{}'.format(question_id))


@app.route('/question/<id>/delete', methods=['POST'])
def delete_question(id):
    data_manager.delete_question(id)
    return redirect('/')


@app.route('/add-question', methods=['POST'])
def saving_add_question():
    if request.method == 'POST':

        title = request.form["title"]
        message = request.form["message" ]

        question = {'title': title, 'message': message, 'image': ''}
        data_manager.write_question(question)
        ID = data_manager.get_question_id(title)
        return redirect('/question/{}'.format(ID[0]['id']))

@app.route('/answer/<answer_id>/edit')
def display_answer_by_id(answer_id):
    answer= data_manager.get_answer_by_id(answer_id)

    return render_template('update_answer.html', answer=answer)

@app.route('/answer/<answer_id>/edit', methods=['POST'])
def update_answer_by_id(answer_id):
    if request.method == 'POST':

        edited_message = request.form['message']
        edited_image =request.form['image']
        submission_time = util.get_timestamp()
        edited_answer = {'submission_time': submission_time, 'message':edited_message, 'image': edited_image, 'id': answer_id}
        data_manager.edit_answer(edited_answer)

        question_id =request.form['question_id']

        return redirect(url_for('display_question_by_id', question_id=question_id))


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        search_phrase = request.args.get("search", '')
        search_words = search_phrase.split(' ')

        result_search = data_manager.search_by_words(search_words)

        return render_template('results_search.html', result_search=result_search, search_phrase=search_phrase)


@app.route('/list_users', methods=['GET'])
def list_users():
    users_list = data_manager.list_all_users()
    return render_template('list_users.html', users_list=users_list)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )