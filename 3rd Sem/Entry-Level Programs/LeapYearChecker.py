print("===Input===")
year=int(input("Enter a Year :"))
print("===Output===")
if year%4==0 or year%400==0:
    print("The Year",year,"is a Leap Year")
else:
    print("The Year",year,"is not a Leap Year")
