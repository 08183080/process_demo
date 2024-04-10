import json

data = {'key1': 'dragon',
        'key2': 'python',
        'key3': 'looong'}

strs = json.dumps(data)
print('json serilization resuls: ', strs)

print('json deserilization results: ', json.loads(strs))