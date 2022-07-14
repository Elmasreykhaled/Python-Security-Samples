import socket
ADD = input('please Enter the sever address>> ')
PORT = int(input('please Enter the server port>> '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADD,PORT))
s.listen(1)
print('server created successfuly and waiting for connection')
connection,address = s.accept()
print('Client Connected With addrss ', address)
while 1:
    data = connection.recv(1024)
    if not data : break
    connection.sendall(b'Message Recived\n')
    print(data.decode('utf-8'))
connection.close()