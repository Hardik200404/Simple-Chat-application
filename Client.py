import socket
c=socket.socket()
c.connect(('localhost',2040))
name=input("Enter name :")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())
while True:
    msg=input("client:")
    if msg=="close":
        c.send(bytes('Connection closed by client','utf-8'))
        break
    c.send(bytes(msg,'utf-8'))
    m=c.recv(1024).decode()
    if m=="Connection closed by the server":
        print(m)
        break
    print("server:",m)
print("Connection lost")
c.close()
