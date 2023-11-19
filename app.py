# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add(a, b):
    """adds a and b"""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])

    # The flask Request object contains the attributes of the URL request.
    #  The args attribute is a dictionary containing arguments from
    # the URL. The get() method is a built-in dictionary method
    #  that will “get” an item from a dictionary or return
    # a default value (None if key not found).
    #  In this case, it avoids a KeyError if “a”  or "b" argument not found.

    result = add(a, b)

    str(result)


@app.route('/sub')
def sub(a, b):
    """Substract b from a."""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])

    result = sub(a, b)

    str(result)


@app.route('/mult')
def mult(a, b):
    """Multiply a and b."""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])

    result = mult(a, b)

    str(result)


def div(a, b):
    """Divide a by b."""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])

    result = div(a, b)

    str(result)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
# value of properties are the functions from the operations file which
# we imported earlier


@app.route("/math/<oper>")
# the operators are the route params
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)
    # this calls the function on a and b

    return str(result)
