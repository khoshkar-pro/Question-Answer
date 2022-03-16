from application import app, db_get, user_session
from flask import render_template, request

@app.route('/ask', methods=['POST', 'GET'])
def ask():
    db = db_get()
    user = user_session()
    if request.method == 'POST':
        db.execute('INSERT INTO questions (question_text, asked_by_id, expert_id) values (?, ?, ?)', [request.form['question'], user['id'], request.form['expert']])
        db.commit()
    exp_curr = db.execute('SELECT id, name FROM users WHERE expert = 1')
    exp_result = exp_curr.fetchall()
    return render_template('ask.html', title='Ask a question', user=user, exp_result=exp_result)