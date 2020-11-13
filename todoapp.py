import re
from flask import Flask,render_template,request, redirect
app = Flask(__name__)

todolist = []
# todolist.append(('Task1', 'a@sps.com', 'Medium'))
# todolist.append(('Task2', 'b@sps.com', 'Low'))
# todolist.append(('Task3', 'c@sps.com', 'High'))
error_message=''

@app.route('/')
def main():
    return render_template('index.html',todolist = todolist,error_message=error_message)

@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['Task']
    email = request.form['Email']
    priority = request.form['Priority']
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    global error_message
    error_message=''
    if (re.search(regex, email)):
        todolist.append((task,email,priority))
    else:
        error_message='Email address is not valid'

    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    todolist.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()