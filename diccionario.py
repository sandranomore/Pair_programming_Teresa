
# definimos un diccionario donde las keys sean strings y lo values también
diccionario1 = { 'lunes':'monday', 'martes':'tuesday', 'miércoles':'wednesday' }

# también podemos tener diccionarios donde las keys sean strings y los values números
diccionario2 = { 'lunes': 1, 'martes':2, 'miércoles':3 }

# o un diccionario donde sean números y los values strings
diccionario3 = { 1:'monday', 2:'tuesday',3:'wednesday' }

# o incluso diccionarios que tengan listas en sus values
diccionario4 = { 'lunes': [1, "peras"], 'martes':[2, "manzanas"], 'miércoles':[3, "brocoli"] }


print("Este es el primer diccionario:", diccionario1)
print("------")
print("Este es el segundo diccionario:", diccionario2)
print("------")
print("Este es el tercer diccionario:", diccionario3)
print("------")
print("Este es el cuarto diccionario:", diccionario4)

# definimos el diccionario con "dict" usando el operador "=" y cada par de clave-valor separado por comas
diccionario5 = dict( jueves = 'thursday', viernes='friday' )

# definimos el diccionario con "dict" usando una lista de tuplas, separando cada tupla por coma. Cada tupla será el par de clave-valor
diccionario6 = dict( [ ('sábado','saturday'), ('domingo','sunday') ] )

print("Este es el quinto diccionario:", diccionario5)
print("------")
print("Este es el sexto diccionario:", diccionario6)
print("------")

# definimos una lista con lo que serán nuestras futuras keys
claves = ['jueves', 'viernes', 'sabado']

# establecemos el valor predeterminado de lo que serán nuestro futuros values. En este caso todos tendrán el valor de una lista vacía
valor_predeterminado = []

# definimos el diccionario usando 
diccionario7 = dict.fromkeys(claves, valor_predeterminado)

print("Este es el septimo diccionario:", diccionario7)
print("------")

# lo primero que vamos a definir es un diccionario. En este caso vamos a crear un diccionario con dos claves o keys las cuales van a ser "nombres" y "nota"
# los values serán listas donde almacenaremos los nombres de las alumnas y sus notas

diccionario_alumnas = {"nombres": ["Lola", "Marta", "Lorena"], "notas": [8, 9, 6]}
print("El diccionario que hemos creado es: ", diccionario_alumnas)

#vamos a usar el método len para saber cuantos pares de clave-valor tenemos en el diccionario con la función len()
print("La cantidad de pares de clave-valor del diccionario es: ", len(diccionario_alumnas))

#vamos a sacar todas las claves del diccionario
print("Las keys del diccionario son:", diccionario_alumnas.keys())

#vamos a sacar todas los valores del diccionario
print("Las keys del diccionario son:", diccionario_alumnas.values())

# vamos a sacar todos los apres de claves-valores que tenemos en el diccionario
print("Los pares de clave-valor del diccionario son: (ESTO NOS DEVUELVE UNA LISTA DE TUPLAS)", diccionario_alumnas.items())
