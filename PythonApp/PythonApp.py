from arachni import *
import json



client = ArachniClient()

#jsonOpen = open('./input/input.json', 'r')
#data = json.load(jsonOpen)
#url = data["url"]
#profile = data["profile"]
#jsonOpen.close()

#client.profile('./profiles/'+ profile + '.json')
#client.target(url) # set target url
#container = client.start_scan()

#jsonOpen2 = open('./input/input.json', 'w')
#_id = container.get("id")
#data["scan_id"] = _id
#json.dump(data, jsonOpen2, indent=4)
#jsonOpen2.close()

client.get_status('300c93808bc9b092ce35235f12b779d4')
client.get_scans() # you can get scan ids that are requested.

client.get_report('300c93808bc9b092ce35235f12b779d4', 'xml')# get report in several format
