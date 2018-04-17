import socket
from flask import Flask
import  threading 



globalhost = ''
gloabalk = "flase"


def sockett():
        global globalhost, gloabalk
        
        host = socket.gethostbyname(socket.gethostname())
        globalhost = host
        port = 8080
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen(10)
        gloabalk = "true"
        while True:
                con, addr = s.accept()
                con.send("Nope")
                con.close()
        s.close()

t = threading.Thread(target = sockett)
t.start()

app = Flask(__name__)
@app.route('/')
def index():
        global globalhost, gloabalk
        return  str(globalhost)+" "+str(gloabalk)

if  __name__ == "__main__":
        app.run()
