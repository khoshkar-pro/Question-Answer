from application import app, db_get, user_session
from flask import render_template, request, redirect, url_for

@app.route('/answer/<question_id>', methods=['POST', 'GET'])
def answer(question_id):
    user = user_session()
    db = db_get()
    question_curr = db.execute('SELECT question_text from questions WHERE id = ?', [question_id])
    question_result = question_curr.fetchone()
    if request.method == 'POST':
        db.execute('UPDATE questions SET answer_text = ? WHERE id = ? ', [request.form['question'], question_id])
        db.commit()
        return redirect(url_for('unanswered'))
    return render_template('answer.html', user=user, question_result=question_result)