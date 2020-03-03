def selection_sort(list):
    iterasi = 0
    for i in range(len(list)-1):
        minimal = i
        for j in range(i+1,len(list)):
            if list[j] < list[minimal]:
                minimal = j
        iterasi += 1
        list[minimal],list[i]=list[i], list[minimal]
        print(iterasi, list)
list=[98,6,33,11,57,33,44,55,29,76,60,81]
print('Data yang di sort :', list )
print('Selection Sort :')
selection_sort(list)