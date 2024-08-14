def tipo_masa(orden: dict, eleccion: str) -> dict:
    """
    Agrega el tipo de masa seleccionado a la orden.

    Args:
        orden (dict): Un diccionario que representa la orden actual.
        eleccion (str): Una letra que representa la elección de masa ('T', 'D', o 'B').

    Returns:
        dict: El diccionario de la orden actualizado con el tipo de masa.

    Raises:
        None, pero imprime un mensaje si la elección no es válida.
    """
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
