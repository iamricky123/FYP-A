from django.shortcuts import render,redirect
import requests, sys, webbrowser, smtplib, os, json, socket, nmap
from subprocess import run,PIPE #,Popen
from django.contrib import messages
from .arachni import *
import xml.etree.ElementTree as ET
from datetime import datetime as datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path
from accounts.models import UserReport, SaveScanID, UserPortReport
from datetime import date
from urllib.request import urlparse

jsonscan = (os.path.dirname(__file__) + "\input\input.json")
authscan = (os.path.dirname(__file__) + "\profiles\Authenticated/")
nonauthscan = (os.path.dirname(__file__) + "\profiles\ScanNon-authenticated/")
solreport = (os.path.dirname(__file__) + "\solution.xml")

# Create your views here.
def portscanscript(request):
    portscanweb = request.POST.get('param')
    portscandate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        if(filterinput(portscanweb) == None):
            target = socket.gethostbyname(portscanweb)
        else:
            target = socket.gethostbyname(filterinput(portscanweb))
        nm = nmap.PortScanner()
        nm.scan(target,'1-500')
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols(): #get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
                lport = nm[host][proto].keys() #get all ports for tcp/udp protocol
                for port in sorted(lport):
                    saveportrecord = UserPortReport()
                    saveportrecord.date = portscandate
                    saveportrecord.host_data = target + "[" + portscanweb + "]"
                    saveportrecord.state = nm[host].state()
                    saveportrecord.protocol = port
                    saveportrecord.email = request.user
                    saveportrecord.save() 
    except:
        messages.error(request, 'Could not connect to host, try again')
        return render(request, 'home.html')
    
    return redirect('portscan_redirect/')  

def filterinput(input):
   x = urlparse(input)
   return x.hostname





def start_scan(in_client,auth):
    jsonOpen = open(jsonscan, 'r')
    data = json.load(jsonOpen)
    url = data["url"]
    profile = data["profile"]
    jsonOpen.close()

    if(auth):
        in_client.profile(authscan + get_Profile() + '.json')
        in_client.target(url) # set target url
        container = in_client.start_scan()
        jsonOpen2 = open(jsonscan, 'w')
        _id = container.get("id")
        data["scan_id"] = _id
        json.dump(data, jsonOpen2, indent=4)
        jsonOpen2.close()
    else:
        in_client.profile(nonauthscan + get_Profile() + '.json')
        in_client.target(url) # set target url
        container = in_client.start_scan()
        jsonOpen2 = open(jsonscan, 'w')
        _id = container.get("id")
        data["scan_id"] = _id
        json.dump(data, jsonOpen2, indent=4)
        jsonOpen2.close()


def auth_scan_parameters(URL, user, _pass, user_param, pass_param):
    file1 = open(authscan + get_Profile() + '.json', 'r') #open to get data from the json file
    data = json.load(file1)
    file1.close()
    data["plugins"]["autologin"]["url"] = URL
    data["plugins"]["autologin"]["parameters"] = user_param+'='+user+'&'+pass_param+'='+ _pass
    file1 = open(authscan + get_Profile() + '.json', 'w') #open file to update the values
    json.dump(data, file1, indent=4)
    file1.close()

