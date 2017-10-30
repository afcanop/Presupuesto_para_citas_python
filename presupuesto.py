#constantes
entrada_cine = 6000
papas_fritas= 4000
porcines = 0
entradas_cine = 0
#ingreso del presupuesto
print("ingrese por favor su presupuesto mayor a mil pesos")
presupuesto =  int(input())


if presupuesto > 1000:

    if presupuesto >= papas_fritas:
        porcines = int(presupuesto / papas_fritas)
        print ("presupuesto para comer papas fritas para comer:"+ str(porcines) + " porciones")
    else:
        print ("presupuesto no valido para comer papitas")

    if presupuesto >= entrada_cine:
        entradas_cine = int( presupuesto / entrada_cine)
        print ("presupuesto para "+ str(entradas_cine) + " entradas a cine normal")
    else:
        print ("presupuesto no valido cine")

else:
    print("presupuesto no valido")