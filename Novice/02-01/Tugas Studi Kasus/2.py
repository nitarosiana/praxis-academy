def mengubah_list(l):
    l.append(11)
    l[0] = 1
    return l

l = [5,7,9]
print(mengubah_list(l))