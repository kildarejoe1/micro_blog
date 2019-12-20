from flask import Flask, render_template, url_for, request,redirect
app=Flask(__name__)

posts = [
    {
     'author': 'henry morrin',
     'title': 'my first post',
     'content': "First content Post",
     'date_posted':'April 22nd 2018'
    },
    {
     'author': 'alan morrin',
     'title': 'my alan post',
     'content': 'alan content Post',
     'date_posted': 'April 14th 2019'
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/user/<name>")
def user(name):
    return " Hello %s , welcome back!!" % name

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/test")
def test():
    return render_template("test.html", variable="random")

@app.route("/error")
def error():
    return "Error, Error!!!", 400

@app.route("/redirect")
def redirect():
    return redirect('http://www.facebook.com')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
