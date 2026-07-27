#Ejercicio 4.- a)	Itera de 0 a 10 usando cualquier ciclo
#for i in range(11):
#   print(i)
#Ejercicio 4.- b)	Itera de 10 a 0 usando cualquier ciclo
#for a in range(10, -1, -1):
 #   print(a)
 # Hacemos 7 iteraciones (del 1 al 7)
 #c)	Escribe un ciclo que haga siete llamadas a print(), de modo que obtengamos en la salida
#for a in range(1, 8):
 #   print('#' * a)
# d) Utiliza ciclos anidados para crear lo siguiente:
# Ciclo externo para las 8 filas
#for i in range(8):          # Ciclo exterior: 8 filas
 #   for j in range(8):      # Ciclo interior: 8 columnas
  #      print("#", end=" ") # Imprime # con espacio, sin saltar línea
   # print()                 # Salto de línea al terminar cada fila
#e) Imprime el siguiente patrón:
 #for a in range(11):
 #resultado = a * a
 #print(f"{a} x {a} = {resultado}")
 # e)	Itera a través de la lista, ['Python', 'Numpy','Pandas','Django', 'Flask'] usando un ciclo
#lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
#for elemento in lista:
 #   print(elemento)
 #f) Utiliza el ciclo for para iterar de 0 a 100 e imprimir solo números pares.
#for num_par in range(0, 101):
 #   if num_par % 2 == 0:
  #      print(num_par)
 #h) g)	Utiliza el ciclo for para iterar de 0 a 100 e imprimir solo números impares
for numero in range(1, 101)[::2]:
    print(numero)