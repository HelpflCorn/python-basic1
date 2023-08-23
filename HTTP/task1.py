import requests

l1 = requests.get("https://en.wikipedia.org/wiki/Robot")


with open ('/Users/mp5f8/Documents/GitHub/python-basic1/HTTP/robots.txt', 'wb') as f: #this doesn't look nice
    f.write(l1.content)


with open ('/Users/mp5f8/Documents/GitHub/python-basic1/HTTP/robots.html', 'wb') as f: 
    f.write(l1.content)


with open('/Users/mp5f8/Documents/GitHub/python-basic1/HTTP/banana.jpg', 'wb') as f:
    f.write(requests.get("https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg").content)