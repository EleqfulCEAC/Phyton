"""
Ejercicio 1: Crear un diccionario que almacene los nombres de estudiantes 
y sus notas finales. 
Luego, agregar funcionalidad para cambiar la nota de un estudiante y 
mostrar la nota modificada.
""" 
def insertarNombre():  
    nombre = input("Inserte el nombre del estudiante")
    return nombre
    
def insertarNota(): 
    nota = float(input("Inserte la nota del estudiante"))
    return nota

def modifyNota(nombre, nota): 
    estudiantes = registroEstudiantes.keys()
    if estudiantes.__contains__(nombre):
         registroEstudiantes[nombre] = nota
         print("La nota modificada seria: " + str(registroEstudiantes.get(nombre)))
    else: print("No existe ese estudiante")     
    


registroEstudiantes = {}

for i in range(0, 2):
    nombre = insertarNombre()
    nota = insertarNota()
    registroEstudiantes[nombre] = nota


print(registroEstudiantes)
modifyNota(insertarNombre(), insertarNota())
modifyNota(insertarNombre(), insertarNota())
print(registroEstudiantes)