print("===Input===")
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
print("===Output===")
temp1=a
temp2=b
while b!=0:
    a,b=b,a%b
print("HCF of",temp1,"and",temp2,":",a)