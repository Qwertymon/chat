import socket
from flask import Flask



host_ip = ''


host_ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)
@app.route('/')
def index():
    global  host_ip
    return str(host_ip)

if __name__ == "__main__":
    app.run(host = host_ip, port = 8080)
