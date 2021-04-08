list1=[9,1,6,5,7,3,8,4]
for i in range(len(list1)):
    for j in range(0,len(list1)-1):
        if(list1[j]>list1[j+1]):
            list1[j],list1[j+1]=list1[j+1],list1[j]
        else:
            pass
print("SORTED LIST is  ",list1)