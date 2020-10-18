from arachni import *
import time


#URL = input("Please insert the URL of the Web Application :")
url = raw_input('Please insert the URL of the Web Application :')

f = open("id.txt", "w+")
f.write(url)
f.close()

client = ArachniClient()
client.profile('./profiles/default.json')
execfile("PythonApp.py") #get scan ID

f = open("id.txt", "r")
readFile = f.readlines()
getID = readFile[0]

while(1):
    if(client.get_report(getID, 'xml') == None):
        print("Scanning In Progress .....")
        time.sleep(10)
    else:
        print(client.get_status(getID))
        print(client.get_report(getID, 'xml'))
        b = client.get_report(getID, 'xml')
        b = b + "<link rel='stylesheet' href='mystyle.css'>"
        b = b + "<title>scanning report</title>"
        b = "<h1>Scanning Report</h1>" + b
        c = open("reporttesthtml.html","w")
        c.write(b)
        c.close()
        f.close()
        break
