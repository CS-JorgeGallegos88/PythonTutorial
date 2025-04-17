fruits = ["apple", "orange", "cherry"]
states_of_america = ["Delaware", "Pennsylvania"]

#access by index
first_state = states_of_america[0]

#Append single item to the list
states_of_america.append("Florida")

#Append a new list to the list
states_of_america.extend(["Washington", "Georgia"])

print(first_state)
print(states_of_america)

#nested list
the_boys = ["Chandler", "Ross", "Joey"]
the_girls = ["Monica", "Rachel", "Phoebe"]
the_one_with_the_friends = [the_boys, the_girls]

'''
En este ejemplo el primer index es para seleccionar la lista 
y el segundo index es para seleccionar un item dentro de esa lista
Ej. the_one_with_the_friends[0][1] -> Ross
    the_one_with_the_friends[0][1] -> Rachel
'''
the_one_with_two_index = the_one_with_the_friends[0][1]
print(the_one_with_two_index)