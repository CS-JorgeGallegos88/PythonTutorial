#PEMDAS (El orden en que se ejecutan las operaciones)
#Las operaciones siempre se van resolviendo de izq a derecha
# ()
# **
# *
# * OR /
# * OR -

print(3 * 3 + 3 / 3 - 3) # => 7.0 (Estos calculos devuelven float)  
print(3 * (3 + 3) / 3 - 3) # => 3.0 (Estos calculos devuelven float)

#Round
bmi = 84 / 1.65 ** 2
print(round(bmi, 2))

#Operators
score = 9
score += 1
score -= 2
score *= 4 
score /= 3
print(score)
