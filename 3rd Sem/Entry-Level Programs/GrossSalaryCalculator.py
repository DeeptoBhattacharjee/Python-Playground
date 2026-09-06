print("===Input===")
basic=int(input("Enter the Basic Salary :"))
print("===Output===")
if basic<1500:
    hra=0.1*basic
    da=0.9*basic
else:
    hra=500
    da=0.98*basic
gross=basic+hra+da
print("Basic Salary = Rs.",basic)
print("Gross Salary = Rs.",gross)