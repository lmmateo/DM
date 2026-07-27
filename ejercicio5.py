# Ejercicio 5
# a) Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma.
#def add_two_numbers(a, b):
#    return a + b
#def area_del_circulo(radio):
#    pi = 3.1416
#    return pi * radio * radio
# c)    Escribe una función llamada add_all_nums que tome un número arbitrario de argumentos y los sume todos. Comprueba si todos los elementos de la lista son tipos numéricos. Si no, dé una valoración razonable.
#def add_all_nums(*args):
#    #Suma todos los valores numéricos pasados
#    for num in args:
#        if not isinstance(num, (int, float)):
#            return "Error: Todos los elementos deben ser números (int o float)"
#    return sum(args)
# Ejemplos de uso
#print(add_all_nums(1, 2, 3, 4, 5))        # Salida: 15
#print(add_all_nums(10.5, 20.3, 5.2))      # Salida: 36.0
#print(add_all_nums(1, 2, "3", 4))         # Salida: Error: Todos los elementos deben ser números (int o float)
# d)    La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit.
#def convert_celsius_to_fahrenheit(celsius):
   #convierte grados Celsius a Fahrenheit
#    return (celsius * 9/5) + 32

#Ejemplos de uso
#print(convert_celsius_to_fahrenheit(0))    # Salida: 32.0
#print(convert_celsius_to_fahrenheit(100))  # Salida: 212.0
#print(convert_celsius_to_fahrenheit(25))   # Salida: 77.0
# e) La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escribe una función que calcule el conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn.
#import math
#def solve_quadratic_eqn(a, b, c):
    #ecuación cuadrática ax² + bx + c = 0
#    discriminante = b**2 - 4*a*c
#    if discriminante > 0:
        # Dos soluciones reales
#        x1 = (-b + math.sqrt(discriminante)) / (2*a)
#        x2 = (-b - math.sqrt(discriminante)) / (2*a)
#        return (x1, x2)
#    elif discriminante == 0:
        # Una solución real (raíz doble)
#        x = -b / (2*a)
#        return (x,)
#    else:
        # Sin soluciones reales
 #       return ()

# Ejemplos
#print(solve_quadratic_eqn(1, -5, 6))    # (3.0, 2.0)  -> x² - 5x + 6 = 0
#print(solve_quadratic_eqn(1, 4, 4))     # (-2.0,)     -> x² + 4x + 4 = 0
#print(solve_quadratic_eqn(1, 2, 5))     # ()          -> x² + 2x + 5 = 0
# f)
#def print_list(lista):
#
#    for elementos in lista:
#        print(elementos)

# Salida
#mi_lista = ['Azure', 'PAM', 'Telco', 'PHP', 'Cyberark']
#print_list(mi_lista)
#g)   Declara una función llamada lista_inversa. Toma una matriz como parámetro y devuelve el reverso de la matriz (use bucles).
#def lista_inversa(lista):
#    lista_invertida = []
#    for i in range(len(lista) - 1, -1, -1):
#        lista_invertida.append(lista[i])
#    return lista_invertida

# Ejemplos
#print(lista_inversa([1, 2, 3, 4, 5]))        
#print(lista_inversa(['a', 'b', 'c', 'd']))  
#print(lista_inversa(['Azure', 'PAM', 'Telco'])) 
# h)Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma.
def add_two_numbers(a=0, b=0):
    return a + b

# Ejemplos
print(add_two_numbers())        
print(add_two_numbers(5))       
print(add_two_numbers(5, 3))  

