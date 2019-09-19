import os
import sys
import yolo


sys.path.append(os.path.dirname(__name__))
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
	
	
# create an app instance
#app = create_app()

#app.run(debug=True)

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

@app.before_first_request
def startup():
    print("hello")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print('message was received!!!')
    emit('my_response',
         {'data': 'server response'})

		 
@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)



@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected'})



def main():
    print("helo")
		 

if __name__ == '__main__':
    main()
    socketio.run(app, debug=True, port=6565)		 
