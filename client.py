import socket
ADD = input('please Enter the sever address>> ')
PORT = int(input('please Enter the server port>> '))
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADD,PORT))
print('connection established')
message = input('Please input your message>> ')
s.sendall(message.encode())
print('Message sent')
s.close()
