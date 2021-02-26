from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return render_template('index.html', title='Welcome', text=text)


app.run(host='0.0.0.0', port=81)
