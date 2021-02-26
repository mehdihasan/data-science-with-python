import requests
import os 
from PIL import Image
from IPython.display import IFrame


###
# https://requests.readthedocs.io/en/master/
###

url='https://www.ibm.com/'
r=requests.get(url)
print(r)
print(r.status_code)
print(r.request.headers)
print(r.headers)
print("request body:", r.request.body)

header=r.headers
print(header['date'])
print(header['Content-Type'])
print(r.encoding)
print(r.text[0:100])

# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
print(r.headers['Content-Type'])
path=os.path.join(os.getcwd(),'image.png')
print(path)
with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)


### 
# wget -O /resources/data/Example1.txt <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt
textUrl = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
req=requests.get(textUrl)
localPath=os.path.join(os.getcwd(),'resources/Example1.txt')
with open(localPath, 'wb') as f:
    f.write(req.content)


## Get Request with URL Parameters
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)
print("request body:", r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])


## Post Requests
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
r_post.json()['form']