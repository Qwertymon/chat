import socket
import threading
from flask import Flask



host_ip = ''
chk_server = "false"

def server():
    global host_ip, chk_server
    host_ip = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host_ip,8080))
    s.listen(10)
    chk_server = "True"
    while True:
        con, addr = s.accept()
        con.send("good")
        con.close()

t = threading.Thread(target = server)
t.start()

app = Flask(__name__)
@app.route('/')
def index():
    global  host_ip, chk_server
    return str(host_ip)+" "+str(chk_server)

if __name__ == "__main__":
    app.run()
