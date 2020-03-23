import json

with open('sumber.json') as json_sumber:
    dt = json.load(json_sumber)
    for p in dt['people']:
        print('Name: ' + p['name'])
        print('Prodi: ' + p['prodi'])
        print('Fakultas: ' + p['fakultas'])
        print('')