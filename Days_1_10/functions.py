def greet_with_location(name, location):
    print(f"Hello {name}, What is it like in {location}")

#Positional arguments
greet_with_location("Yorsh", "Florida")

#Keyword arguments
greet_with_location(location = "Florida", name = "Zuzu")


def calculate_love_score(name1, name2):
    fullname = (name1 + name2).lower()
    total_T = fullname.count("t")
    total_R = fullname.count("r")
    total_U = fullname.count("u")
    total_E = fullname.count("e")
    total_true = total_T + total_R + total_U + total_E
    
    total_L = fullname.count("l")
    total_O = fullname.count("o")
    total_V = fullname.count("v")
    total_E = fullname.count("e")
    total_love = total_L + total_O + total_V + total_E
    
    love_score = int(str(total_true) + str(total_love))
    print(f"Love Score = {love_score}")

calculate_love_score("Angela Yu", "Jack Bauer")