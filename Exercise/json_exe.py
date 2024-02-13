import json
from json import JSONEncoder

# data = """{"key1" : "value1", "key2" : "value2"}"""
# jsonData = json.dumps(data)
# print(jsonData)


# data = """{"key1" : "value1", "key2" : "value2"}"""
# sample = json.loads(data)
# print(sample['key2'])

# sampleJson = {"key1": "value1", "key2": "value2", "key3" : "value3"}
# seperate = json.dumps(sampleJson,indent=2,separators=(",","="))
# print(seperate)


# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# with open("samplejson.json","w") as write_file:
#     json.dump(sampleJson,write_file,indent=4,sort_keys=True)
# print("executed successfully")



# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payble":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
#
# nested =json.loads(sampleJson)
# print(nested["company"]["employee"]["payble"]["salary"])


# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
# class VehicleEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
#
# print("Encoding Vehicle object into JSON Data")
# vehiclejson = json.dumps(vehicle,indent=4,cls=VehicleEncoder)
# print(vehiclejson)


# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
# def vehicleDecoder(obj):
#     return Vehicle(obj['name'],obj['engine'],obj['price'])
#
# vehicleobj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',object_hook=vehicleDecoder)
# print("Type of decoded object from JSON Data")
# print(type(vehicleobj))
# print("Vehicle Details")
# print(vehicleobj.name, vehicleobj.engine, vehicleobj.price)


# def validateJSON(jsonData):
#     try:
#         json.loads(jsonData)
#     except ValueError as err:
#         return False
#     return True
#
# InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000,"bonus":800} } } }"""
# isValid = validateJSON(InvalidJsonData)
#
# print("Given JSON string is Valid", isValid)


json_data = """[
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]"""

# data = ""
#
# data = json.loads(json_data)
#
#
# dataList = [item.get('name') for item in data]
# print(dataList)

# json_data_list = json.loads(json_data)
# json_data_list_name = []
# for item in json_data_list:
#     for key, value in item.items():
#         if key == 'name' :
#             json_data_list_name.append(value)
# json_data_list_name_string = json.dumps(json_data_list_name)
# print(json_data_list_name_string)