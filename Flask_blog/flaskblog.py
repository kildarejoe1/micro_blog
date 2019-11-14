from flask import Flask, render_template
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

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/test")
def test():
    return render_template("test.html", variable="random")


    
if __name__ == '__main__':
    app.run(debug=True)
