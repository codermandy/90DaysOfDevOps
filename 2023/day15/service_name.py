# {
#     "services": {
#       "debug": "on",
#       "aws": {
#         "name": "EC2",
#         "type": "pay per hour",
#         "instances": 500,
#         "count": 500
#       },
#       "azure": {
#         "name": "VM",
#         "type": "pay per hour",
#         "instances": 500,
#         "count": 500
#       },
#       "gcp": {
#         "name": "Compute Engine",
#         "type": "pay per hour",
#         "instances": 500,
#         "count": 500
#       }
#     }
#   }



#json file
import json

#opening JSON file
f=open('2023/day15/services.json')

#returns JSON object as a dictionary
data=json.load(f)
#Iterating through JSON list
for i in data['services']:
    print(i)

# closing file 
f.close();

