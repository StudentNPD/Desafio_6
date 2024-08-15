def agregar_ingredientes(ingredientes,lista_ingredientes, eleccion):
    
    
    ingredientes.append(lista_ingredientes[eleccion-1])
    print(f'Se ha agregado {lista_ingredientes[eleccion-1]}')

    return ingredientes