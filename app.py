from flask import Flask, render_template

app = Flask(__name__,)

students = {
    'user_1' : {
        'first_name' : 'John',
        'last_name' : 'Doe',
        'age' : 20
    },
    'user_2' : {
        'first_name' : 'Kelly',
        'last_name' : 'Doe',
        'age' : 22
    },
    'user_3' : {
        'first_name' : 'Smith',
        'last_name' : 'Doe',
        'age' : 15
    },
}

colors = ['red', 'blue', 'green']

@app.route("/")
def hello_world():
    return render_template('index.html', users = students, colors = colors)