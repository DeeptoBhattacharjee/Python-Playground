print("===Input===")
num=int(input("Enter a Number :"))
print("===Output===")
i=1
c=0
while i<=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print(num,"is a Prime Number")
else:
    print(num,"is not a Prime Number")