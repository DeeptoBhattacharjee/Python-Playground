print("===Input===")
num1=int(input("Enter 1st Number :"))
num2=int(input("Enter 2nd Number :"))
num3=int(input("Enter 3rd Number :"))
print("===Output===")
if num1<num2 and num1<num3:
    print(num1,"is the smallest of three")
elif num2<num1 and num2<num3:
    print(num2,"is the smallest of three")
else:
    print(num3,"is the smallest of three")