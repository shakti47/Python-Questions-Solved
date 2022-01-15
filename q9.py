def prime(n):
  if(n>1):
       for i in range(2,n):
           if(n%i)==0:
               print(n,"is not a prime nuber")
               break
  else:
       print(n,"is a prime number")


num=int(input("enter a number: "))
prime(num)
