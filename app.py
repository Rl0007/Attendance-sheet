from flask import *
from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import date, timedelta
from sqlalchemy import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_BINDS'] = {
    'sub1':      'sqlite:///sub1.db',
    'sub2':      'sqlite:///sub2.db',
    'sub3':      'sqlite:///sub3.db',
    'sub4':      'sqlite:///sub4.db',
    'sub5':      'sqlite:///sub5.db'

}
db = SQLAlchemy(app)


class user(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40))
    middlename = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email1 = db.Column(db.String(80), unique=True)


class sub1(db.Model):
    __bind_key__ = 'sub1'
    sno = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer)
    date = db.Column(db.String(12))
    std_name = db.Column(db.String(80))
    attendance = db.Column(db.String(1))


class sub2(db.Model):
    __bind_key__ = 'sub2'
    sno = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer)
    date = db.Column(db.String(12))
    std_name = db.Column(db.String(80))
    attendance = db.Column(db.String(1))


class sub3(db.Model):
    __bind_key__ = 'sub3'
    sno = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer)
    date = db.Column(db.String(12))
    std_name = db.Column(db.String(80))
    attendance = db.Column(db.String(1))


class sub4(db.Model):
    __bind_key__ = 'sub4'
    sno = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer)
    date = db.Column(db.String(12))
    std_name = db.Column(db.String(80))
    attendance = db.Column(db.String(1))


class sub5(db.Model):
    __bind_key__ = 'sub5'
    sno = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer)
    date = db.Column(db.String(12))
    std_name = db.Column(db.String(80))
    attendance = db.Column(db.String(1))


sub = sub1


@app.route("/setsub1")
def setsub1():
    subject = sub1.query.all()
    return render_template('attendance.html', subject=subject, sub='sub1')


@app.route("/setsub2")
def setsub2():
    subject = sub2.query.all()
    return render_template('attendance.html', subject=subject, sub='sub2')


@app.route("/setsub3")
def setsub3():
    subject = sub3.query.all()
    return render_template('attendance.html', subject=subject, sub='sub3')


@app.route("/setsub4")
def setsub4():
    subject = sub4.query.all()
    return render_template('attendance.html', subject=subject, sub='sub4')


@app.route("/setsub5")
def setsub5():
    subject = sub5.query.all()
    return render_template('attendance.html', subject=subject, sub='sub5')


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        firstname = request.form['id1']
        password = request.form['password']
        if bool(user.query.filter_by(firstname=firstname, email1=password).first()):
            return redirect('/attendance')
        else:
            print("user does not exist")

    print("hello")
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        password1 = request.form['password1']
        password2 = request.form['password2']

        ant = user.__table__.columns.keys()
        print(ant)

        a = bool(user.query.filter_by(email1=password1).first())
        if a == 1:
            print("exists")
        else:
            print("not exist")
            if password1 == password2:
                print("registered")
                uid = user(firstname=firstname, middlename=middlename,
                           lastname=lastname, email1=password1)
                db.session.add(uid)
                db.session.commit()
            else:
                return render_template("register.html")
            return render_template("login.html")

        # a=bool(user.query.filter_by(name=id).first())

    return render_template("register.html")


@app.route("/attendance")
def attendance():
    # sub = subject
    subject = sub1.query.all()
    # allattendance = sub.query.all()
    return render_template("attendance.html", subject=subject, sub='sub1')


@app.route("/delete/<int:sno>,<string:sub>")
def delete(sno, sub):
    # allbooks = book.query.all()
    if sub == 'sub1':
        delete_entry = sub1.query.filter_by(sno=sno).first()
    if sub == 'sub2':
        delete_entry = sub2.query.filter_by(sno=sno).first()
    if sub == 'sub3':
        delete_entry = sub3.query.filter_by(sno=sno).first()
    if sub == 'sub4':
        delete_entry = sub4.query.filter_by(sno=sno).first()
    if sub == 'sub5':
        delete_entry = sub5.query.filter_by(sno=sno).first()
    db.session.delete(delete_entry)
    db.session.commit()
    return redirect('/addnewattendance')


