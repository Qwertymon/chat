import socket

host = socket.gethostbyname(socket.gethostname())
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
f = open("file.txt",'w')
f.write("created "+str(host))
f.close()

s.close()
