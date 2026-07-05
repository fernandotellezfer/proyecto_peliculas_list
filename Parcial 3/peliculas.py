import funciones
from peliculas import crud

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(conexionBD):
    print("\n\t\t\t...::: AGREGAR PELICULAS :::... \n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    #Agregar pelicula a la BD
    respuesta=crud.insertar(peli,conexionBD)
    if respuesta:
       funciones.accionExitosa()
    else:
       funciones.accionNoExitosa()
    funciones.esperarTecla()
    
def mostrarPeliculas(conexionBD):
    print("\n\t\t\t...::: MOSTRAR PELICULAS :::... \n")
    pelis=crud.consultar(conexionBD)
    if len(pelis)>0:    
        print("\n\t\tCodigo\t\tPelicula\n")
        for i in pelis:
            print(f"\t\t{i[0]}\t\t{i[i]}")
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ... ")
    funciones.esperarTecla()
    
def limpiarPeliculas(conexionBD):
    print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS :::... \n")
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
    if opc=="si":
        respuesta=crud.vaciar(conexionBD)
        if respuesta:
           funciones.accionExitosa()
        else:
           funciones.accionNoExitosa()
        funciones.esperarTecla
           
        

def buscarPeliculas(pelis,conexionBD):
    print("\n\t\t\t...::: BUSCAR PELICULAS :::... \n")
    peli=input("Escribe la pelicula a buscar: ").upper().strip()
    if peli in pelis:
        print("\n\t\tCodigo\t\tPelicula\n")
        for i in range(0,len(pelis)):
          if peli==pelis[i]:
             print(f"{i+1}\t\t{pelis[i]}")
        funciones.esperarTecla()
    else:
        input("\n\t... ¡No existe la pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis,conexionBD):
    posiciones=[]
    print("\n\t\t\t...::: BORRAR PELICULAS :::... \n")
    peli=input("Escribe la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
          if peli==pelis[i]:
            opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
            while opc!="si" and opc!="no":
              opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
               posiciones.append(i)
        if len(posiciones)>0:
            for i in range(0,len(posiciones)):
                pelis.remove(peli)
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la pelicula a borrar, verifique! ...")
        
def modificarPeliculas(pelis,conexionBD):
    print("\n\t\t\t...::: MODIFICAR PELICULAS :::... \n")
    peli=input("Escribe la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
          if peli==pelis[i]:
               opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
               while opc!="si" and opc!="no":
                 opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
               if opc=="si":
                 pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
                 funciones.accionExitosa() 
    else:
        input("\n\t... ¡No existe la pelicula a modificar, verifique! ...")