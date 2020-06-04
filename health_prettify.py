import json
import re
from unicodedata import normalize

temp_diseases = {}

with open('diseases.txt') as json_file:
    print("Starting prettifying diseases...")
    data = json.load(json_file)

    for key in data.keys():
        data[key] = normalize("NFKD",data.get(key))
        temp_key = key.replace('\n\n\t\t\t','')
        temp_key = temp_key.replace('\n\t\t\n\n', '')
        temp_key = temp_key.replace('\n\t\t\t', '')
        temp_key = temp_key.replace('\n\n\n', '')
        temp_diseases[temp_key] = data[key]

    print("Prettifying professions is completed...")

with open('diseases.txt','w') as json_file:
    json.dump(temp_diseases,json_file)