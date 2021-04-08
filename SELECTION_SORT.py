def selection_sort(list1):
    sorted_list=[]
    for i in range(len(list1)):
        minpos=i
        for j in range(i,len(list1)):
            if (list1[j]<list1[minpos]):
                list1[j],list1[minpos]=list1[minpos],list1[j]
list1=[3,9,11,34,7,24]
selection_sort(list1)
print(list1)