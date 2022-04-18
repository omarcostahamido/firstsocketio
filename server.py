import socketio
import eventlet
import argparse

print("Hello Fly.io!")

IP = "0.0.0.0"
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
	sio.emit('response', data, room=sid)

@sio.event
def disconnect(sid):
	print('disconnected from: ', sid)


if __name__ == '__main__':

	p = argparse.ArgumentParser()

	p.add_argument('port', type=int, nargs='?', default=5000, help='The port where the server.py will listen for incoming messages. Default port is 5000')

	args = p.parse_args()

	PORT = args.port

	print("getting ready to start server at",IP,PORT)

	eventlet.wsgi.server(eventlet.listen((IP, PORT)), app)

	print("this should not print")