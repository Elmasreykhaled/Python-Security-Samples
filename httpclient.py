import http.client
host = input('Please Enter the hostname host/ip>> ')
port = input('Please Enter the port (default=80)>> ')
path = input('Please Enter the path (/ex)>> ')
if port == "":
    port = 80
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', path)
    response = connection.getresponse()
    statusCode = response.status
    if statusCode in range(100, 200):
        print('information response')
    elif statusCode in range(200, 300):
        print('Successful')
    elif statusCode in range(300, 400):
        print('redirect')
    elif statusCode in range(400, 500):
        print('Client error')
    else:
        print('server error')
    connection.close()
except ConnectionRefusedError:
    print('connection Error')
