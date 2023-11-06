""" from pkg.mod_1 import func_1,func_2
from pkg.mod_2 import func_3,func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
"""


"""
otra forma de usar el init que nosea definir variables cada vez que se importe el paquete .
TODO : y es hacer  imports en __init__ (es una manera explicita ) en vez de hacerlo en cada uno de los modulo (implicita ) para que se no solo limpio sino que no se condense los modulos, se confundan nombres con otros
"""
import pkg
"""y podemos hacer llamads directa de init"""
print(pkg.URL)

print(pkg.mod_1.func_1())
print(pkg.mod_1.func_2())
print(pkg.mod_2.func_3())
print(pkg.mod_2.func_4())

