from classes.Ciclista import Ciclista
from classes.Escuderia import Escuderia

opcion = 1

ciclistas = []
tiempos=[]

# while(opcion != 3):

#     print("\n1)Ingresar Ciclista\n2)Mostrar Resultados\n3)Salir")
#     opcion = int(input("\nIngrese una opcion: "))

#     if(opcion ==1):
#         ciclista = Ciclista()

#         ciclista.nombre = input("\nNombre: ")
#         ciclista.edad = input("Edad: ")
#         ciclista.pais = input("Pais: ")
#         ciclista.tiempo = float(input("Tiempo(minutos): "))

#         ciclistas.append(ciclista)
#         tiempos.append(ciclista.tiempo)
#     elif(opcion ==2):
#         tiempos.sort()
#  
#         for ciclist in ciclistas:
#             print("\n")
#             ciclist.mostrarDatos()

#         for ciclist in ciclistas:
#             if(ciclist.tiempo == tiempos[0]):
#                 print("\n==================Ganador============== \n")
#                 ciclist.mostrarDatos()
#     elif(opcion ==3):
#         pass
#     else: 
#         print("\nOpcion incorrecta")
costos=[ ]
motores= [ ]
escuderias= [ ]
r=0
m=0
f=0
while(opcion !=4 ):

    print("\n1. Ingresar escuderías")
    print("2. Comprobar cual es la escudería más cara")
    print("3. Comprobar cuantos escuderías tienen motor cuantas mercedes,  Ferrari y  renault")

    opcion = int(input("\ndigite el numero según la opcion: "))

    if opcion == 1:
        salir = False
        escuderia = Escuderia()
        escuderia.nombre=input("\ndigite el nombre de la escuderia : ")
        while(salir == False):
            print("\nEscoje un Motor: ")
            print("\n1)Ferrari\n2)Mercedes\n3)Renault")
            opcion2 = int(input("\nIngrese una opcion: "))

            if(opcion2 == 1):
                escuderia.motor = "Ferrari"
                salir = True
            elif(opcion2 == 2):
                escuderia.motor = "Mercedes"
                salir = True
            elif(opcion2 == 3):
                escuderia.motor = "Renault"
                salir = True
            else:
                print("\nOpcion incorrecta")
                salir = False

        escuderia.piloto=input("ingrese el piloto : ")
        escuderia.costoAnual=float(input("ingrese costo anual : "))

        escuderias.append(escuderia)
        costos.append(escuderia.costoAnual)
        
        motores.append(escuderia.motor)

    elif opcion == 2:
        costos.sort()

        for escuderia in escuderias:
            print("\n")
            escuderia.pintarEscuderia()

        for escuderia in escuderias:
            if(escuderia.costoAnual == costos[len(costos)-1]):
                print("\nLa escuderia con mayor costo anual es: \n")
                print(f"{escuderia.nombre}: {escuderia.costoAnual} <----")
    elif opcion == 3:
        f=motores.count("Ferrari")
        m=motores.count("Mercedes")
        r=motores.count("Renault")

        print('\nmotores ferrari: '+ str(f))
        print('motores renault: '+ str(r))
        print('motores mercedes: '+ str(m))

    elif opcion == 4:
        pass
    else:
       print("\nintrodujo una numero invalido")