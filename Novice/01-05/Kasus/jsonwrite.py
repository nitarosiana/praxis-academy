import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Nita Rosiana',
    'prodi': 'Sistem Informasi',
    'fakultas': 'FAST'
})
data['people'].append({
    'name': 'Devia Oktavia',
    'prodi': 'Matematika',
    'fakultas': 'FAST'
})

with open('sumber.json', 'w') as outfile:
    json.dump(data, outfile)