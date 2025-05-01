#Range function 1-9 (no incluye el 10)
# for number in range(1, 10):
#     print(number)

#Range function el 2 es para el step, para que se salte 2
#step => La cantidad por la que se incrementa (o decrementa) cada número en la 
#secuencia (opcional; por defecto es 1).
#1,3,5,7,9
# for number in range(1, 10, 2):
#     print(number)

#FizzBuzz
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)