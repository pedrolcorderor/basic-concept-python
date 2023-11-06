'''
dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)
'''
names = ['nico', 'zule', 'santi',"pepe"]
ages = [12, 56, 98]
#zip nos une dos listas ,pero nos devuelve una direccion , hay que convertirlo en una lista 
print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
"""
Revisando los comentarios para las personas que usan una iteracion con len estan asumiendo que las 2 listas contiene la misma cantidad de elementos. y para este caso especifico el output es correcto.

como obervacion: y que pasa si una lista tiene un elemento mas o menos que la otra, con la iteraciones de indices de las 2 lista se rompe el programa por el error IndexError: list index out of range, por que un elemento no tiene un indice homologo en la otra lista, espero hay sido claro.

para mi gusto la mejor manera es usar la funcion zip ya que ese elemento que no tiene pareja la omite y solo une las listas con los elementos con indices iguales.

el primera instancia eso me ahorraria mucha logica tratando ese error de los indices.
"""
#por ejemplo abajo al usar len como referencia  : si hubiese un elemento de mas en names daria un error porque interia buscar 
#un elemento en la posicion 4 de edades que no existe y dara error , por eso es bueno zip, ya que descartaria esa posicion ya que no existe .
names = ['sofi', 'angel', "pedro"]
edades = [12,56,98, 55]
new_dict = {names[i]:edades[i] for i in range(len(names))}
print(new_dict)