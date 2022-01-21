class NodoLSE:
    """Clase que implementa el funcionamiento de un nodo, teniendo aquel un solo puntero de referencia hacia otro nodo.
    """    

    def __init__(self, dato):
        """Constructor de la clase NodoLSE. Recibe como parámetro un dato de cualquier tipo.

        :param dato: Dato que pertenecerá al nodo
        :type dato: object
        """

        self.dato = dato
        self.sig = None

    def __str__(self):
        """Método que retorna una cadena con la impresión del dato, según su clase lo determine.

        :return: Cadena con la información del dato
        :rtype: str
        """   

        return str(self.dato)