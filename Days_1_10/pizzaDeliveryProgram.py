print("Welcome to Python Pizza deliveries!")
size = input("What size of pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
final_bill = 0

if size.upper() == "S":
    final_bill = 15
elif size.upper() == "M":
    final_bill = 20
elif size.upper() == "L":
    final_bill = 25
else:
    print("Wrong input")
    exit()

if pepperoni == "Y":
    if size.upper() == "S":
        final_bill += 2
    else:
        final_bill += 3

if extra_cheese.upper() == "Y":
    final_bill += 1

print(f"Your final bill is ${final_bill}")
