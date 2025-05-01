print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? "))
tip_vale = float(input("How much tip would you like to give? 10 , 12 or 15 "))
total_people = float(input("How many people to split the bill?" ))

divided_bill = round(((total_bill * (1 + (tip_vale/100))) / total_people), 2)
print(f"Each person should pay: {divided_bill}")