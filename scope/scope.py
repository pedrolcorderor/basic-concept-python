price = 100  # global
# result = 200

def increment():
    #price = price + 10 
    #! Error 
    
    # andres =20
    
    price = 200
    result = price + 10
    print(result)
    return result
#aunque existan dos variables de nombre price las dos son diferente por el contexto (scope )en el que estan , una tiene scope global y otra scope local . si price no tubiese el valor 200 . daria error porque no existe el price de scope funcion 

print(price)
price_2 = increment()
print(price_2)
# print(result)
#andres = andres + 10

pedro ="pedro"
def pepe():
    print(pedro)
    sofia=pedro + " cordero "
    print(sofia)
pepe()

result = price + 10
print(result)