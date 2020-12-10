try:
    raise NameError('Hi There')
except NameError:
    print('An exceptions flew by!')
    raise