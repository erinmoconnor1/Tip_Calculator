print("Welcome to the tip calculator!")
bill = float(input("What was the total amount of your bill?\n"))
num_people = int(input("How many people will split the bill?\n"))
Tip = int(input("How much tip would you like to give? 12, 15, or 20?\n"))
Tip_as_percent = Tip / 100 + 1
Bill_Total = bill * Tip_as_percent
Bill_Split = ((Bill_Total) / num_people)
Final_Bill_Split = round(Bill_Split, 2)
print(f"Each person should pay: ${Final_Bill_Split}")