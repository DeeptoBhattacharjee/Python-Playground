print("===Input===")
m1=int(input("Enter the marks in Subject 1 :"))
m2=int(input("Enter the marks in Subject 2 :"))
m3=int(input("Enter the marks in Subject 3 :"))
m4=int(input("Enter the marks in Subject 4 :"))
m5=int(input("Enter the marks in Subject 5 :"))
print("===Output===")
percent=(m1+m2+m3+m4+m5)/5
if percent>=60:
    print("First Division")
elif percent>=50 and percent <=59:
    print("Second Division")
elif percent>=40 and percent <=49:
    print("Third Division")
else:
    print("Fail")