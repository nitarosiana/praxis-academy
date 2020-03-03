import Bubble_Sort


list =[7,8,6,4,1,3]
print("Data yang di sort", list)
print("Bubble Sort :")
Bubble_Sort.bubble_sort(list)
print('================================================')


import Insertion_Sort

list = [2,54,38,76,23,56,84,90]
print("Data yang di sort", list)
print("Insertion Sort :")
Insertion_Sort.insertion(list)
print('=================================================')


import Selection_Sort

list=[98,6,33,11,57,33,44,55,29,76,60,81]
print('Data yang di sort :', list )
print('Selection Sort :')
Selection_Sort.ss(list)
print('=================================================')


import Quick_Sort

a = [68,90,78,44,34,20,100,56,34,2]
print('Data yang di sort :', list )
print('Quick Sort :')
Quick_Sort.quicksort(a,0,len(a)-1)
print('=================================================')


import Merge_Sort


list = [2,5,60,43,27,10,89,17]
print('Data yang di sort :', list )
print('Merge Sort :')
Merge_Sort.mergesort(list)
print('=================================================')