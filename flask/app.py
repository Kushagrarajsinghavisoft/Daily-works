from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Configuration for the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) #creating SQLAlchemy class object(db) which sets up a link between the Flask application (app) 
                     #and the SQLAlchemy database (db)

# Model representing the 'Todo' table in the database
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(400), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} -> {self.title}"

# Flask CLI command to create the database tables
@app.cli.command("initdb")
def initdb_command():
    with app.app_context():
        db.create_all()
        print("Initialized the database.")

# Route for the main page, handling both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def view():
    # Handling POST request to add a new Todo
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    # Fetching all Todo items from the database
    allTodo = Todo.query.all()

    # Rendering the main page with the list of Todo items
    return render_template('index.html', allTodo=allTodo)

# Route for updating a Todo item, handling both GET and POST requests
@app.route('/update/<sno>', methods=['GET', 'POST'])
def update(sno):
    # Handling POST request to update a Todo
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    # Fetching the Todo item to be updated
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

# Route for deleting a Todo item
@app.route('/delete/<int:sno>')
def delete(sno):
    # Fetching the Todo item to be deleted
    todo = Todo.query.filter_by(sno=sno).first()
    
    # Deleting the Todo item from the database
    db.session.delete(todo)
    db.session.commit()
    
    # Redirecting back to the main page
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
