print("===Input===")
num=int(input("Enter a Number :"))
print("===Output===")
s=0
while num!=0:
    d=num%10
    s+=d
    num=num//10
print("The Sum of Digits :",s)