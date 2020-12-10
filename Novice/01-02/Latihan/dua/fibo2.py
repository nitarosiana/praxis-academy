import fibo

print(fibo.fib(1000))

print('===============================')

print(fibo.fib(100))

print('===============================')

fib = fibo.fib
print(fib(500))

print('===============================')

from fibo import fib, fib2
print(fib(500))

print('===============================')

from fibo import *
print(fib(500))

print('===============================')

import fibo as fib
print(fib.fib(500))