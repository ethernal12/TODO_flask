from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment

app = Flask(__name__)
# Add the enumerate function to the jinja2 environment
app.jinja_env.globals.update(enumerate=enumerate)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create an empty list to store our
todo_list = []


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    cpmplete = db.Column(db.Boolean)


@app.route('/', methods=["POST", "GET", "PUT"])
def index():
    response = request.args.get('Response', None)
    print(response, 'from index')
    return render_template('base.html', todo_list=todo_list), response


# add one item
@app.route("/todos", methods=["POST", "PUT"])
def add_todo():
    title = request.form.get("title")
    todo_list.append(title)

    return render_template('base.html', todo_list=todo_list)


# update item
@app.route("/todos/<int:todo_id>", methods=["POST","PUT"])
def update_todo(todo_id):
    print('update!!!!!!!!!!!!!!!!!!!!!')
    title = request.form.get('title')
    print(title, 'update')
    # Update the item in your list here
    todo_list[todo_id] = title
    return redirect(url_for("index"))


# delete item
@app.route("/todo/<int:todo_id>", methods=['POST', 'DELETE'])
def delete_todo(todo_id):
    title = todo_list[todo_id]
    del todo_list[todo_id]

    return redirect(url_for("index"), Response=title)



# get  one item
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    print(todo_list)
    return jsonify({'title': todo_list[todo_id]})


# get all items
@app.route("/todos/", methods=["GET"])
def get_todos():
    return todo_list


@app.route('/About')
def about():
    return {'Data': 'About page'}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        new_todo = Todo(title='title 1', cpmplete=False)
        db.session.add(new_todo)
        db.session.commit()
    app.run(debug='True')
