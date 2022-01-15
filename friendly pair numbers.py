n=int(input("enter the first number"))
m=int(input("enter the second number"))
n_divisor=0
m_divisor=0

for i in range(1,(n//2)+1):
    if n%i==0:
        n_divisor+=i

for i in range(1,(m//2)+1):
               if m%i==0:
                   m_divisor+=i

if m_divisor==n and n_divisior==m:
               print("Friendly divisor")
else:
    print("Not friendly pair")

