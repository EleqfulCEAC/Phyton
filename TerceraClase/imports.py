import string as str 
import random as rd
import datetime as dt



print(str.ascii_letters)
print(list(str.ascii_letters))
print(rd.choices([10,2,5], [70,10,20], k=5)) 
'''Funcion que permite sacar una opcion aleatoria del array de elementos, segundo array de probabilidades'''
nuevaFecha = dt.datetime(1994,5,31)
print(nuevaFecha)
nuevaFecha+=dt.timedelta(weeks=1,days=-1)
print(nuevaFecha)
print()