import socket
from flask import Flask, render_template
import threading





def Socket():
	host = socket.gethostbyname(socket.gethostname())
	s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,8080))
	s.listen(10)
	print "Server start"
	while True:
		con, addr = s.accept()
		con.send("hi")
		con.close()

l = threading.Thread(target = Socket)
l.start()


app = Flask(__name__)
@app.route('/')
def index():
	host = socket.gethostbyname(socket.gethostname())
	return render_template('main.html', title = host)

host = socket.gethostbyname(socket.gethostname())
print host
if __name__ == "__main__":
	app.run(port = 8080)
