def tipo_masa(abrv, masa):
    masas = {
        'T': 'Masa Tradicional',
        'D': 'Masa Delgada',
        'B': 'Bordes de Queso'
    }
    if masa in masas:
        abrv['masa'] = masas[masa]
        print(f"Masa cambiada a {masas[masa]}")
    else:
        print("Opción de masa no válida")
    return abrv

