import math
print(f'The value of pi is approximately {math.pi:.3f}.')


print('===============================')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('===============================')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print('===============================')

print(f'My hovercraft is full of {animals!r}.')

print('===============================')
