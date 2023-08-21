from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.services.generate_message import generate_message

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/hi/<name>/<int:number>")
@app.route("/hi/<name>")
@app.route("/hi")
def hi(name: str = "Daniel", number: int = 101):
    return generate_message(name=name, number=number)


@app.route("/hello")
@use_args({"name": fields.Str(missing="Daniel"), "number": fields.Int(missing=101)}, location="query")
def hello(args):
    name = args["name"]
    number = args["number"]

    return generate_message(name=name, number=number)


if __name__ == '__main__':
    app.run()
