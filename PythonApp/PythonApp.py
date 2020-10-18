from arachni import *

client = ArachniClient()

readURL = open("id.txt","r")
URL = readURL.readlines()


client.target(URL[0]) # set target url
container = client.start_scan()

readURL.close()

f = open("id.txt","w+")
_id = container.get("id")
print(_id)
f.write(_id)
f.close()
        
#client.get_scans() # you can get scan ids that are requested.
#client.get_report('f708c31c5532b84f9d76e0c79570752c', 'xml') # get report in several format
 
