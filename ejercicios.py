# Solicitar la altura del triángulo
altura = float(input("Ingrese la altura del triángulo: "))

# Calcular el área del triángulo
area = (base * altura) / 2

# Imprimir el área del triángulo
print("El área del triángulo es:", area)



#ejercicio 2
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Ingrese el 1 numero: '))
b = int(input('Ingrese el 2 numero: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')



#ejercicio 3
# Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Calcular el cuadrado del número
cuadrado = numero ** 2

# Imprimir el número elevado al cuadrado
print("El número", numero, "elevado al cuadrado es:", cuadrado)



#ejericico 4
# Solicitar al usuario el lado del cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))

# Calcular el área del cuadrado
area = lado ** 2

# Calcular el perímetro del cuadrado
perimetro = 4 * lado

# Imprimir el área y el perímetro del cuadrado
print(f"El área del cuadrado es: {area:.2f}")
print(f"El perímetro del cuadrado es: {perimetro:.2f}")



#ejercicio 5
import math

# Solicitar al usuario el radio y la altura del cilindro
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular el área lateral del cilindro
area_lateral = 2 * math.pi * radio * altura

# Calcular el área total del cilindro
area_total = 2 * math.pi * radio * (altura + radio)

# Calcular el volumen del cilindro
volumen = math.pi * radio ** 2 * altura

# Imprimir el área lateral, área total y volumen del cilindro
print(f"El área lateral del cilindro es: {area_lateral:.2f}")
print(f"El área total del cilindro es: {area_total:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")



#ejercicio 6
# Solicitar al usuario que ingrese tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Sumar los tres números
suma = num1 + num2 + num3

# Calcular el promedio
promedio = suma / 3

# Imprimir el promedio
print(f"El promedio de los tres números es: {promedio:.2f}")



#ejercicio 7 
# conventir euros a dolares
dinero = float(input("ingrese el monto en euros: "))
cambio = dinero*1.08
print("la convesion es",cambio)



#ejercicio 8
radio = float(input("Introduzca el radio del círculo: "))
longitud = 2 * math.pi * radio
area = math.pi * radio ** 2
print(f"La longitud de la circunferencia es: {longitud:.2f}")
print(f"El área del círculo es: {area:.2f}")