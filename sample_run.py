#import os
#import sys
#from yolo import yolo


#sys.path.append(os.path.dirname(__name__))
from flask_cors import CORS
from yolo import yolo

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
	
	
# create an app instance
#app = create_app()

#app.run(debug=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

CORS(app)

@app.before_first_request
def startup():
    print("hello")


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_event_to_backend')
def test_message(message):
    y=yolo.yolo()
    print(y)
    #for i in range(10):
    emit('response_from_backend', {'data': str(y) + ' ' + 'working', 'count': '2'})

#emit('my_response', {'data': 'server response'})

		 
@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected'})



		 

if __name__ == '__main__':
    socketio.run(app, debug=True, port=6569)		 
