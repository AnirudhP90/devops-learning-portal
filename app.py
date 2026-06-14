from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/roadmaps")
def roadmaps():
    return render_template("roadmaps.html")


@app.route("/study-materials")
def study_materials():
    return render_template("study_materials.html")


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/interview-questions")
def interview_questions():
    return render_template("interview_questions.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
