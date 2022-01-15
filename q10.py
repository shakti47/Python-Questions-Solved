first=int(input("enter the first number : ")'
second=int(input("Enter the Second Number: "))
for i in range(First,Second+1)
          flag=1
          for j in range(2,(i//2)+1):
                if  i % j ==0:
                       flag=0
                       break
            else:
                 if flag==1 and i!=1:
                     print("Prime Number", i )
