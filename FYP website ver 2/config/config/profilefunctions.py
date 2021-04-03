import json
import os

def clear(): 
    # for windows 
    if os.name == 'nt': 
        os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        os.system('clear') 

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
        print("[6] Back to menu")
    
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
        elif(selection == '6'): #Return to menu
            clear()
            return 
        else :
            print("Incorrect input try again !")
            input('Press any key to continue....')
        clear()

#Displays the profiles available
def profile():
    while(1):
        print("----------Scan Profiles-----------")
        print("[1] Web Application Scan")
        print("[2] Full Audit Scan")
        print("[3] Server Scan")
        print("[4] SQL Injection scan")
        print("[5] Profile Descriptions")
        print("[6] Back to menu")
    
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
        elif(selection == '6'): #Return to menu
            clear()
            return 
        else :
            print("Incorrect input try again !")
            input('Press any key to continue....')
        clear()

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
    print("\n")
    input("Press enter to continue.......")