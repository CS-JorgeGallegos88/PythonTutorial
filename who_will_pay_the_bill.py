import random

friends = ["Monica", "Chandler", "Rachel", "Ross", "Joey", "Phoebe"]

#Obtener un elemento de la lista accediendo a los elementos de la lista por 
#medio de un index random
who_will_pay_the_bill = friends[random.randint(0, len(friends)-1)]

#choice sirve para obtner un elemento random de una lista
who_will_pay_the_tip = random.choice(friends)
print(f"{who_will_pay_the_bill} has to pay the bill and {who_will_pay_the_tip} will pay the tip")