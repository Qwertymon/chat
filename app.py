import socket
from flask import Flask
import  threading 



globalhost = ''
gloabalk = "flase"



app = Flask(__name__)
@app.route('/')
def index():
        global globalhost, gloabalk
        return  "sdf"

if  __name__ == "__main__":
        app.run()
