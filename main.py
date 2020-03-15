from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/students")
# def students():
#     def db_query():
#         db = Database()
#         students = db.list_students()
#         return students
#     res = db_query()
#     return render_template("show_students.html", result=res, content_type='application/json')
#

@app.route("/show_students")
def show_students():
    def db_query():
        db = Database()
        students = db.list_students()
        return students
    res = db_query()
    return render_template("show_students.html", result=res, content_type='application/json')


@app.route("/add_student", methods=['GET', 'POST'])
def add_student():
    if request.method == "POST":
        details = request.form
        first_name = details['first_name']
        last_name = details['last_name']
        age = details['age']
        db = Database()
        db.add_student(first_name, last_name, age)
        return show_students()
    return render_template("add_student.html")


@app.route("/change_student", methods=['GET', 'POST'])
def change_student():
    if request.method == "POST":
        details = request.form
        first_name = details['first_name']
        last_name = details['last_name']
        age = details['age']
        id = details['id']
        db = Database()
        db.change_student(first_name, last_name, age, id)
    return render_template("change_student.html")

@app.route("/classes")
def classes():
    def db_query():
        db = Database()
        classes = db.list_classes()
        return classes
    res = db_query()
    return render_template("classes.html", result=res, content_type='application/json')


@app.route("/grades")
def grades():
    return render_template("grades.html")


if __name__ == "__main__":
    app.run(debug=True)
