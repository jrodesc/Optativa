print("""
Hello World
Hola Mundo
Bonjour le monde""")
#hola mundo



nombre_usuario = "Jose"

saldo_cuenta = "150.20"

edad = 24

nombre = "Pepe"

salario = 1800.40

numero_complejo = -100 + 3.2j

print(type(numero_complejo))


#En python todos los valores son objetos
#ya que todos heredan de la clase objeto
#no existen los tipos primitivos, son los tipos basicos

# Declaración de variables
numero_entero = 10
numero_real = 3.14
numero_complejo = -1.23 + 4.5j
cadena = "Hola"
es_par = True

#las listas se señalan con corchetes

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista)

#pueden existir listas anidadas

lista2 = ["cosa", 1, ["casa", "llave", "perro"]]

print(lista2[2][1])
print(lista2[1])


#slicing
print(lista[:])
print(lista[2:4])
print(lista[:6])
print(lista[:-5])


#las tuplas se pueden conventir en listas pero inicialmente son inmutables y se marcan con parentesis
#y no con corchetes
tupla = ("hola", "mundo", "adios","mundo")

#los diccionarios se abren y cierran con llaves y hacen uso del key value, en este caso almeria nos da
#el valor 22
diccionario = {"Almeria": 22, "Barcelona": 19, "Valencia": 28}
print(diccionario)
#asi se elimina un valor del diccionario
del(diccionario["Barcelona"])
print(diccionario)


#conjunto
#un conjunto es una coleccion desordenada de valores unicos
conjunto = {1, 2, 3}




#Ejercicio 1.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Modificar el tercer elemento a 100.
lista_numeros[2] = 100



#Extraer una sublista del 5º al 8º elemento.
sublista = lista_numeros[4:8]
print(sublista)
#Añadir el número 200 al final.
lista_numeros.append(200)
print(lista_numeros)

#Calcular la suma y media de los elementos.
total = sum(lista_numeros)
media = total/len(lista_numeros)

print(total)
print(media)


#Ejercicio 2

coordenadas = (40.7128, -74.0060)

tupla_convexa = list(coordenadas)

tupla_convexa.append(10)

print(tupla_convexa)

coordenadas = tuple(tupla_convexa)


x = coordenadas[0]
z = coordenadas[1]
y = coordenadas[2]

print(x, z, y)

#Ejercicio 3
estudiante = {"nombre": "Jose", "edad": 20, "asignaturas": ["Matematicas", "Ciencias", "Lengua"]}

estudiante["asignaturas"] = "Geografia"
estudiante["edad"] = 21


for clave, valor in estudiante.items():
    print(clave, ":", valor)

