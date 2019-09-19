#import os
#import sys
#from yolo import yolo
import numpy as np
import argparse
import cv2 as cv
import subprocess
import time
import os
import yoloc
from threading import Lock
from yolo_utils import infer_image, show_image
import dateutil.parser
from camera import VideoCamera,VideoCamera2

from flask import Flask, render_template,request,session,redirect,Response
#from flask_adminlte import AdminLTE
from flask_mysqldb import MySQL


#sys.path.append(os.path.dirname(__name__))
from flask_cors import CORS
#from yolo import yolo

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
	
	
# create an app instance
#app = create_app()

#app.run(debug=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

thread = None
thread_lock = Lock()
async_mode = None
frame=None
socketio = SocketIO(app, async_mode=async_mode)



CORS(app)

def startVideo():
    print("Video func")
    vid = cv.VideoCapture("./hw.mp4")
    count=0
    bb1=None
    while True:
        _, frame = vid.read()
        if (count%5==0):
            y=yoloc.yolo(frame,count,bb1)
            print(type(y))
            print(y)
            lis=np.array(y).tolist()
            #for i in range(10):
            #listY = y#.tolist()
            print("Sart list")
            print(lis)
            print("End list")
            print(type(lis))
            socketio.sleep(0.3)
            socketio.emit('video_data', {'data': [lis]})
            #socketio.emit('video_data', {'data': [12,12,12,listY]})
            #emit('response_from_backend', {'data': str(y) + ' ' + 'working', 'count': '2'})
            if count==0:
                bb1=y
            #count=count+1
        count=count+1
        

        

        cv.imshow('webcam', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
                break
    vid.release()
    cv.destroyAllWindows()


@app.route('/vido')
def vido():
    return render_template('vido.html')

@app.route('/boxesvideo')
def boxesvideo():
    return render_template('boxesvideo.html')


@app.route('/boxesvideo1')
def boxesvideo1():
    return render_template('boxesvideo1.html')

@app.route('/boxesvideo2')
def boxesvideo2():
    return render_template('boxesvideo2.html')

@app.route('/boxesvideo3')
def boxesvideo3():
    return render_template('boxesvideo3.html')


def gen(camera):
    #count=0
    bb1=[]
    
    while True:
        
        frame,bb1 = camera.get_frame(bb1)
        #if count==0:
        #    bb1=
        #count=count+1
        #out.write(frame)
        print("frame")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen2(camera):
    #count=0
    bb1=[]
    
    while True:
        
        frame,bb1 = camera.get_frame(bb1)
        #if count==0:
        #    bb1=
        #count=count+1
        #out.write(frame)
        print("frame")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed2')
def video_feed2():
    return Response(gen(VideoCamera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.before_first_request
def startup():
    print("hello")

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
            userdetails = request.form
            name = userdetails['name']
            password = userdetails['password']
            cur = mysql.connection.cursor()
            #cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT * FROM record where name=%s and password = %s",(name,password))
            row = cur.fetchall()
            if (len(row)==0):
                return redirect('/login2')
            else:
                return redirect('/startcamera')
            mysql.connect.commit()
            cur.close()
        
    return render_template('login2.html')
    #socketio.run(app, port=6565, debug=True)
#    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/livevideo')
def livevideo():
    if request.method=='POST':
        return redirect('/vido')
    #socketio.run(app, port=6565, debug=True)
    return render_template('livevideo.html', async_mode=socketio.async_mode)

#app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'criminal'

mysql = MySQL(app)





@app.route('/login2', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
            userdetails = request.form
            name = request.form['name']
            password = userdetails['password']
            cur = mysql.connection.cursor()
            #cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT name,password FROM record where name=%s and password = %s",(name,password))
            row = cur.fetchall()
            if (len(row)==0):
                return redirect('/login2')
            else:
                return redirect('/startcamera')
            mysql.connect.commit()
            cur.close()
            #return redirect('/')

        return render_template('login2.html')



@app.route('/register2',methods=['GET','POST'])
def register2():
        #cur = mysql.connection.cursor()
        if request.method == 'POST':
            userdetails = request.form
            name = userdetails['name']
            password = userdetails['password']
            email=userdetails['email']
            phone=userdetails['phone']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO record(name,password,email,phone) VALUES(%s,%s,%s,%s)", (name, password,email,phone))
            mysql.connect.commit()
            cur.close()
            return redirect('/login2')

        return render_template('register2.html')

@app.route('/startcamera',methods=['GET','POST'])
def startcamera():
        if request.method=='POST':
            return redirect('/livevideo')

    
        return render_template('startcamera.html')




@socketio.on('send_event_to_backend')
def test_message(message):
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(startVideo)
    #emit('response_from_backend', {'data': "asdad" + ' ' + 'working', 'count': '2'})

    
    #for i in range(10):
    

#emit('my_response', {'data': 'server response'})

		 
@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected'})



		 

#if __name__ == '__main__':
def startvideo():
    print("Main")
    socketio.run(app, port=6567, debug=True)

startvideo()
