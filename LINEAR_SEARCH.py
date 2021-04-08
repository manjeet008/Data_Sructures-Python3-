list=input("Enter elements separated by comma....")
new=list.split(",")
length=len(new)
search=input("Enter the searching element..")
for i in range(0,length):
    if search==new[i]:
        print("Element found at ",i+1," place")
        break
    else:
        pass
else:
    print("Element not found....")