@app.route("/addnewattendance", methods=['GET', 'POST'])
def addnewattendance():
    if request.method == 'POST':
        sub = request.form['sub']
        date = request.form['date1']
        print(date)
        # date = datetime.datetime.strptime(date, "%Y-%m-%d")
        rollno = request.form['rollno']
        name = request.form['name']
        att = request.form['att']
        if sub == 'sub1':
            entry = sub1(rollno=rollno, std_name=name,
                         date=date, attendance=att)
            db.session.add(entry)
            db.session.commit()
            subject = sub1.query.all()
        elif sub == 'sub2':
            entry = sub2(rollno=rollno, std_name=name,
                         date=date, attendance=att)
            db.session.add(entry)
            db.session.commit()
            subject = sub2.query.all()
        elif sub == 'sub3':
            entry = sub3(rollno=rollno, std_name=name,
                         date=date, attendance=att)
            db.session.add(entry)
            db.session.commit()
            subject = sub3.query.all()
        elif sub == 'sub4':
            entry = sub4(rollno=rollno, std_name=name,
                         date=date, attendance=att)
            db.session.add(entry)
            db.session.commit()
            subject = sub4.query.all()
        elif sub == 'sub5':
            entry = sub5(rollno=rollno, std_name=name,
                         date=date, attendance=att)
            db.session.add(entry)
            db.session.commit()
            subject = sub5.query.all()

        return render_template("addnewattendance.html", subject=subject, sub=sub)

    subject = sub1.query.all()
    sub = 'sub1'
    return render_template("addnewattendance.html", subject=subject, sub=sub)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "POST":

        rollno = request.form.get("rollno")

        subject1 = sub1.query.filter_by(rollno=rollno).all()
        subject2 = sub2.query.filter_by(rollno=rollno).all()
        subject3 = sub3.query.filter_by(rollno=rollno).all()
        subject4 = sub4.query.filter_by(rollno=rollno).all()
        subject5 = sub5.query.filter_by(rollno=rollno).all()

        return render_template("search.html", subject1=subject1, subject2=subject2, subject3=subject3, subject4=subject4, subject5=subject5)


@app.route("/dailyatt", methods=['GET', 'POST'])
def dailyatt():

    if request.method == 'POST':
        date = request.form['date1']
        print(type(date))
        print(date)
        subject1 = sub1.query.filter_by(date=date)
        subject2 = sub2.query.filter_by(date=date)
        subject3 = sub3.query.filter_by(date=date)
        subject4 = sub4.query.filter_by(date=date)
        subject5 = sub5.query.filter_by(date=date)
        return render_template("dailyatt.html", subject1=subject1, subject2=subject2, subject3=subject3, subject4=subject4, subject5=subject5)
    return render_template("dailyatt.html")


@app.route("/average", methods=['GET', 'POST'])
def average():

    if request.method == 'POST':
        fromdate = request.form['fromdate']
        todate = request.form['todate']
        rollno = request.form['rollno']
        av1 = (db.session.query(sub1).filter(sub1.date.between(fromdate, todate), sub1.attendance == 'P', rollno == rollno).count(
        ))/(db.session.query(sub1).filter(sub1.date.between(fromdate, todate), rollno == rollno).count())
        av2 = (db.session.query(sub2).filter(sub2.date.between(fromdate, todate), sub2.attendance == 'P', rollno == rollno).count(
        ))/(db.session.query(sub2).filter(sub2.date.between(fromdate, todate), rollno == rollno).count())
        av3 = (db.session.query(sub3).filter(sub3.date.between(fromdate, todate), sub3.attendance == 'P', rollno == rollno).count(
        ))/(db.session.query(sub3).filter(sub3.date.between(fromdate, todate), rollno == rollno).count())
        av4 = (db.session.query(sub4).filter(sub4.date.between(fromdate, todate), sub4.attendance == 'P', rollno == rollno).count(
        ))/(db.session.query(sub4).filter(sub4.date.between(fromdate, todate), rollno == rollno).count())
        av5 = (db.session.query(sub5).filter(sub5.date.between(fromdate, todate), sub5.attendance == 'P', rollno == rollno).count(
        ))/(db.session.query(sub5).filter(sub5.date.between(fromdate, todate), rollno == rollno).count())
        subject1 = sub1.query.filter_by(date=fromdate, rollno=rollno).all()
        subject2 = sub2.query.filter_by(date=fromdate, rollno=rollno).all()
        subject3 = sub3.query.filter_by(date=fromdate, rollno=rollno).all()
        subject4 = sub4.query.filter_by(date=fromdate, rollno=rollno).all()

        subject5 = sub5.query.filter_by(date=fromdate, rollno=rollno).all()

        return render_template("average.html", subject1=subject1, subject2=subject2, subject3=subject3, subject4=subject4, subject5=subject5, av1=av1, av2=av2, av3=av3, av4=av4, av5=av5)
    return render_template("average.html")


if __name__ == "__main__":
    app.run(debug=True)
