import dateutil.parser

from flask import Flask, render_template,request,session,redirect
from flask_adminlte import AdminLTE
from flask_mysqldb import MySQL
from sample_application import yolo
#from sample_application import hi




class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "Fusion Informatics"
    avatar = "/static/img/fusion.jpg"
    created_at = dateutil.parser.parse("November 12, 2016")



def create_app(configfile=None):
    app = Flask(__name__)
    AdminLTE(app)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'criminal'

    mysql = MySQL(app)

    # This is a placeholder user object.  In the real-world, this would
    # probably get populated via ... something.
    current_user = User()

    @app.route('/')
    def index():
        #h=hi.hii()
        yolo.yolo()
        return render_template('index.html', current_user=current_user)

   # @app.route('/login',methods=['POST'])
   # def login():
    #    if request.form['password'] == 'password' and request.form['username'] == 'admin':
     #            session['logged_in'] = True
      #  return render_template('login.html',current_user=current_user)

    @app.route('/login', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            userdetails = request.form
            name = userdetails['username']
            password = userdetails['password']
            cur = mysql.connection.cursor()
            #cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT * FROM record where name=%s and password = %s",(name,password))
            row = cur.fetchall()
            if (len(row)==0):
                return redirect('/login')
            else:
                return redirect('/')
            mysql.connect.commit()
            cur.close()
            #return redirect('/')

        return render_template('login.html')

    @app.route('/register',methods=['GET','POST'])
    def register():
        #cur = mysql.connection.cursor()
        if request.method == 'POST':
            userdetails = request.form
            name = userdetails['username']
            password = userdetails['password']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            mysql.connect.commit()
            cur.close()
            return redirect('/login')

        return render_template('register.html')

    @app.route('/pending')
    def pending():
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM pending WHERE grade='pending'")
        if result > 0:
            userdetail = cur.fetchall()
            # return "hello"
            #return render_template('user.html', userdetail=userdetail)
            return render_template('pending.html', userdetail=userdetail,current_user=current_user)
        return render_template('pending.html', current_user=current_user)

    @app.route('/completed')
    def completed():
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM pending WHERE grade='completed'")
        if result > 0:
            userdetail = cur.fetchall()
            # return "hello"
            # return render_template('user.html', userdetail=userdetail)
           # return render_template('pending.html', userdetail=userdetail, current_user=current_user)
            return render_template('completed.html', current_user=current_user,userdetail=userdetail)
        return render_template('completed.html', current_user=current_user)

    @app.route('/parsedwitherror')
    def parsedwitherror():
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM pending WHERE grade='parsedwitherrror'")
        if result > 0:
            userdetail = cur.fetchall()
            # return "hello"
            # return render_template('user.html', userdetail=userdetail)
            # return render_template('pending.html', userdetail=userdetail, current_user=current_user)
            return render_template('parsedwitherror.html', current_user=current_user, userdetail=userdetail)
        return render_template('parsedwitherror.html', current_user=current_user)

        #return render_template('parsedwitherror.html', current_user=current_user)

    @app.route('/lockscreen')
    def lockscreen():
        return render_template('lockscreen.html', current_user=current_user)


    @app.route('/add_resume')
    def add_resume():
        print("hi")
        return render_template('add_resume.html', current_user=current_user)


    @app.route('/search')
    def search():
        return render_template('search.html', current_user=current_user)


    @app.route('/Rocdetails')
    def Rocdetails():
        return render_template('Rocdetails.html', current_user=current_user)

    @app.route('/modeldetails')
    def modeldetails():
        return render_template('modeldetails.html', current_user=current_user)

    return app
    def hello():
        yolo.yolo()
        return "hello"

if __name__ == '__main__':
    add_resume()
    create_app().run(debug=True)
