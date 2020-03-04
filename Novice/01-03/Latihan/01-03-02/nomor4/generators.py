def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


    for char in reverse('golf'):
        print(char) 


    sum(i*i for i in range(10))
    print(sum)


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))
print(sum)