print("===Input===")
num=int(input("Enter a Number :"))
print("===Output===")
temp=num
arm=0
while num!=0:
    d=num%10
    arm=arm+(d**3)
    num=num//10
if arm==temp:
    print(temp,"is an Armstrong Number")
else:
    print(temp,"is not an Armstrong Number")
    