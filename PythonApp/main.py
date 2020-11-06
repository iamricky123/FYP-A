from arachni import *
import time
import json
import os


def clear(): 
    # for windows 
    if os.name == 'nt': 
        os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        os.system('clear') 

#For authenticated scan
def auth_scan_parameters(URL, user, _pass):
    file1 = open('./profiles/Authenticated/' + get_Profile() + '.json', 'r') #open to get data from the json file
    data = json.load(file1)
    file1.close()
    data["plugins"]["autologin"]["url"] = URL
    data["plugins"]["autologin"]["parameters"] = 'email='+user+'&password='+_pass
    file1 = open('./profiles/Authenticated/' + get_Profile() + '.json', 'w') #open file to update the values
    json.dump(data, file1, indent=4)
    file1.close()

#Get current selected profile from json file 
def get_Profile():
    file = open('./input/input.json', 'r')#open input json file 
    data = json.load(file)
    profile_Data = data["profile"]  #input selected profile
    file.close()
    return profile_Data
  
#Function to return the name of the profile 
def print_profile():
    prof = get_Profile()
    if(prof == "webapp"):
        return "Web Application Scan"
    elif(prof== "full_audit"):
        return "Full Audit Scan"
    elif(prof== "server"):
        return "Server Scan"
    else:
        return "SQL injection scan"

#Record which profile is in use
def edit_profile(insert_prof):
    file = open('./input/input.json', 'r')#open input json file 
    data = json.load(file)
    data["profile"] = insert_prof #input selected profile
    file.close()

    file = open('./input/input.json', 'w')
    json.dump(data,file, indent = 4)#write into json file
    file.close()

#Displays the profiles available
def profile():
    while(1):
        print("----------Scan Profiles-----------")
        print("[1] Web Application Scan")
        print("[2] Full Audit Scan")
        print("[3] Server Scan")
        print("[4] SQL Injection scan")
        print("[5] Profile Descriptions")
    
        selection = input("Select one scan profile :")
        if(selection == '1'):
            profile_name = 'webapp'
            edit_profile(profile_name)
            clear()
            return profile_name
        elif(selection == '2'):
            profile_name = 'full_audit'
            edit_profile(profile_name)
            clear()
            return profile_name
        elif(selection == '3'):
            profile_name = 'server'
            edit_profile(profile_name)
            clear()
            return profile_name
        elif(selection == '4'):
            profile_name = 'sql_injection'
            edit_profile(profile_name)
            clear()
            return profile_name
        elif(selection == '5'):
            profile_descriptions()
        else :
            print("Incorrect input try again !")
            input('Press any key to continue....')

#Explanation on the profiles
def profile_descriptions():
    print("Web Application Scan")
    print("-----------------------")
    print("The web application scan focuses on the vulnerabilities of the web application such as XSS attacks, brute force and CSRF")
    print("\n")
    print("Server Scan")
    print("-----------------------")
    print("The server scan does checks such as backdoors, directories, files and mixed resources")
    print("\n")
    print("SQL Injection scan")
    print("-----------------------")
    print("SQL Injection sql is a injection attack which control database server behind the web application")
    print("\n")
    print("Full Audit scan")
    print("-----------------------")
    print("Performs a full scan on the web application including server side and databases")


#Prompts user for URL and saved in the json file for other functions to reference
def userInput():
    URL = input('Please insert the URL of the Web Application :')
    #open json file to get data
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()

    #userinput inserted into the json file
    data["url"] = URL
    jsonOpen = open('./input/input.json', 'w')
    json.dump(data, jsonOpen, indent=4)
    jsonOpen.close
    return URL

#Gets the current scan ID from the json file
def get_ID():
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()
    if(data["scan_id"] != None):
        _id = data["scan_id"]
        return _id
    else:
        print('No Scan ID found !')

