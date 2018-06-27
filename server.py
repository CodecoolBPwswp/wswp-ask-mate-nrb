from flask import Flask, request, url_for, session, render_template, redirect
import connection


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
    print(data_header)
    return render_template('list.html', data=old_data,
                                        question_headers=data_manager.QUESTION_HEADER_TITLES,
                                        data_header=data_header)


@app.route('/question/<question_id>')
def display_question(question_id):

    # all_question = [{'id':'0', 'submission_time':'1493368154', 'view_number':'29', 'vote_number':'7', 'title':"How to make lists in Python?", 'message':"I am totally new to this, any hints?", 'image':''}, {'id':'1', 'submission_time':'1493068124', 'view_number':'15', 'vote_number':'9', 'title':"Wordpress loading multiple jQuery Versions", 'message':"I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $('.myBook').booklet() I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine. BUT in my theme i also using jquery via webpack so the loading order is now following: jquery booklet app.js(bundled file with webpack, including jquery)", 'image':"images / image1.png"}, {'id':'2', 'submission_time':'1493015432', 'view_number':'1364', 'vote_number':'57', 'title':"Drawing canvas with an image picked with Cordova Camera Plugin", 'message':"I'm getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I'm on IOS, it throws errors such as cross origin issue, or that I'm trying to use an unknown format.", 'image':''}]
    #
    # all_answer = [{'id':'0','submission_time':'1493398154','vote_number':'4','question_id':'0','message':"You need to use brackets: my_list = []",'image':""}, {'id':'1', 'submission_time':'1493088154', 'vote_number':'35', 'question_id':'0', 'message':"Look it up in the Python docs This is the code I'm using to draw the image (that works on web/desktop but not cordova built ios app)", 'image':""}]
    all_question = connection.get_all_questions()
    all_answer = connection.get_all_answers()


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
        id = util.generate_question_id()
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