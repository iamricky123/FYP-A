from arachni import *
import time
import json


def auth_scan_parameters(URL, user, _pass, profile):
    file1 = open('./profiles/' + profile + '.json') #open to get data from the json file
    data = json.load(file1)
    file1.close()
    data["plugins"]["autologin"]["url"] = URL
    data["plugins"]["autologin"]["parameters"] = 'email='+user+'&password='+_pass
    file1 = open('./profiles/' + profile + '.json', 'w') #open file to update the values
    json.dump(data, file1, indent=4)
    file1.close()

    file2 = open('./input/input.json', 'r')
    data2 = json.load(file2)
    data2["profile"] = profile
    file2.close()

    file2 = open('./input/input.json', 'w')
    json.dump(data2,file2, indent = 4)
    file2.close()

def print_profile():
    print("----------Scan Profiles-----------")
    print("[1] Default scan")
    print("[2] Full audit scan")
    print("[3] XSS scan")
    print("[4] SQL Injection scan")

    while(1):
        selection = input("Select one scan profile :")
        if(selection == 1):
            return 'default'
        elif(selection == 2):
            return 'fullaudit'
        elif(selection == 3):
            return 'xss'
        elif(selection == 4):
            return 'sqlinjection'
        else :
            print("Incorrect input try again !")


##def startscan(useClient, _url):
##    useClient.profile('./profiles/default.json')
##    useClient.target(_url) # set target url
##    container = useClient.start_scan()
##    _id = container.get('id')
##    return _id

def userInput(URL):
    #open json file to get data
    jsonOpen = open('./input/input.json')
    data = json.load(jsonOpen)
    jsonOpen.close()

    #userinput inserted into the json file
    data["url"] = URL
    jsonOpen = open('./input/input.json', 'w')
    json.dump(data, jsonOpen, indent=4)
    jsonOpen.close

def get_ID():
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()
    if(data["scan_id"] != None):
        _id = data["scan_id"]
        return _id
    else:
        print('No Scan ID found !')
    

def main():
    client = ArachniClient()
    url = raw_input('Please insert the URL of the Web Application :')
    userInput(url)
    auth_scan = raw_input('Authenticated Scanning [Y/N]? :')
    if(auth_scan == 'Y' or auth_scan == 'y'):
        username = raw_input("Input username :")
        password = raw_input("Password :")
        profile = 'default'
        auth_scan_parameters(url, username, password, profile)
        execfile('PythonApp.py')
        getID = get_ID()
        while(1):
            if(client.get_report(getID, 'xml') == None and client.get_status(getID)["status"] != 'aborted'):
                print("Scanning In Progress .....")
                time.sleep(10)
            elif(client.get_status["status"] != 'aborted'):
                print("Scan has been aborted")
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
        
        else:
            getID = getID()
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
                
main()
                
