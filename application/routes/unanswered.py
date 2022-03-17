from application import app, user_session, db_get
from flask import render_template, redirect, url_for

@app.route('/unanswered')
def unanswered():
    try:
        db = db_get()
        user = user_session()
        curr = db.execute('SELECT questions.id as qu_id, questions.question_text, questions.asked_by_id, questions.expert_id, users.id, users.name FROM questions JOIN users on users.id = questions.asked_by_id WHERE questions.answer_text is NULL and expert_id = ?', [user['id']])
        result = curr.fetchall()
        return render_template('unanswered.html', title='Unanswered Questions', user=user, result=result)
    except UnboundLocalError:
        return redirect(url_for('home'))
    except TypeError:
        return redirect(url_for('home'))