from flask import (
    Flask,
    request,
    redirect,
    url_for,
    abort,
    make_response,
    json,
    jsonify,
    session,
)
import click

app = Flask(__name__)

app.secret_key = "Drmhze6EPcv0fN_81Bj-nA"


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/login")
def login():
    session["logged_in"] = True
    return redirect(url_for("hello"))


@app.route("/user/<string:username>")
def profile(username):
    return f"{username}'s profile"


# @app.cli.command('say-hello')
# def hello():
#     click.echo('hello')
# with app.test_request_context():
#     print(url_for('login'))
#     print(url_for('profile', username='John Doe'))
# if __name__ == '__main__':
#     app.run()


@app.route("/")
@app.route("/hello")
def hello():
    name = request.args.get("name")
    if name is None:
        name = request.cookies.get("name", "Human")  # 从Cookie中获取name值
        response = "<h1>Hello, %s!</h1>" % name
        # 根据用户认证状态返回不同的内容
        if "logged_in" in session:
            response += "[Authenticated]"
        else:
            response += "[Not Authenticated]"
    return response


@app.route("/goback")
def go_back():
    return redirect(url_for("hello"))


@app.route("/404")
def not_found():
    abort(500)


@app.route("/set/<name>")
def set_cookie(name):
    response = make_response(redirect(url_for("hello")))
    response.set_cookie("name", name)
    return response


@app.route("/logout")
def logout():
    if "logged_in" in session:
        session.pop("logged_in")
    return redirect(url_for("hello"))


@app.route("/foo")
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>' % url_for(
        "do_something", next=request.full_path
    )


@app.route("/bar")
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something and redirect</a>' % url_for(
        "do_something", next=request.full_path
    )


@app.route("/do_something")
def do_something():
    # do something
    # return redirect(url_for('hello'))
    # return request.args
    # return request.referrer
    return request.host_url
    # return redirect(request.args.get("next", url_for("hello")))
