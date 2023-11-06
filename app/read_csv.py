import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])

"""
El código que proporcionaste es un script de Python que lee un archivo CSV y lo convierte en una lista de diccionarios, donde cada diccionario representa una fila del archivo CSV. Aquí está el paso a paso de lo que hace el código:

1. **Importa el módulo csv**: Este módulo implementa clases para leer y escribir datos tabulares en formato CSV.

2. **Define la función read_csv(path)**: Esta función toma un argumento, `path`, que es la ruta al archivo CSV que quieres leer.

3. **Abre el archivo CSV**: Utiliza la función incorporada `open()` para abrir el archivo CSV en modo de lectura ('r').

4. **Crea un objeto reader**: Utiliza `csv.reader()`, que devuelve un objeto lector que iterará sobre las líneas del archivo CSV. El parámetro `delimiter=','` especifica que las columnas del CSV están separadas por comas.

5. **Obtiene el encabezado del CSV**: Utiliza la función `next()` para obtener la primera línea del archivo CSV, que generalmente contiene los encabezados de las columnas.

6. **Itera sobre las filas restantes del CSV**: Para cada fila en el objeto reader, crea un diccionario donde las claves son los nombres de las columnas (encabezado) y los valores son los valores de las celdas en la fila actual. Añade cada uno de estos diccionarios a la lista `data`.

7. **Devuelve la lista de diccionarios**: Una vez que ha iterado sobre todas las filas del CSV, la función devuelve la lista `data`.

8. **Llama a la función read_csv()**: Si este script se ejecuta como el script principal (es decir, no se importa desde otro script), entonces llama a la función `read_csv()` con la ruta al archivo CSV que quieres leer y almacena el resultado en la variable `data`.

9. **Imprime el primer diccionario en data**: Imprime el primer diccionario en `data`, que representa la primera fila de datos en el archivo CSV.

La función `csv.reader(csvfile, delimiter=',')` es una función del módulo csv de Python que devuelve un objeto lector que convierte las líneas del archivo de entrada en listas de strings utilizando el delimitador especificado, en este caso una coma (','). Cada línea se convierte en una lista separada y cada valor se trata como un string separado.

Un objeto lector en Python es un objeto que proporciona una interfaz de alto nivel para leer datos de un archivo o cualquier otro tipo de stream de texto. En el contexto del módulo `csv`, un objeto lector se crea utilizando la función `csv.reader()`. Este objeto lector convierte las líneas del archivo de entrada en listas de strings.

Cuando se itera sobre un objeto lector, se obtiene una lista por cada línea del archivo. Cada elemento de la lista corresponde a una celda en esa línea del archivo CSV, y el orden de los elementos en la lista corresponde al orden de las celdas en la línea.

Por ejemplo, si tu archivo CSV se ve así:

```
nombre,edad
Alice,20
Bob,25
```

Iterar sobre el objeto lector te daría las siguientes listas:

```python
['nombre', 'edad']
['Alice', '20']
['Bob', '25']
```

Así es como el objeto lector te permite acceder a los datos en un archivo CSV de una manera estructurada y conveniente.
"""
