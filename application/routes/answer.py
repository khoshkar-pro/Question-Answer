from application import app, db_get, user_session
from flask import render_template, request, redirect, url_for

@app.route('/answer/<question_id>', methods=['POST', 'GET'])
def answer(question_id):
    user = user_session()
    if not user:
        return redirect(url_for('register'))
    if user['expert'] == 0:
        return redirect(url_for('home'))
    db = db_get()
    question_curr = db.execute('SELECT question_text from questions WHERE id = ?', [question_id])
    question_result = question_curr.fetchone()
    if request.method == 'POST':
        db.execute('UPDATE questions SET answer_text = ? WHERE id = ? ', [request.form['question'], question_id])
        db.commit()
        return redirect(url_for('unanswered'))
    return render_template('answer.html', title='Question reply', user=user, question_result=question_result)