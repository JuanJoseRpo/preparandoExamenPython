import random
bandas=[]


opcion=None
while opcion !=5: 
  try:  
    print(' ****FESTIVAL ALTAVOZ***')
    print('************************')
    print('1.Registrar Banda')
    print('2.ver el cartel del festival')
    print('3.Buscar Banda')
    print('4.Modificar Banda')
    print('5.Finalizar')
    opcion = int(input("Digita una opcion: "))
    
    if opcion == 1:
      banda={}
      #SE LLENA EL OBJETO BANDA
      banda["id"]=random.randint(1000,2999)
      banda["nombre"]=input('Digite el nombre: ')
      banda["genero"]=input('Digite el genero: ')
      banda["clasificacion"]=input('Digite la clasificacio: ')
      banda["costo"]=int(input('Digite el costo: '))
      banda["Tiempo"]=int(input('Digite el tiempo: '))
      
      # como agrego un diccionario a un arreglo
      bandas.append(banda)
      
    elif opcion == 2:
      #recorriendo una lista para imprimir sus elementos
      for bandaAuxiliar in bandas:
        print(f'nombre: {bandaAuxiliar["nombre"]} genero: {bandaAuxiliar["genero"]}') 
    elif opcion == 3:
      #Buscando un elemnto dentro de una lista
      bandaBuscada= input('Digita la banda que quieres buscar: ')
      for bandaAuxiliar in bandas:
        if bandaAuxiliar['nombre']==bandaBuscada:
          print('oe sisas, si es')
        else:
          print('oe, ese no es, no lo encontraste')   
    elif opcion == 4:
      pass
    elif opcion == 5:
      pass
    else:
      print('****************')
      print('Opcion invalida')
      print('****************')
      print(banda)
  except ValueError:
    print('solo se reciben numeros en esta monda')


