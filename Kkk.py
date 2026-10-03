subtotal = int(input("How many Students? "))

for i in range(subtotal):
    print("Student", i + 1)
    
    name = input("Enter name: ")
    activity1 = int(input("Activity 1: "))
    activity2 = int(input("Activity 2: "))
    activity3=int(input("activity3"))
    totals = activity1 + activity2 + activity3
    average = totals / 3
    
    print("Average:", average)
    
    if average >= 90:
        print("Status: Excellent")
    elif average >= 80:
        print("Status: Very Good")
    elif average >= 75:
        print("Status: Passed")
    else:
        print("Status: Failed")
        
    print()
