from application import app, user_session, db_get
from flask import render_template
@app.route('/')
@app.route('/home')
def home():
    user = user_session()
    db = db_get()
    home_curr = db.execute('select questions.id, questions.question_text as question_text, \
    questions.answer_text as answer_text, askers.name as asker, experts.name as expert\
    from questions join users as askers on askers.id = questions.asked_by_id \
    join users as experts on experts.id = questions.expert_id\
    where questions.answer_text is not null')
    home_result = home_curr.fetchall()
    return render_template('home.html', title='Home', user = user, home_result=home_result)