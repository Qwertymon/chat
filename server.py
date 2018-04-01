from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room
import random



chat_room_id = []


app = Flask(__name__)
app.config['SECRET-KEY'] = 'scret'
socketio = SocketIO(app)

@app.route('/')
def index():
        return render_template('main.html')

@app.route('/chatroom/<roomid>')
def chat(roomid):
        global chat_room_id
        if roomid not in chat_room_id:
                return "<h1>No such room</h1>"
        else:
                return render_template('chat.html')


        
@socketio.on('message')
def handle_maessage(msg):
        global chat_room_id
        if msg == "room":
                letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                key = ''
                for i in range(0,8):
                        key += random.choice(letters)
                chat_room_id.append(key)
                emit("key",key)
        else:
                room = msg[-9:-1]
                print room
                emit(room,msg[0:-9], broadcast = True)

if __name__ == '__main__':
        socketio.run(app)