#Starts the scan
def start_scan(in_client,auth):
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    url = data["url"]
    profile = data["profile"]
    jsonOpen.close()

    if(auth):
        in_client.profile('./profiles/Authenticated/'+ get_Profile() + '.json')
        in_client.target(url) # set target url
        container = in_client.start_scan()
        jsonOpen2 = open('./input/input.json', 'w')
        _id = container.get("id")
        data["scan_id"] = _id
        json.dump(data, jsonOpen2, indent=4)
        jsonOpen2.close()
    else:
        in_client.profile('./profiles/Non-authenticated/'+ get_Profile() + '.json')
        in_client.target(url) # set target url
        container = in_client.start_scan()
        jsonOpen2 = open('./input/input.json', 'w')
        _id = container.get("id")
        data["scan_id"] = _id
        json.dump(data, jsonOpen2, indent=4)
        jsonOpen2.close()


#Prints the menu for the user to select
def print_menu():
        print("****************************************************")
        print("Vulnerability Scanner")
        print("****************************************************")
        print("1.Start Scanning")
        print("2.Change Scanning Settings")
        print("Current selected profile : ", print_profile())

#Function incharge of prompting and process the user input
def menu():
    while(1):
        choice = input("Please input your choice :")
        clear()
        if(choice == '1'):
            while(1):
                select = input('Do you want to customize your scannning profile ? [Y/N] : ')
                if(select == 'Y' or select =='y' or select =='Yes' or select =='YES'):
                    clear()
                    return 2
                elif(select == 'N' or select =='n' or select =='No' or select =='NO'):
                    clear()
                    return 1
                else :
                    print("Invalid input... Try again")
                    input("Press any key to continue...")
                    clear()
        elif(choice == '2'):
            clear()
            return 2
        else:
            print("Invalid input... Try again")
            input("Press any key to continue...")
            clear()
 
#Process the input from the user
def process(client, choice):
    if(choice == '1'):
        start(client)
        return
    elif(choice == '2'):
        return
    else:
        profile_select = profile()
        return profile_select

#Ask user if they want to do authenticated scanning
def authenticate():
    while(1):
        auth_scan = input('Authenticated scanning [y/n]? :')
        if(auth_scan == 'Y' or auth_scan == 'y' or auth_scan == 'Yes' or auth_scan == 'YES'):
            return True
        elif(auth_scan ==  'N' or auth_scan =='n' or auth_scan =='No' or auth_scan =='NO'):
            return False
        else:
            print("Invalid input... Try again")
            input("Press any key to continue...")
            clear()
    return True



def main():
    client = ArachniClient()
    while(1):
        print_menu()
        start = menu()
        if(start != 1):
            profile = process(client, start)
        else:
            break
    url = userInput()
    auth = authenticate()
    if(auth):
        username = input("Input username :")
        password = input("Password :")
        auth_scan_parameters(url, username, password)
        start_scan(client, auth)
        while(1):
            if(client.get_report(get_ID(), 'xml') == None and client.get_status(get_ID())["busy"] == True):
                time.sleep(10)
            else:
                print(client.get_status(get_ID()))
                print(client.get_report(get_ID(), 'xml'))
                b = client.get_report(get_ID(), 'xml')
                b = b + "<link rel='stylesheet' href='mystyle.css'>"
                b = b + "<title>scanning report</title>"
                b = "<h1>scanning report</h1>" + b
                c = open("reporttesthtml.html","w")
                c.write(b)
                c.close()
                f.close()
                break
        
    else:
        start_scan(client, auth)
        while(1):
            if(client.get_report(get_ID(), 'xml') == None):
                time.sleep(10)
            else:
                print(client.get_status(get_ID()))
                print(client.get_report(get_ID(), 'xml'))
                b = client.get_report(get_ID(), 'xml')
                b = b + "<link rel='stylesheet' href='mystyle.css'>"
                b = b + "<title>scanning report</title>"
                b = "<h1>scanning report</h1>" + b
                c = open("reporttesthtml.html","w")
                c.write(b)
                c.close()
                f.close()
                break

            
main()
