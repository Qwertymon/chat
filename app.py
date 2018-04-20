from flask import Flask, render_template
import socket

host = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)
@app.route('/')
def index():
    global host
    return render_template('main.html', title = host)

if  __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
