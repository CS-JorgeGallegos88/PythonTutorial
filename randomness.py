import random
import my_module

#--> random() devuelve un valor de punto flotante entre 0 y 1 sin incluir 1 (Ej. 0.12312)
# random_0_to_1 = random.random() 

#random_integer = random.randint(1, 10)
# random_0_to_10 = random.random() * 10
# random_float = random.uniform(1, 20)

# print(random_0_to_1)
# print(random_integer)
# print(random_0_to_10)
# print(random_float)
# print(my_module.my_favorite_number)

#Heads or Tails game
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("heads")
else:
    print("tails")