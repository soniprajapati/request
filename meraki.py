import json
from textwrap import indent
import requests

 
r=requests.get("http://saral.navgurukul.org/api/courses")
a = r.json()
print(a)
with open("meraki.json","w") as c:
    json.dump(a, c, indent = 4)


n=0
id=[]
for i in a["availableCourses"]:
    print(n,i['name'],":",i['id'])
    id.append(i["id"])
    n+=1
