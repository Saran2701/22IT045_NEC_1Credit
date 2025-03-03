# Update this file to add your code
# /name - Should give your name
# /register_number - Should give your register_number
# /department - Should give your department

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, from Saran!'

@app.route('/name')
def get_name():
    return 'Saran S' 

@app.route('/register_number')
def get_register_number():
    return '22IT045'

@app.route('/department')
def get_department():
    return 'Information Technology'

if __name__ == '__main__':
    app.run(debug=True)