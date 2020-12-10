year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
print('===================================')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
print('===================================')

s = 'Hello, world.'
print(str(s))
print('===================================')

print(str(1/7))
print('===================================')

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print('===================================')

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))
print('===================================')