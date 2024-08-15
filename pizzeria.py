#Desafio 6 Modulo 3
import funciones
import masa
import salsa
import suma_ingredientes

orden = {'masa': 'Masa Tradicional','salsa': 'Salsa de Tomate','ingredientes': ['Queso']}
lista_ingredientes = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo','Jamon','Carne','Tocino','Queso']
 
ingredientes= ['Queso']

print("************************")
print("Bienvenidos Pizzeria JAT")
print("************************")

print("Orden Básica:")
funciones.mostrar(orden,ingredientes)

while True:
    opcion = input('''Seleccione
    1. Cambiar tipo de Masa
    2. Cambiar tipo de Salsa
    3. Agregar Ingredientes
    4. Eliminar Ingredientes
    5. Consultar ingredientes de la pizza
    6. Ordenar con los Ingredientes Actuales
    0. Cancelar pedido.
    > ''')

    if opcion == '1':
        eleccion = input("""Escoja el tipo de Masa:
        T). Tradicional
        D). Delgada
        B). Bordes de Queso
        > """).upper()
        orden = masa.tipo_masa(orden, eleccion)
        aux=input("--->Presione ENTER para continuar")

    elif opcion == '2':
        eleccion = input('''Seleccione su tipo de Salsa:
        T). Tomate
        A). Alfredo
        B). Barbecue
        P). Pesto
        > ''').upper()
        orden = salsa.tipo_salsa(orden, eleccion)

    elif opcion == '3':
        
        i=1
        for elemento in  lista_ingredientes:
            print(f"{i}). {lista_ingredientes[i-1]}") 
            i=i+1
        eleccion = int(input('''Seleccione su Ingrediente: '''))                      
#        1). Tomate
#        2). Champiñones
#        3). Aceituna
#        4). Cebolla
#        5). Pollo
#        6). Jamón
#        7). Carne
#        8). Tocino
#        9). Queso
#        > '''))
        ingredientes = suma_ingredientes.agregar_ingredientes(ingredientes,lista_ingredientes,eleccion)

    elif opcion == '4':
        eleccion = int(input('''Seleccione qué ingrediente quitar:
        1). Tomate
        2). Champiñones
        3). Aceituna
        4). Cebolla
        5). Pollo
        6). Jamón
        7). Carne
        8). Tocino
        9). Queso
        > '''))
        orden = quitar_ingrediente(orden,eleccion)


    elif opcion == '5':
        funciones.mostrar(orden,ingredientes)
        aux=input("--->Presione ENTER para continuar")

    elif opcion == '6':
        tiempo = funciones.estimar_tiempo(ingredientes)
        print(f'Su Pizza estará lista en {tiempo} minutos')
        ordenar = input('Desea ordenar ahora S/N: ').upper()
        if ordenar == 'S':
            print('Gracias por comprar en Pizza JAT')
            print('Disfrute su Pizza!!!!!!')
            exit()
        aux=input("--->Presione Enter para continuar")

    elif opcion == '0':
        print('Su pedido ha sido cancelado. Gracias por Preferirnos Pizza JAT')
        exit()    