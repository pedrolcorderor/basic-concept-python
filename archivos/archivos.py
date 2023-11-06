file = open('archivos/texto.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
    print(line)

file.close()

with open('archivos/texto.txt') as file:
    for line in file:
        print(line)
        
""" 
line 1 
line 2
line 3
line 4 
line 5 
"""