def userInput(URL):
    jsonOpen = open(jsonscan, 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()

    #userinput inserted into the json file
    data["url"] = URL
    jsonOpen = open(jsonscan, 'w')
    json.dump(data, jsonOpen, indent=4)
    jsonOpen.close
    return URL

def get_ID():
    jsonOpen = open(jsonscan, 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()
    if(data["scan_id"] != None):
        _id = data["scan_id"]
        return _id
    else:
        print('No Scan ID found !')

def get_Profile():
    file = open(jsonscan, 'r')#open input json file 
    data = json.load(file)
    profile_Data = data["profile"]  #input selected profile
    file.close()
    return profile_Data

def edit_profile(insert_prof):
    file = open(jsonscan, 'r')#open input json file 
    data = json.load(file)
    data["profile"] = insert_prof #input selected profile
    file.close()

    file = open(jsonscan, 'w')
    json.dump(data,file, indent = 4)#write into json file
    file.close()



def url_in(insert_url):
    URL = insert_url
    #open json file to get data
    jsonOpen = open(jsonscan, 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()

    #userinput inserted into the json file
    data["url"] = URL
    jsonOpen = open(jsonscan, 'w')
    json.dump(data, jsonOpen, indent=4)
    jsonOpen.close
    return URL

def generateReport(request, website, scan_id, scan_select):
    report_tree = ET.parse('reporthtml.xml')
    report_root = report_tree.getroot()
    solution_tree = ET.parse(solreport)
    solution_root = solution_tree.getroot()
    today = date.today()
    reportName = str(today)+"_ScanningReport.html"
    scan_id_1 =""

    if (report_root.text == 'None'):
        f = open(reportName,"w")
        f.write("<html lang='en'>")
        f.write("<head>")
        f.write("<link rel='stylesheet' href='mystyle1.css'>")
        f.write("</head>")
        f.write("<body>")
        f.write("<div class='report'>")
        f.write("<h1>Scanning Report</h1>")
        f.write("<p class='name'>None</p>")
        f.write("</div>")
        f.write("</body>")
        f.write("</html>")
        f.close()
    else:
        f = open(reportName,"w")
        f.write("<html lang='en'>")
        f.write("<head>")
        f.write("<link rel='stylesheet' href='mystyle1.css'>")
        f.write("</head>")
        f.write("<body>")
        f.write("<div class='report'>")
        f.write("<h1>Scanning Report</h1>")
        f.write("<p class='name'>Issue(s) Found</p>")
        f.write("<p class='description'>Issue(s) Description</p>")
        f.write("<p class='solution'>Remedy Guidance</p>")
        f.write("<p class='url'>Issue(s) Site</p>")

        for report1 in report_root:
            for report2 in report1:
                for report3 in report2:
                    for report4 in report2.findall('description'):
                        for report5 in report3.findall('name'):
                            report_description = report4.text
                            report_name = report5.text
                            for report6 in report2.findall('vector'):
                                for report7 in report6.findall('url'):
                                    report_url = report7.text
                                    for solution1 in solution_root.findall('select'):
                                        for solution2 in solution1.findall('name'):
                                            for solution3 in solution1.findall('description'):
                                                for solution4 in solution1.findall('solution'):
                                                    solution_name = solution2.text
                                                    solution_description = solution3.text
                                                    solution_solution = solution4.text
                                                    if (solution_name == report_name):
                                                        f.write("<p class='container'>----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>")
                                                        f.write("<p class='name'>"+solution_name+"</p>")
                                                        f.write("<p class='description'>"+report_description+"</p>")
                                                        f.write("<p class='solution'>"+solution_solution+"</p>")
                                                        f.write("<p class='url'>"+report_url+"</p>")

                                                        saverecord = UserReport()
                                                        saverecord.email=request
                                                        saverecord.scan_data=scan_id
                                                        saverecord.scan_website=website
                                                        saverecord.vulnerabilities=report_name
                                                        saverecord.solutions=solution_solution
                                                        saverecord.date = today
                                                        saverecord.scan_type = scan_select
                                                        saverecord.report_url = report_url
                                                        saverecord.vulnerabilities_description = report_description
                                                        saverecord.save()

                                                        savescanid = SaveScanID()
                                                        scan_id_2 = scan_id
                                                        if (scan_id_1 != scan_id_2):
                                                            savescanid.scan_data = scan_id_2
                                                            scan_id_1 = scan_id_2
                                                            savescanid.date = today
                                                            savescanid.scan_website = website
                                                            savescanid.email = request
                                                            savescanid.scan_type = scan_select
                                                            savescanid.save()
                                                        

                                                        
                                            
        f.write("</div>")
        f.write("</body>")
        f.write("</html>")  
        f.close()

        print(scan_select)


        
def SendEmail(request):
    mail_content = """Hello,
    Your scan is completed. You may visit rickyteama.com to retrieve your results.
    
    Yours sincerely,
    Ricky Team
    """

    #The mail addresses and password
    sender_address = "fypb4343@gmail.com"
    sender_pass = "@bcde_12345"
    receiver_address = str(request)
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    



def ArachniScan(request):
    try:
        scan_type = "non_authenticated_scan"
        target_website = request.POST.get('target_website')
        scan_select = request.POST.get('scan_select')
        target_username = request.POST.get('target_username')
        target_password = request.POST.get('target_password')
        

        client = ArachniClient()
        URL = url_in(target_website)
        auth = 0
        username = target_username
        password = target_password
        profile = edit_profile(scan_select)


        if (target_password == "" and target_username == "" ):
            #non authenticated scan

            auth = False

            start_scan(client, auth)
            while(1):
                if(client.get_report(get_ID(), 'xml') == None and client.get_status(get_ID())["busy"] == True):
                    continue
                else: 
                    scan_id = get_ID()
                    b = client.get_report(scan_id, 'xml')
                    if (type(b) == bytes):
                        b = b.decode("utf-8")
                    elif (b == None):
                        b = "<?xml version='1.0'?><report>None</report>"
                    c = open("reporthtml.xml","w")
                    c.write(b)
                    c.close()
                    generateReport(request.user, target_website, scan_id, scan_select)
                    SendEmail(request.user)
                    break

            print(scan_type)
            return redirect('arachni_redirect/',)
        else:
            scan_type= "authenticated_scan"

            auth = True

            auth_scan_parameters(URL, username, password)
            start_scan(client, auth)
            while(1):
                if(client.get_report(get_ID(), 'xml') == None and client.get_status(get_ID())["busy"] == True):
                    continue
                else: 
                    scan_id = get_ID()
                    b = client.get_report(scan_id, 'xml')
                    if (type(b) == bytes):
                        b = b.decode("utf-8")
                    elif (b == None):
                        b = "<?xml version='1.0'?><report>None</report>"
                    c = open("reporthtml.xml","w")
                    c.write(b)
                    c.close()
                    generateReport(request.user, target_website, scan_id, scan_select)
                    SendEmail(request.user)
                    break

            print(scan_type)
            return redirect('arachni_redirect/',)
    except: 
        messages.error(request, 'Could not connect to host, try again')
        return render(request, 'home.html')