from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key="abc"
app.debug = True


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        excercise= int(request.form["excercise"])
        rest= int(request.form["rest"])
        sets= int(request.form["sets"])

        session["excercise"] = excercise
        session["rest"] = rest
        session["sets"] = sets
        session["set_counter"] = 0
        return redirect(url_for("excercise"))
    return render_template("home.html")


@app.route("/rest")
def rest():
    return render_template("rest.html", rest=session["rest"])

@app.route("/complete")
def complete():
    return render_template("complete.html")

@app.route("/excercise")
def excercise():
    if session["set_counter"] ==session["sets"]:
        return redirect(url_for("complete"))
    session["set_counter"] +=1
    return render_template("excercise.html",excercise=session["excercise"])

if __name__ == '__main__':
    app.run()