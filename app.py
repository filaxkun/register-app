from flask import Flask, render_template, request, redirect

app = Flask(__name__)

people = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name     = request.form.get("name")
    activity = request.form.get("activity")
    if not name or not activity:
        return render_template("failure.html")
    people.append(f"{name} subbed to {activity}")
    #return render_template("success.html",name=name,activity=activity)
    return redirect("/registrants")

@app.route("/registrants")
def show_registrants():
    return render_template("registrants.html",people=people)
