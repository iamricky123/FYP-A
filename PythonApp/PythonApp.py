from arachni import *
import json



client = ArachniClient()
client.profile('./profiles/default.json')

jsonOpen = open('./input/input.json', 'r')
data = json.load(jsonOpen)
url = data["url"]
jsonOpen.close()

client.target(url) # set target url
container = client.start_scan()

jsonOpen2 = open('./input/input.json', 'w')
_id = container.get("id")
data["scan_id"] = _id
json.dump(data, jsonOpen2, indent=4)
jsonOpen2.close()

##client.get_status('0c3ed20a3bc3bc4f3473d2282367b61b')
##client.get_scans() # you can get scan ids that are requested.
##client.get_report('0c3ed20a3bc3bc4f3473d2282367b61b', 'xml') # get report in several format
 
