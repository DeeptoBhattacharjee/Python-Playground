print("===Input===")
num=int(input("Enter a Number :"))
print("===Output===")
i=1
s=0
while i<num:
    if num%i==0:
        s+=i
    i+=1
if s==num:
    print(num,"is a Perfect Number")
else:
    print(num,"is not a Perfect Number")