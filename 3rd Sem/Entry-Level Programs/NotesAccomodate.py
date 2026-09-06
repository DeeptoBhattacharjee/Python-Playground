print("===Input===")
amt=int(input("Enter the amount : "))
notes=[500,200,100,50,20,10,5,2,1]
total_notes=0
print("===Output===")
for note in notes:
    count=amt//note
    amt=amt%note

    if count>0:
        print(note,"x",count)
        total_notes+=count
print("Minimum No. of Notes :",total_notes)