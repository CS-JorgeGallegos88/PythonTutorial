colors = {
    "apple":"red",
    "pear":"green",
    "banana":"yellow"
}

#Get item by Key
print(colors["apple"])

#Add new elements to dictionary
colors["orange"] = "orange"

#Edit item on the dictionary
colors["apple"] = "green"

print(colors)

#Empty dictionary
empty_dictionary = {}
empty_dictionary["Seiya"] = "Pegaso"
empty_dictionary["Saga"] = "Geminis"
empty_dictionary["Shaka"] = "Virgo"
print(empty_dictionary)

#Clear dictionary
empty_dictionary = {}
print(empty_dictionary)

#Loop thru dictionary - will only return the keys not the values
for color in colors:
    print(color)

#List as value
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"]
}

#Print Paris
print(travel_log["France"][0])

#Print D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

another_travel_log = {
    "France" : {
        "num_times_visited": 8,
        "cities_visited":["Paris", "Lille", "Dijon"]
    },
    "Germany" : {
        "num_times_visited": 2,
        "cities_visited":[ "Berlin", "Hamburg", "Stuttgart",]
    }
}

#Print travel log for France
print(f"You have visited France {another_travel_log["France"]["num_times_visited"]} times and you have been in these cities: {another_travel_log["France"]["cities_visited"]}")

#Print Stuttgart
print(another_travel_log["Germany"]["cities_visited"][2])

#Another example
starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)