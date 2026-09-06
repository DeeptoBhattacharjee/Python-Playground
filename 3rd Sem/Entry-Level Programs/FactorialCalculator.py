print("===Input===")
num=int(input("Enter a Number :"))
print("===Output===")
i=1
fact=1
while i<=num:
    fact*=i
    i+=1
print("Factorial of",num,":",fact)