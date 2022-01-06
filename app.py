from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)
app.secret_key="abc"
app.debug = True


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/pytimerDB'
db=SQLAlchemy(app)


class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80))
    worktime = db.Column(db.Integer)
    resttime = db.Column(db.Integer)
    setscount = db.Column(db.Integer)


db.create_all()
db.session.commit()


@app.route("/", methods=["GET","POST"])
def home():
    def to_seconds(timestr):
        seconds= 0
        for part in timestr.split(':'):
            seconds= seconds*60 + int(part, 10)
        return seconds
    



    
    if request.method == "POST":
        excercise= to_seconds(request.form["excercise"])
        rest= to_seconds(request.form["rest"])
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
    # print("id ",id)


    # timequery = Time(user=id,worktime=excercise, resttime=rest)
    # print("timequery: ",timequery)
    # print("timequery: ",timequery)
    # print("timequery: ",type(timequery))
    # print("timequery: ",vars(timequery))
    # print("timequery: ",dir(timequery))

    if session["set_counter"] ==session["sets"]:
        return redirect(url_for("complete"))
    session["set_counter"] +=1
    
    return render_template("excercise.html",excercise=session["excercise"])

@app.route("/test")
def test():

    return render_template("test.html")


@app.route("/progress")
def progress():
    rest_status=True
    return render_template("progress.html")

@app.route("/post_data", methods=["POST"])
def post_data():
    # user=User(user=request.form["username"],worktime=request.form["worktime"])
    # updater = User.query.filter_by(user=request.form["username"]).first()
    # print("updater: ",updater)
    # print("updater: ",type(updater))
    # print("updater: ",vars(updater))
    # # db.session.add(user)
    # updater.worktime = request.form["worktime"]
    # db.session.commit()
    testing()
    return redirect(url_for("test"))

def testing():
    print("testing")



def timer():
    excerciseVal=session["excercise"]
    restVal=session["rest"]
    setVal=session["sets"]
    
    def timerRun():
        render_template("excercise.html")
        for i in range(excerciseVal):
            print("i ",i)
            time.sleep(1)
    timerRun()
    

    print("excerciseVal", excerciseVal)
    print("restVal", restVal)
    print("setVal", setVal)




if __name__ == '__main__':
    app.run()