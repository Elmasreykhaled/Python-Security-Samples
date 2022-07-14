import socket
ADD = input('Please Enter ip Address>> ')
PortRange=input('Please Enter port range ex : 1-10>> ')
intialPort = int(PortRange.split('-')[0])
lastlPort = int(PortRange.split('-')[1])
openPorts = []
closedPorts = []
for Port in range(intialPort,lastlPort+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    value =s.connect_ex((ADD,Port))
    if value ==0:
        openPorts.append(Port)
    else:
        closedPorts.append(Port)
    s.close()
print('The open ports are:-')
for i in range(0,len(openPorts)):
    print(openPorts[i])
print(f'There are {len(closedPorts)} Closed or filtered Ports')
