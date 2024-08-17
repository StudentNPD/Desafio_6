# Que se permita modificar ingredientes (agregar y eliminar). Actualmente, la
# pizzería trabaja con los siguientes ingredientes: Tomate, Champiñones,
# Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso
agregados = {
    1: "Tomate",
    2: "Champiñones",
    3: "Aceituna",
    4: "Cebolla",
    5: "Pollo",
    6: "Jamón",
    7: "Carne",
    8: "Tocino",
    9: "Queso",
}


def agregar_ingrediente(ingredientes):
    i = 0
    while i < 3:
        eleccion = int(
            input(
                """Seleccione su Ingrediente:
        1) Tomate
        2) Champiñones
        3) Aceituna
        4) Cebolla
        5) Pollo
        6) Jamón
        7) Carne
        8) Tocino
        9) Queso\n
        > """
            )
        )
        ingredientes.append(agregados[eleccion])
        print(f"Haz Agregado: {ingredientes}")
        i = i + 1

        if i == 3:
            break

        while True:
            pregunta = input("¿Desea agregar otro ingrediente? Escriba s / n: ").lower()
            if pregunta == "s":
                break
            elif pregunta == "n":
                return ingredientes
            else:
                print("Por favor ingrese s / n")

    return ingredientes


# def agregar_ingrediente(ingredientes):
#     i=0
#     while i < 3 :
#         eleccion = int(input('''Seleccione su Ingrediente:
#         1) Tomate
#         2) Champiñones
#         3) Aceituna
#         4) Cebolla
#         5) Pollo
#         6) Jamón
#         7) Carne
#         8) Tocino
#         9) Queso\n
#         > '''))
#         ingredientes.append(agregados[eleccion])
#         print(f"Haz Agregado: {ingredientes}")
#         i = i + 1

#         if i == 3:
#             break

#         pregunta = input('¿Desea agregar otro ingrediente? Escriba SI o NO: ').lower

#         if pregunta == 'S':
#             continue
#         elif pregunta == 'N':
#             break
#         else:
#             print('Por favor ingrese algo')

#     return ingredientes


def eliminar_ingrediente(ingredientes):
    i = 0
    for ingrediente in ingredientes:
        print(i, ingrediente)
        i += 1
    eliminar = int(input("Escoga Ingrediente que desea eliminar:"))
    ingredientes.remove(ingredientes[eliminar])
    return ingredientes
