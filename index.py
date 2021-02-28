from flask import *
import pymysql as p 
from Student_DBM import insertData,getConnection,selectAllData,delete,selectAllDataByID,updateData

f = Flask(__name__)
f.secret_key='asdsdfsdfs13sdf_df%&'

@f.route("/")
def index():
    return render_template("index.html")

@f.route("/update_student", methods = ["POST"])
def update_student():
    id = request.form['id']
    rollno = request.form["rollno"]
    name = request.form["name"]
    contact = request.form["contactno"]
    email = request.form["email"]
    college = request.form["college"]
    address = request.form["address"]
    password = request.form["password"]
    t =(rollno,name,contact,email,college,address,password,id)
    updateData(t)
    return redirect("/showList")

@f.route("/home")
def home():
    if session.get('username') is None:
        return redirect(url_for('index'))
    else:
        return render_template("home.html")


@f.route("/showList")
def showlist():
    if session.get('username') is None:
        return redirect(url_for('index'))
    else:
        studentsList = selectAllData()
        return render_template("showList.html", students=studentsList)

@f.route("/deleteStudent")
def deleteStudent():
    if session.get('username') is None:
        return redirect(url_for('index'))
    else:
        id = request.args.get('id')
        delete(id)
        return redirect("/showList")
    

@f.route("/editStudent")
def editStudent():
    if session.get('username') is None:
        return redirect(url_for('index'))
    else:
        id = request.args.get('id')
        getStudentById = selectAllDataByID(id)
        return render_template("updateStudent.html", getData=getStudentById)


@f.route("/reg")
def register():
    if session.get('username') is None:
        return redirect(url_for('index'))
    else:
        return render_template("register.html")


@f.route("/check_user", methods = ["POST"])
def checkUser():
    email = request.form["email"]
    password = request.form["password"]
    db = getConnection()
    cr = db.cursor()
    cr.execute("select * from admin where email = '"+email+"' AND password = '"+password+"'")
    user=cr.fetchone()
    if user is not None:
        session['username'] = user[3]
        return redirect(url_for('home'))
    else:
        return """
        <h1 style='color:red'>You have entered wrong email or password or maybe both</h1>
        <h1 style='color:red'>please try again later</h1>
        <a href="/" style="text-decoration: none; color: white; border: 1px solid; background-color: blue; padding: 12px; margin: 20px; border-radius: 7px;">Login Again</a>
        """

@f.route("/add_student", methods = ["POST"])
def add_student():
    if session.get('username') is None:
        return redirect(url_for('index'))
    else:
        rollno = request.form["rollno"]
        name = request.form["name"]
        contact = request.form["contactno"]
        email = request.form["email"]
        college = request.form["college"]
        address = request.form["address"]
        password = request.form["password"]
        t =(rollno,name,contact,email,college,address,password)
        insertData(t)
        return render_template("home.html")


@f.route ("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    f.run (debug = True)
