n=int(input("enter then number"))
sum=0
order= len(str(n))
copy_n=n
while(n>0):
    digit =n%10
    sum += digit **order
    n = n//10

if(sum== copy_n ):
    print("{} is an armstrong number",copy_n)
else:
    print("{} is  not an armstrong number",copy_n)
    
