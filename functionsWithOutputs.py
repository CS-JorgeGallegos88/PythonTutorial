def calculate(number1:float, number2:float, operation:str) -> float:
    if operation == "add":
        return number1 + number2
    if operation == "substract":
        return number1 - number2
    if operation == "divide":
        return number1 / number2
    if operation == "multiply":
        return number1 * number2

number1_choice = float(input("Introduce the first number: "))
number2_choice = float(input("Introduce the second number: "))
operation_choice = input("Introduce the operation: ")
result = calculate(number1=number1_choice, number2=number2_choice, operation=operation_choice)
print(result)

def format_name(f_name:str, l_name:str):
    return (f_name + " " + l_name).title()

print(format_name("jorge", "gallegos"))


#Leap years
def is_leap_year(year):
    isLeap = False
    if year % 4 == 0:
        if year % 100 > 0:
            return True
        else: 
            if year % 400 == 0:
                return True
    return isLeap

print(is_leap_year(2020))
