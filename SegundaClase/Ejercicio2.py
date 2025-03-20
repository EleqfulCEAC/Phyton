import math

"""
Ejercicio 2: Dado un diccionario con nombres de empleados y su salario,
calcular el salario medio, el salario más alto y el más bajo.
"""

salariosPorEmpleados = {
    "Angel": 2000,
    "Martin":4000,
    "Maria":8200,
    "Angela":9000
}
nombres = salariosPorEmpleados.items()

sueldos = salariosPorEmpleados.values()

mediaTotal = sum(sueldos) / len(salariosPorEmpleados)
mayorSueldo = max(sueldos)
menorSueldo = min(sueldos)

print("El valor medio de sueldo es: " + str(mediaTotal))
print("El valor mayor de sueldo es: " + str(mayorSueldo))   
print("El valor menor de sueldo es: " + str(menorSueldo))    
      