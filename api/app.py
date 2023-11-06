from flask import Flask, render_template, request, send_file
import re
import requests

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


@app.route("/form")
def form():
    input_username = request.form.get("username")
    return render_template(
        "newpage.html", username=input_username
    )


@app.route('/new-user', methods=['GET'])
def new_user():
    return render_template(
        "github_form.html"
    )


@app.route('/submit-request', methods=["POST"])
def submit_username():
    username = request.form.get("username")
    response = requests.get("https://api.github.com/users/" + username + "/repos")

    if response.status_code == 200:
        repos = response.json()
        repo_data = [{
            'name': repo["name"],
            'last_updated': repo["updated_at"],
            'language': repo["language"],
            'stars': repo["stargazers_count"]
        } for repo in repos]
        return render_template("user_repos.html", username=username, repo_data=repo_data)
    else:
        error_message = "Error fetching repos. GitHub API returned status: " + str(response.status_code)
        return render_template("error.html", error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/githubstats", methods=["POST"])
def stats():
    input_username = request.form.get("username")
    return render_template(
        "newreturnpage.html", username=input_username
    )


@app.route
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
    elif q.startswith("What is") and "plus" in q:
        words = q.split()
        first_number = int(words[2])
        second_number = int(words[-1][:-1])
        return str(first_number + second_number)
    elif q.startswith("What is") and "minus" in q:
        words = q.split()
        first_number = int(words[2])
        second_number = int(words[-1][:-1])
        return str(first_number - second_number)
    elif q.startswith("Which of the following numbers is"
                      " both a square and a cube:"):
        numbers = [int(i) for i in re.findall(r'[0-9]+', q)]
        result = [str(num) for num in numbers if (num ** 0.5).is_integer()
                  and (num ** (1 / 3)).is_integer()]
        return ", ".join(result)
    else:
        return "Unknown"
