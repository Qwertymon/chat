import socket
from flask import Flask, render_template
import threading
import time




def Socket():
              global host
              host = socket.gethostbyname(socket.gethostname())
              s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              s.bind((host,8080))
              s.listen(10)
              while True:
                            con, addr = s.accept()
                            con.send("hi")
                            con.close()

l = threading.Thread(target = Socket)
l.start()
host = ''
time.sleep(0.5)
app = Flask(__name__)
@app.route('/')
def index():
              global host
              return render_template('main.html', title = host)

if __name__ == "__main__":
	app.run(port = 8080)

