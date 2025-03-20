import math


"""var = "hola"    
var2 = "adios"
var3 = "hasta luego"
var4 = "hasta pronto"
print(var, var2, var3, var4, end="++",sep="?")"""


#Ejercicio 1
def calculo(text):
    result = int(input(text))
    return result

"""base = calculo("Introduce la base")
altura = calculo("Introduce la altura")
area = base*altura/2
print(area)"""

#Ejercicio 2
"""celcius = calculo("Introduce la temperatura en celcius")
def toFarenheit(weather):
    farenheit = (weather * 9 ) / 5 + 32
    return farenheit

print(toFarenheit(celcius))"""

#Ejercicio 3
"""radio = calculo("dame el radio de tu circulo")
def getPerimetro(radio):
    perimetro = (3.14 * 2) * radio
    return perimetro

perimetro = round(getPerimetro(radio))
print(perimetro)

def getArea(radio):
    area = 3.14 * radio**2
    return area

area = getArea(radio)
print(area)"""


#Ejercicio 4
"""numero = calculo("introduce el numero")
result = numero % 2
if ( result == 0):
    print("Es par")
else: print("Es impar")"""

#Ejercicio 6
Base = calculo("Dame el valor de la base del triangulo")
Altura = calculo("Dame el valor de la altura del triangulo")

Area = Base*Altura/2
print("El area del triangulo es: " + str(Area)) 
Hipotenusa = math.pow(Base, 2) + math.pow(Altura,2)
Hipotenusa = math.sqrt(Hipotenusa)
Perimetro = Base + Altura + Hipotenusa
print("El perimetro del triangulo es: " + str(Perimetro))


