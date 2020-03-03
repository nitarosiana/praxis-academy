import fibo


fibo.fib(1000)
print('================')

print(fibo.fib2(100))
print('================')

print(fibo.__name__)
print('================')

fib = fibo.fib
fib(500)