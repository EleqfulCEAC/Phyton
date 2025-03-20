#Tuplas y sets

#Tupla: ()
 #Estructura de almacenaje que no permite la modificacion
 

#Sets: {}
    #Conjunto de datos cubicos que no permite datos repetidos
var={2,3,4,5,6,6,6,6}
print(var)

 #Funcion para agregar datos en el caso que no se encuentre presente
var.add(1)
print(var)

#Para borrar un valor correspondiente
var.discard(1) 

#Diccionarios: 
varDic= {
 "element1": 1, 
 "element2":3,
 "element3": True,
 }
print(varDic)
print(varDic["element1"])
varDic["element1"] = 525
print(varDic)
print(list(varDic.keys()))
print(list(varDic.values()))
print(list(varDic.items()))

for key, values in varDic.items():
    print(key, "-", values)

    
