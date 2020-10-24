people = [{
    'name': 'Marek',
    'age': 20
},{
    'name': 'Karol',
    'age': 10
}]

names = [p['name'] for p in people]

names2 = []
for p in people:
    names2.append(p['name'])

print('x')
