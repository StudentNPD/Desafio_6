def tipo_masa():
    masas_disponibles = ["Tradicional", "Delgada", "Bordes de Queso"]
    nueva_masa = input(f"Elige el tipo de masa ({', '.join(masas_disponibles)}): ").capitalize()
    if nueva_masa in masas_disponibles:
        return nueva_masa
    else:
        print("Masa no disponible.")
        return None
