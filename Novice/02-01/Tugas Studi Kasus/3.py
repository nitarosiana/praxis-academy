def kuadrat(x):
    return x*x

def masuk_list(l, fn):
    return  [fn(n) for n in l]

l = [1,2,3,4,5,6,7,8,9,10]

print(masuk_list(l, kuadrat))
