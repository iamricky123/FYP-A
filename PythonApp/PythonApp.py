from arachni import *

client = ArachniClient()
client.target('https://tryhackus-theboyes.ml/login') # set target url
client.start_scan() # start scan
client.get_scans() # you can get scan ids that are requested.
client.get_report('f708c31c5532b84f9d76e0c79570752c', 'xml') # get report in several format