import requests 

endpoint = 'http://httpbin.org/get'

myreq = requests.get(endpoint)
print(myreq.json())