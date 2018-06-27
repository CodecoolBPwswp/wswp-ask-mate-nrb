from flask import Flask, request, url_for, session, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def index():
    pass


@app.route('/question/<question_id>')
def display_question():
    pass


@app.route('/add-question')
def add_question():
    return render_template("add-question.html")


@app.route('/add-question', methods=['POST'])
def saving_add_question():
    if request.method == 'POST':
        id = util.ge
        submisson_time=util.get_timestamp()
        view_number= '0'
        vote_number = '0'
        title = request.form["title"]
        message = request.form["message" ]
        image_path = request.form["image_path"]
        row ={'id':id, 'submisson_time': submisson_time, 'view_number': view_number,'vote_number': vote_number,'title':title, 'message': message,'image_path':image_path}

        return redirect(url_for('/question/<question_id>'))


@app.route('/question/<question_id>/new-answer')
def add_answer():
    pass


@app.route('/question/<question_id>/new-answer', methods=['POST'])
def adding_answer():
    pass


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )