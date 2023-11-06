with open('archivos/texto.txt', 'r+') as file:
    """ r+ no permite leer y escribir agregando nuevas lineas , mientras w+ lee y sobreescribe"""
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write(' mas linea\n')
