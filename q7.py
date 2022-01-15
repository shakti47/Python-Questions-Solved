x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
z=int(input("Enter the 3rd number : "))

if x>y>z:
    print(x,"is largest")
elif y>x>z:
    print(y,"is largest")
else:
    print(z,"is largest")
