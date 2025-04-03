import string as str 
import random as rd

def generadorContraseña(longitud = 12, maxC = 3):
    mayusculas = rd.choices(str.ascii_uppercase, k=maxC)
    minusculas = rd.choices(str.ascii_lowercase, k=maxC)
    digitos = rd.choices(str.digits, k=maxC)
    simbolos = rd.choices(str.punctuation, k=maxC)
    caracteres = digitos + minusculas + simbolos + mayusculas
    contraseña = rd.choices(caracteres, k=longitud)
    
   
    print(''.join(contraseña))
    
    
generadorContraseña()