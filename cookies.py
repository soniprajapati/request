from http import cookies
import requests


res=requests.get('https://httpbin.org/cookies',)

print(res,cookies           )