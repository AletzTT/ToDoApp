from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/alex/Projects/Flask/TodoApp/app/database/tasks.db'
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    done = db.Column(db.Boolean)

@app.route('/')
def home():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def create_task():
    task = Tasks(content = request.form['content'], done = False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done/<id>')
def done(id):
    task = Tasks.query.filter_by(id=int(id)).first()
    task.done = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/undone/<id>')
def undone(id):
    task = Tasks.query.filter_by(id=int(id)).first()
    task.done = False
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    task = Tasks.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/admin')
def admin():
    return "Administrar Contenido"

if __name__ == '__main__':
    app.run(debug=True)

