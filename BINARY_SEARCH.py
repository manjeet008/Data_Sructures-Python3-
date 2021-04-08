list1=[55,21,13,4,98,62,71,29,10,12]
list1.sort()
low=0
high=len(list1)-1
search=int(input("Enter an element.....  "))
print("\nList is ",list1)
while(low<=high):
    mid=(low+high)//2
    if(search==list1[mid]):
        print("Element found at ",mid," position")
        break
    elif(search>list1[mid]):
        low=mid+1
    elif(search<list1[mid]):
        high=mid-1
    else:
        print("Element not found in the list.....")
        break