import json

a = {
    'name': 'Jack',
    'age': 22,
    'marks': [80, 90, 100, 95],
    'pass': True
}

print(json.dumps(a))