print('Hola')


def my_print(text):
    print(text * 2)


my_print('Este es my texto')
my_print('Hola')

a = 10
b = 90

c = a + b


def suma(a, b):
    my_print(a + b)


suma(1, 5)  # 6
suma(10, 4)  # 14

def espar(num1, num2):
    if (num1 + num2) % 2 == 0:
        print("La sumas de los dos da un numero par")
    else:
        print("la suma da un numero impar")

espar(4,2)
espar(3,2)