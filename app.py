import socket
from flask import Flask
import threading



def meme():
              global host
              s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              host = socket.gethostbyname(socket.gethostname())
              s.bind(("0.0.0.0",8080))
              s.listen(10)
              f = open("log.txt","w")
              f.write(str(host)+" listeniing")
              f.close()
              while True:
                            con, addr = s.accept()
                            f1 = open("clients.txt","w")
                            f1.write(str(addr))
                            f1.close()
                            con.send("LOL")
                            con.close()
              s.close()
host = ''
              
tor = threading.Thread(target = meme)
tor.start()

app = Flask(__name__)
@app.route('/')
def index():
   global host
   return host

if __name__ == "__main__":
   app.run()
