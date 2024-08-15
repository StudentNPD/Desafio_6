def estimar_tiempo(ingredientes):
   # n_ingredientes = len(pizza['ingredientes'])
   # tiempo = 20 + n_ingredientes * 2
    n_ingredientes=len(ingredientes)
    tiempo = 20 + n_ingredientes * 2
    return tiempo


def mostrar(pizza,ingredientes):
    print(f'Su masa es: {pizza["masa"]}')
    print(f'Su salsa es: {pizza["salsa"]}')
    print('Los ingredientes de su Pizza:')
    
    for ing in ingredientes:
        print(f'- {ing}')