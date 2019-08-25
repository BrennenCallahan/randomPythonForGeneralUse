import requests
import redfish

r=requests.get("http://github.com/timeline.json")
print r.headers    #gets the headers from the URL
print "\n"
print r.encoding #prints the encoding of the page









