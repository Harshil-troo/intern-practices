import json
import requests
# data = open("test.json","r")
# print(data)
# print(type(data))
# print(data.read())
# myobj = json.load(data)
# print(myobj[0]["name"])
# print(type(myobj))

obj = {"Employee1":
    {
        "name":"Harshil",
        "skill":"Python"
    },"Employee2":
    {
        "name":"Tasmey",
        "skill":".net"
    },"Employee3":
    {
        "name":"Nikhil",
        "skill":"Angular"
    }
}

# print(type(obj))
# jsondata = json.dumps(obj)
# print(jsondata)
# print(type(jsondata))
#
# f =open("new.json","w")
# f.write(jsondata)


url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
# print(response.status_code)
# print(response.text)
responseobj = json.loads(response.text)
# print(responseobj)
print(len(responseobj))

response = requests.post(url,data={"userid": 1,
                                   "title":"My New Title"})
print(response.text)
print(response.status_code)