"""
antes habia que definir (con el archivo __init__ ) para que un paqueta pudiese ser importado desde otro archivo , habria que crear un archivo clave  llamado __init__.py  para que funcionen los paquetes y despues de la version 3.3 se pueden trabajar los modulos de un paquete como hicimos en main2-pkg.py sin la necesidad del archivo __init__

ahora para que nos sirven 
antes era para declarar lo que era un paquete , ahora se utilizaria para inicializar una variable o importaciones a ese paquete  y cada vez que se ejecuta el paquete (con un modulo o varios  por ejemplo ) el archivo __init__ se ejecutara  una "vez" e inicializara la variables (por ejemplo)

Y Podemos hacer llamadas directas del init

otra forma de usar el init que nosea definir variables cada vez que se importe el paquete .

TODO : y es hacer  imports en __init__ (es una manera explicita ) en vez de hacerlo en cada uno de los modulo (implicita ) para que se no solo limpio sino que no se condense los modulos, se confundan nombres con otros
"""


print("se inicializo  el paquete y soy  init y los demas son los modulos del paquete que se estan llamando dos veces , pero init solo se inicializa una vez")

URL = "use the __init__"

from . import mod_1
print(mod_1.func_1())

"""

?? Ejecutar __init__ directemane error

Entiendo tu confusión. El problema aquí es cómo Python maneja las importaciones relativas y absolutas.

Cuando ejecutas un script directamente, ese script se considera el módulo principal y su directorio se agrega al inicio de `sys.path`. Entonces, cuando intentas `from pkg import mod_1, mod_2` en `__init__.py`, Python busca un paquete o módulo llamado 'pkg' en `sys.path`, pero no puede encontrarlo porque 'pkg' es el directorio actual, no un subdirectorio.

Una solución a este problema es utilizar importaciones relativas en lugar de absolutas. En lugar de `from pkg import mod_1, mod_2`, puedes usar `from . import mod_1, mod_2`. El punto antes de 'import' indica a Python que debe buscar los módulos en el directorio actual.

Por lo tanto, tu archivo `__init__.py` debería verse así:

```python
from . import mod_1, mod_2
```

Espero que esto resuelva tu problema. Si tienes más preguntas, no dudes en preguntar.

!! otro error 

El error `ImportError: attempted relative import with no known parent package` generalmente ocurre cuando intentas ejecutar un módulo dentro de un paquete directamente. Las importaciones relativas dependen del módulo actual, por lo que si estás ejecutando el archivo `__init__.py` directamente, Python no puede determinar el paquete padre.

Una solución es ejecutar el módulo como parte del paquete utilizando la opción `-m` de la línea de comandos de Python. Por ejemplo, si tu estructura de archivos es así:

```
mypackage/
    __init__.py
    mod_1.py
    mod_2.py
```

Y estás en el directorio que contiene `mypackage/`, puedes ejecutar:

```bash
python -m mypackage
```

Esto le dice a Python que ejecute `mypackage/__init__.py` como un script, pero también establece el contexto correcto para que las importaciones relativas funcionen.

Espero que esto te ayude a resolver el problema. Si tienes más preguntas, no dudes en preguntar.

? se ejecuto __init__ como un cript ,aunque al final me aparece un menseje 
?C:\Python311\python.exe: No module named pkg.__main__; 'pkg' is a package and cannot be directly executed
?? Que es?

El mensaje `C:\Python311\python.exe: No module named pkg.__main__; 'pkg' is a package and cannot be directly executed` indica que Python está intentando encontrar un archivo `__main__.py` en tu paquete, que se ejecutaría si tu paquete se ejecuta como un script. 

Cuando ejecutas un paquete con `python -m pkg`, Python busca un archivo `__main__.py` en el paquete `pkg`. Si no encuentra tal archivo, obtienes el error que estás viendo.

Si deseas poder ejecutar tu paquete directamente como un script, puedes agregar un archivo `__main__.py` en tu paquete. Este archivo debe contener el código que te gustaría que se ejecute cuando se ejecuta el paquete.

Si no necesitas esta funcionalidad, puedes ignorar este mensaje de error. No afecta la funcionalidad de tu paquete y tus importaciones relativas deberían funcionar correctamente.
"""
