from flask import Flask, render_template, send_file, request

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
    return render_template("hello.html", name=input_name,
                           age=input_age, course=input_course)


@app.route("/query/<q>", methods=["GET"])
def process_query(q):
    if q == 'dinosaurs':
        return 'Successful'
    else:
        return 'Failure'
