from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret!'

socket_io = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@socket_io.on('connect')
def connect():
    """
    聊天建立连接
    """
    app.logger.debug('connected')
    emit('debug', {'data': 'Connected.'})


@socket_io.on('disconnect')
def disconnect():
    """
    聊天断开连接
    """
    app.logger.debug('disconnected')
    emit('debug', {'data': 'Disconnect.'})


@socket_io.on('message')
def handle_message(message):
    app.logger.info(message)


@socket_io.on('my event')
def handle_my_custom_event(json):
    app.logger.info('received json: ' + str(json))


if __name__ == '__main__':
    socket_io.run(app, port=8000)
