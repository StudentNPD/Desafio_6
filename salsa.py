def tipo_salsa(orden, eleccion):
    salsas = {
        'T': 'Salsa de Tomate',
        'A': 'Salsa Alfredo',
        'B': 'Salsa Barbecue',
        'P': 'Salsa Pesto'
    }
    if eleccion in salsas:
        orden['salsa'] = salsas[eleccion]
    else:
        print("Opción de salsa no válida.")
    return orden
