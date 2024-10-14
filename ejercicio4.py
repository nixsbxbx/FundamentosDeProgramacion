'''
Dados dos numeros , mostrar la suma, resta, division y multiplicacion
de ambos
entrada: 
numerouno : float
numerodos : float

salida:
suma : float
resta : float
multiplicacion: float
division :float
'''
import math
numerouno = input("Escribe el valor del numero 1: ")
numerouno = float(numerouno)
numerodos = input(" Escribe el valor del numero 2: ")
numerodos = float(numerodos)
suma = (numerouno +numerodos)
resta = (numerouno - numerodos)
multiplicacion = (numerouno * numerodos)
division = (numerouno / numerodos)
print("La suma es de: ", suma)
print("La resta es de: ", resta)
print("La multiplicacion es de: ", multiplicacion)
print("La division es de: ", division)