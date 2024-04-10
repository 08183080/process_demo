import pickle

data = {'key1': 'dragon',
        'key2': 'python',
        'key3': 'looong'}

strs = pickle.dumps(data)
print('pickle serilization resuls: ', strs)

print('pickle deserilization results: ', pickle.loads(strs))