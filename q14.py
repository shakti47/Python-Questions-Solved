size=int(input("ENTER ARRAY SIZE "))
arr=[]
for i in range(size):
    element=int(input())
    arr.append(element)
print("LARGEST ELEMENTIS",max(arr))
