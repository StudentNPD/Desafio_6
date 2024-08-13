def estimar_tiempo(pizza):
    n_ingredientes = len(pizza['ingredientes'])
    tiempo = 20 + n_ingredientes * 2
    return tiempo


def mostrar(pizza):
    print(f'Su masa es: {pizza["masa"]}')
    print(f'Su salsa es: {pizza["salsa"]}')
    print('Los ingredientes de su Pizza:')
    
    for ing in pizza['ingredientes']:
        print(f'- {ing}')