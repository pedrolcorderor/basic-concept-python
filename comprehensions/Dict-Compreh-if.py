import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2) 

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result) #recordar que convertimos el objeto en una lista llave valor de tuplas gracias al metodo items para poder iterar

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)
# tenemos tres o ,pero en el  diccionario no se puede repetir llave , ahora para contar utilizamos la funcion count

unique2 ={ c: text.count(c) for c in text if c in 'aeiou' }
print(unique2)

#? con module podemos hacer algo parecido ok
import collections
unique3 = collections.Counter(text)
print(unique3)

numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter,'\n')



pedro=["hola", 'hola','hola','pedro']
print("veces que aparece la palabra hola usando el metodo count ",pedro.count("hola"))
#? el metodo count nos devuelve el numero de elemetos repetidos dentro de un dato iterable . tuplas , listas o string
