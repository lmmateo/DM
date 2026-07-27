# Crea un diccionario vacío llamado perro
perro = {}
# b)	Agrega nombre, color, raza, patas y edad al diccionario de perros.
perro = {
	"nombre": "Solovino",
	"color": "Negro",
    "raza": "pitbull",
    "patas": 4,
    "edad": 1
}
print(perro)
# Crea un diccionario de estudiantes y agregue nombre, apellido, sexo, edad, estado civil
estudiantes = {
    "nombre": "Luis",
    "apellido": "Mateo",
    "sexo": "Masculino",
    "edad": 42,
    "estado_civil": "Casado"
}
print(estudiante)
# d)	habilidades, país, ciudad y dirección como claves para el diccionario
estudiante = {
    "nombre": "Luis",
    "apellido": "Mateo",
    "sexo": "Masculino",
    "edad": 42,
    "estado_civil": "Casado"
}
# Agregamos las habilidades y claves:
estudiante["habilidades"] = ["Azure", "PAM", "Telco"]
estudiante["pais"] = "México"
estudiante["ciudad"] = "Ciudad de México"
estudiante["direccion"] = "Av. Périferico norte"
print(len(estudiante))
# f) Obtén el valor de las habilidades y verifica el tipo de datos, debería ser una lista.
estudiante = {
    "nombre": "Luis",
    "apellido": "Mateo",
    "sexo": "Masculino",
    "edad": 42,
    "estado_civil": "Casado"
}	
# Agregamos las habilidades y claves:
estudiante["habilidades"] = ["Azure", "PAM", "Telco"]
estudiante["pais"] = "México"
estudiante["ciudad"] = "Ciudad de México"
estudiante["direccion"] = "Av. Périferico norte"
# 1. valor de las habilidades
habilidades = estudiante["habilidades"]
# 2. Imprimir las habilidades
print("habilidades:", habilidades)
# 3. Obtener y verificar el tipo de dato
tipo_dato = type(habilidades)
print("Tipo de dato:", tipo_dato)
# 4. Comprobación 
es_lista = isinstance(habilidades, list)
# g)	Modifica los valores de las habilidades agregando una o dos habilidades.
estudiante['habilidades'].append('HTML')
#claves = list(estudiante.keys())
# i) Obtén los valores del diccionario como una lista
#valores = list(estudiante.values())
# j) Cambia el diccionario a una lista de tuplas usando el método items().
#lista_de_tuplas = list(estudiante.items())
# k) k)	Elimina uno de los elementos del diccionario.
#del estudiante["direccion"]
del estudiante 
print("¿Es una lista?:", es_lista)