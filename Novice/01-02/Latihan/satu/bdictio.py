tel = {'jack' : 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print('===============================')

print(tel['jack'])

print('===============================')

del tel['sape']
tel['irv'] = 4127
print(tel)

print('===============================')

print(list(tel))

print('===============================')

print(sorted(tel))

print('===============================')

print('guido' in tel)

print('===============================')

print('jack' not in tel)

print('===============================')

print({x: x**2 for x in (2, 4, 6)})

print('===============================')

print(dict(sape=4139, guido=4127, jack=4098))

print('===============================')
