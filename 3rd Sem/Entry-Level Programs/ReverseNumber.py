print("===Input===")
num=int(input("Enter a Number :"))
print("===Output===")
rev=0
temp=num
while num!=0:
    d=num%10
    rev=rev*10+d
    num=num//10
print("Original Number :",temp)
print("Reverse Number :",rev)
