#Solicitar variables al usuario
nombre = input("Nombre: ")
altura = input("Altura: ")
edad = input("Edad: ")
estudiante = input("Estdiante: ")

#Imprimir variables del usuario
print("Datos del usuario:")

print(f'Edad:{edad}')
print(f'nombre:{nombre}')
print(f'altura:{altura}')
print(f'estudiante:{estudiante}')

#Verificar el tipo de variable del usuario
print("Tipo de variables del usuario")
print(type(edad))
print(type(nombre))
print(type(altura))
print(type(estudiante))

#Conversion de tipo de variables
nombre = str(nombre)
edad = int(edad)
altura = float(altura)
estudiante = bool(estudiante)

#Verificar el tipo de variable del usuario
print("Tipo de variables del usuario")
print(type(edad))
print(type(nombre))
print(type(altura))
print(type(estudiante))


#Imprimir variables del usuario
print("Datos del usuario:")

print(f'Edad:{edad}')
print(f'nombre:{nombre}')
print(f'altura:{altura}')
print(f'estudiante:{estudiante}')