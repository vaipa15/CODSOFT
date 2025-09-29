num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

print("choose the operation:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=input("enter choice(1/2/3/4):")

if choice=="1":
    print("addition:",num1+num2)
elif choice=="2":
    print("subtraction:",num1-num2)
elif choice=="3":
    print("multiplication:",num1*num2)
elif choice=="4":
    print("division:",num1/num2)
else:
    print("invalid choice")
