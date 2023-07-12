#ni yo se que carajos estoy haciendo D:
import numpy as np
piso_list='|      | A | B | C | D |'
habitacion_list= []
rut_list=[]
precios_list=[]
ejecutar=True
while ejecutar==True:
  print("************************************************")
  print("*                 Casa Feliz                   *")
  print("*                   *Menu*                     *")
  print("*                                              *")
  print("*  1) Comprar departamento                     *")
  print("*  2) Mostrar departamentos ocupados           *")
  print("*  3) Ver listado de compradores               *")
  print("*  4) Mostrar ganancias totales                *")
  print("*  5) Salir                                    *")
  print("*  6) debug lists                              *")
  print("************************************************")
  op=int(input("porfavor seleccione una opcion: "))
  if op==1:
    print("los precios son: ")
    print("Tipo A: 3.800 UF")
    print("Tipo B: 3.000 UF")
    print("Tipo C: 2.800 UF")
    print("Tipo D: 3.500 UF")
    print("porfavor elija un departamento, los departamentos ocupados son: ")
    print(habitacion_list)
    opa=True
    while opa==True:
      valorrandom=str(input('seleccione un cuarto poniendo primero el tipo de departamento seguido de el numero del piso ejemplo: "A9" : '))
      if valorrandom in habitacion_list:
        print("esa habitacion ya fue tomada porfavor ingrese otra habitacion")
      else:
        opa=False
    rutcomprador=int(input('porfavor ingrese su rut sin puntos y sin numero verificador ejemplo: "12.345.678-9 = 12345678" : '))
    rut_list.append(rutcomprador)
    habitacion_list.append(valorrandom)
    print("la operacion se a realizado correctamente")
  if op==2:
    print(habitacion_list)
  if op==3:
    rut_list.sort()
    print(rut_list)
  if op==4:
    matriz= np.array()
  if op==5:
    print("entendido, que tenga un buen dia. . .")
    print("           Brayan Alarcon, 12/07/2023")
    ejecutar=False
  if op==6:
    print(habitacion_list)
    print(rut_list)