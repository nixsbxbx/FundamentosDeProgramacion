'''
programa que calcule el area y perimetro de un rectangulo
a partir de su basey su altura
Entradas:
         base:integer
         altura:integer
Salida: 
         perimetro:integer
         area:integer
Analisis: 
         Se requiere calcular con las formulas para area y perimetro
'''
# input siempre regreesa un string
# para tratarlo como otro dato se debe convertir
print("programa que calcula area y perimetro de un rectangulo")
base = input("Escribe la base del rectangulo: ")
base = int(base)
altura = input("Escribe la altura del rectangulo: ")
altura = int(altura)
area = base * altura
perimetro = base + base + altura + altura
print("El area del rectangulo es: " , area)
print("El perimetro del rectangulo es: " , perimetro)