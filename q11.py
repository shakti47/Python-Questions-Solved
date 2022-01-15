num= int (input("Enter the number : "))
temp=num
reverse=0
while num>0:
    remainder = num%10
    reverse=(reverse*10)+remainder
    num=num//10

if temp==reverse:
    print("given number {} is palindrome".format(temp))
else:
    print("Given number {} is not palindrome".format(temp))

