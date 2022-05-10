import requests

#this is how we use get request
res=requests.get('https://httpbin.org/get')

print(res.text) 