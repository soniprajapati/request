import requests

#this is how we use parameter in get request
payload={'key1':'value2'}
res=requests.get('https://httpbin.org/get',params=payload)

print(res.url)