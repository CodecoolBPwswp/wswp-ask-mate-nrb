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
def add_question()
    pass


@app.route('/add-question', methods=['POST'])
def adding_question():
    pass


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