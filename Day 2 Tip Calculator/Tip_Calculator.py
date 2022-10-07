print ("Welcome to the tip calculator.")
bill = float(input("What is the total bill?  $"))
tip = int(input("how much tip would you like to give? 5, 10, 12, 15, etc "))
people = int (input("How many people to split the bill?"))
tip_as_percent = tip/100
total_tip = bill * tip_as_percent
bill_with_tip = bill + total_tip
bill_per_person = round(bill_with_tip/people, 2)
print(f"Your total bill including tip is { bill_with_tip } ")
print(f"Each person should pay { bill_per_person } ")