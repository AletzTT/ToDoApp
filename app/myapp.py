from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/alex/Projects/Flask/TodoApp/app/database/tasks.db'
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    done = db.Column(db.Boolean)

@app.route('/')
def saludo():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return "Administrar Contenido"


if __name__ == '__main__':
    app.run(debug=True)

