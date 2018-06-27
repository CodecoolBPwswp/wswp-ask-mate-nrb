from flask import Flask, request, url_for, session, render_template, redirect


import data_manager

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
    print(data_header)
    return render_template('list.html', data=old_data,
                                        question_headers=data_manager.QUESTION_HEADER_TITLES,
                                        data_header=data_header)


@app.route('/question/<question_id>')
def display_question():
    pass


@app.route('/add-question')
def add_question():
    return render_template("add-question.html")


"""@app.route('/add-question', methods=['POST'])
def saving_add_question():
    if request.method == 'POST':
        'id' = request.form['id']
        'submisson_time'= request.form['submisson_time"']
        "view_number" = request.form["view_number"]
        "vote_number" = request.form["vote_number"]
        "title" = request.form["title"]
        "message" = request.form["message" ]
        "image_path" = request.form["image_path"]

        return redirect(url_for('/question/<question_id>'))"""


@app.route('/question/<question_id>/new-answer')
def add_answer():
    pass


@app.route('/question/<question_id>/new-answer', methods=['POST'])
def adding_answer():
    pass


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )