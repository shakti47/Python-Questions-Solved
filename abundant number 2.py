import math
print("Enter the number:")
n=int(input())
sum=1 
i=2

while(i<=math.sqrt(n)):
    if(n%i==0): 
        if(n//i==i): 
           sum=sum+i
        else:
            sum=sum + i + n/i

    i=i+1

if(sum>n):
    print(n,"is Abundant Number")
else:
    print(n,"is not Abundant Number")
