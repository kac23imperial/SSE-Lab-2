from flask import Flask, render_template, request, send_file
import re

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/Logo.png")
def get_image():
    return send_file("templates/Logo.png")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_course = request.form.get("course")
    return render_template(
        "hello.html", name=input_name, age=input_age, course=input_course
    )


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    return process_query(q)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif q == "What is your name?":
        return "Karen and Nicole"
    elif q.startswith("Which of the following numbers is the largest:"):
        return str(max([int(i) for i in re.findall(r'[0-9]+', q)]))
        # return "61"
    elif q.startswith("What is") and "multiplied by" in q:
        words = q.split()
        first_number = int(words[2])
        second_number = int(words[-1][:-1])
        return str(first_number * second_number)
    else:
        return "Unknown"
