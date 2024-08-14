def tipo_masa(orden, eleccion):
    masas = {
        'T': 'Masa Tradicional',
        'D': 'Masa Delgada',
        'B': 'Masa con Bordes de Queso'
    }
    if eleccion in masas:
        orden['masa'] = masas[eleccion]
    else:
        print("Opción de masa no válida.")
    return orden
