from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu_secreto_aqui'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('url.html')

@socketio.on('message')
def handle_message(message):
    print('Mensagem recebida: ' + message)
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
