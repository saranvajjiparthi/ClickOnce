from flask import Flask,url_for,redirect,flash,request,render_template,session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key = "saran"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:vsvsmanikanta@localhost/signup"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db=SQLAlchemy(app)

class Result(db.Model):
    __tablename__ = "details"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    name = db.Column(db.String(50),unique=True)
    mob = db.Column(db.String(50))
    dno = db.Column(db.String(50))
    sname = db.Column(db.String(50))
    landmark = db.Column(db.String(90))
    
    

    # def __init__(self,email,password,username):
    #     self.email = email
    #     self.username = username
    #     self.password = password

    # name = db.Column(db.String(50),unique=True)
    # mob = db.Column(db.String(50))
    # dno = db.Column(db.String(50))
    # sname = db.Column(db.String(50))
    # landmark = db.Column(db.String(90))
       
    # def __init__(self,name,mob,dno,sname,landmark):
       
    #     self.name =name
    #     self.mob = mob
    #     self.dno = dno
    #     self.sname=sname
    #     self.landmark=landmark
    

@app.route('/')
def index():
    return "Homepage"


@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        # sname = request.form["sname"]
        # landmark = request.form["landmark"]
       
        # session["email"]=email
        # session["password"] = password
        # session["username"] = username
        
        

        found_user = Result.query.filter_by(username=username).first()
        if found_user:
            session["username"] = found_user.username
            flash("User Found Please Login")
            return render_template("login.html")

        else:
            if password==password:
                usr = Result(email=email,password=password,username=username)
                db.session.add(usr)
                db.session.commit()
                flash("You have Signedup Successfully")
                return redirect(url_for("signup"))        
    
    else:
        if "username" in session:
            return redirect(url_for("user"))
        return render_template("signupnew.html")
    

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        username = request.form["username"]
        
        # session["username"]=username
        # session["password"] = password
        
        found_user = Result.query.filter_by(username=username).first()
        found_user1 = Result.query.filter_by(password=password).first()

        if found_user:
            if found_user1:
                session["username"] = found_user.username
                session["password"] = found_user1.password
                return redirect(url_for("user"))
            else:
                flash("wrong password")
                return render_template("login.html")
               
        else:
            flash("sorry you don't have account create new one")
            return render_template("signupnew.html")
       
    return render_template("login.html")
 
@app.route("/user")
def user():
    if "username" in session:
        username = session["username"]
       
        return render_template("user.html",usr=username)
    else:
        return redirect(url_for("signupnew"))

@app.route("/address",methods=["POST","GET"])
def address():


    if request.method == "POST":

        name = request.form["name"]
        mob = request.form["mob"]
        dno = request.form["dno"]
        sname = request.form["sname"]
        landmark = request.form["landmark"]
        
        # session["name"]=name
        # session["mob"] = mob
        # session["dno"] = dno
        # session["sname"] = sname
        # session["landmark"] = landmark

        usr = Result(name=name,mob=mob,dno=dno,sname=sname,landmark=landmark)
        db.session.add(usr)
        db.session.commit()
        flash("Address Submitted Successfully")
        return redirect(url_for("address"))
    
    return render_template("1.html")





# class Address(db.Model):
#     __tablename__ = "address"
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(50),unique=True)
#     mob = db.Column(db.String(50))
#     dno = db.Column(db.String(50))
#     sname = db.Column(db.String(50))
#     landmark = db.Column(db.String(90))
    

    # def __init__(self,name,mob,dno,sname,landmark):
    #     self.name =name
    #     self.mob = mob
    #     self.dno = dno
    #     self.sname=sname
    #     self.landmark=landmark
       

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)