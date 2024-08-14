def tipo_salsa(orden: dict, eleccion: str) -> dict:
    """
    Agrega el tipo de salsa seleccionado a la orden.

    Args:
        orden (dict): Un diccionario que representa la orden actual.
        eleccion (str): Una letra que representa la elección de salsa ('T', 'A', 'B', o 'P').

    Returns:
        dict: El diccionario de la orden actualizado con el tipo de salsa.

    Raises:
        None, pero imprime un mensaje si la elección no es válida.
    """
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
