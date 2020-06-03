from flask import Flask, render_template, request
from username_gen import make_username

app = Flask(__name__)

names = ['Alice', 'Bob', 'Charlie']


@app.route('/', methods=["GET","POST"])
def upload_name():
    return render_template('upload.html')


@app.route('/second', methods=["POST"])
def second_route():
    if request.method == "POST":

        req = request.form

        username = req.get("username")

        username_list = make_username(username)
        return render_template('result.html', names=username_list)


if __name__ == '__main__':
    app.run(debug=True)
