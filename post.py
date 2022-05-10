import requests

#we use this to give perameter in post method

payload={'key1':'value2'}
res=requests.post("https://httpbin.org/post",data=payload)

print(res.text)