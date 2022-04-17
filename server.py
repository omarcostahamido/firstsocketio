import socketio
import eventlet

print("Hello Fly.io!")

# IP = "fly-global-services"
IP = "127.0.0.1"
PORT = 5000

sio = socketio.Server(async_mode='eventlet',cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
	print('new connection: ', sid)

@sio.event
def Client(sid, *data):
	print("received message from client:",sid)
	print("the contents of the message were:",*data)

@sio.event
def disconnect(sid):
	print('disconnected from: ', sid)

eventlet.wsgi.server(eventlet.listen((IP, PORT)), app)

print("this should not print")
