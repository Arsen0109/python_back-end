from python_backend import app


@app.route("/")
def hello():
    return "Hello world!"


