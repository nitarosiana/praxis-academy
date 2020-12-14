def ubah_list(l):
    l.append('orange')
    l[0]= 'grape'
    return l
l = ['mango', 'apple', 'strawberry', 'pineapple']
print(ubah_list(l))