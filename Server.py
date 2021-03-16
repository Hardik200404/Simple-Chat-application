import socket
s=socket.socket()
s.bind(('localhost',2040))
s.listen(2)
print('Listening,waiting for connection')
while True:
    c,add=s.accept()#we will receive two parameters,when a client connects(connection and address) 
    n=c.recv(1024).decode()
    print("Connected :",n,"\nAdress:",add)
    c.send(bytes('Welcome to server','utf-8'))
    while True:                                #chat box
        msg=c.recv(1024).decode()
        print("client:",msg)
        if msg=="Connection closed by client":
            break
        m=input("server:")
        if m=="close":
            c.send(bytes('Connection closed by the server','utf-8'))
            break
        c.send(bytes(m,'utf-8'))
    break
print("connection lost")    
c.close()