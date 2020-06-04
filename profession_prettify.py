import json
from unicodedata import normalize

temp_profs = {}

with open('data.txt') as json_file:
    print("Starting prettifying professions...")
    data = json.load(json_file)

    for key in data.keys():
        data[key] = normalize("NFKD",data.get(key))
        data[key] = data.get(key).replace('\t\t\t\t\t\t\t\t','')
        data[key] = data.get(key).replace('\t\t\t\t\t\t\t','')
        data[key] = data.get(key).replace('\n','')

    for key in data.keys():
        tmp_key = normalize("NFKD",key)
        temp_profs[tmp_key] = data.get(key)
    print("Prettifying professions is completed...")

with open('data.txt','w') as json_file:
    json.dump(temp_profs,json_file)