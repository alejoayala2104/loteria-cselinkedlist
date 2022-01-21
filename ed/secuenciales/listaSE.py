from ed.secuenciales.nodo import NodoLSE
    
class ListaSE:
    """Clase que implementa el funcionamiento basico de una lista simplemente enlazada.
    Permite la utilización de cualquier tipo de dato.

    :param: nodo_cab: Cabecera de la lista    
    """

    def __init__(self):
        """Constructor de la clase ListaSE. Se crea con un nodo cabecera, por defecto None.

        :param nodo_cab: Cabecera de la lista. Por defecto None.
        :type nodo_cab: NodoLSE
          
        """

        self.nodo_cab = None

    def es_vacia(self):
        """Determina si la lista está vacía o no.

        :return: Valor que verifica si el nodo cabecera tiene referencia determinada
        :rtype: bool
        """

        return self.nodo_cab is None
      
    def adicionar(self,nuevo_dato):    
        """Crea un nodo con el dato suministrado y lo inserta al final de la lista.   Verifica que el dato ingresado corresponda al tipo de dato manejado por la lista. Retorna un valor booleano dependiendo si se pudo adicionar el dato o no.

        :param nuevo_dato: Dato a insertar al final de la lista   
        :type nuevo_dato: object     
        :return: Valor que indica si el adicionamiento fue exitoso o no
        :rtype: bool
        """ 

        if self.es_vacia():
            self.nodo_cab = NodoLSE(nuevo_dato)
        else:
            if type(nuevo_dato) is not type(self.nodo_cab.dato):            
                return False

            nodo_actual = self.nodo_cab
            while nodo_actual.sig is not None:
                nodo_actual = nodo_actual.sig
            nodo_actual.sig = NodoLSE(nuevo_dato)           
        return True
       
   
    def insertar(self,nuevo_dato,pos):
        """Crea un nodo con el dato suministrado y lo inserta en una posición válida de la lista. Si la lista está vacía, solamente es posible insertar datos en la posición 0. Retorna un valor booleano dependiendo si se pudo realizar la inserción o no.

        :param nuevo_dato: Dato a insertar en la posición dada        
        :param pos: Número de la posición donde se insertará en dato
        :type nuevo_dato: object
        :type pos: int
        :return: Valor que indica si la inserción fue exitosa o no
        :rtype: bool
        """               
        
        if self.es_vacia() and pos!=0:
            print("La lista está vacía, solo se puede insertar datos en la posición 0")
            return False

        # Validación del tipo de dato: Si la lista no está vacía, valide el tipo de dato a insertar.
        if self.es_vacia() != True:
            if type(nuevo_dato) is not type(self.nodo_cab.dato):
                print("El tipo de dato a insertar no coincide con el tipo de dato de los objetos de la lista.")
                return False
             
        # Si se inserta en la posición 0.
        if(pos == 0):
            nodo_posterior = self.nodo_cab
            self.nodo_cab = NodoLSE(nuevo_dato)
            self.nodo_cab.sig = nodo_posterior
            return True
        
        # Algoritmo que con ayuda de una variable auxiliar recorre la lista
        # a través de la referencia del nodo siguiente.
        nodo_actual = self.nodo_cab
        nodo_anterior = nodo_actual
        cdr_pos = 0 
        while cdr_pos < pos and nodo_actual:
            cdr_pos += 1
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
                
        if(nodo_actual and pos > 0):
            nuevo_nodo = NodoLSE(nuevo_dato)
            nodo_anterior.sig = nuevo_nodo
            nuevo_nodo.sig = nodo_actual
            return True
        else:
            print("La posición " + str(pos) + " está fuera de los límites de la lista.")
        return False
   
    def buscar(self, item, por_dato=True):
        """Recorre la lista en búsqueda de un dato determinado. Puede ser configurado para buscar por posición o por dato, su configuración por defecto.

        :param item: Dato o posición a buscar en la lista
        :type item: object
        :param por_dato: Valor que determina la configuración de búsqueda, True por defecto
        :type por_dato: bool, optional
        :return: Valor que indica si se encontró el dato o no
        :rtype: bool
        """  

        if por_dato: # Búsqueda por dato
            nodo_actual = self.nodo_cab
            while nodo_actual and nodo_actual.dato != item:
                nodo_actual = nodo_actual.sig
            if nodo_actual:
                return nodo_actual.dato
            return None
            #return nodo_actual.dato if nodo_actual else None
        else:
            # Búsqueda por posición (cuando por_dato = False e item se asume como posición)
            # La posición tiene que estar en el rango válido de 0 hasta n-1 donde n es el total de nodos de la lista.
            size = self.__len__()
            if(item < 0 or item > (size - 1)):
                print("La posición a buscar está fuera de los limites de la lista")
                return None
                        
            nodo_actual = self.nodo_cab
            ctr_pos = 0
            # Si ciclo llega antes de la posición, porque al terminarse, nodo_actual es el nodo en la posición buscada.
            while ctr_pos < item and nodo_actual:
                ctr_pos += 1
                nodo_actual = nodo_actual.sig
            # ¿Se encontró el nodo?
            if nodo_actual:
                return nodo_actual.dato
            return None

    def recorrer(self):        
        """ Recorre la lista imprimiendo cada nodo contenido en ella.
        """

        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.sig

    # Verificar que pos no sea negativa.
    def borrar_pos(self,pos):
        """Recorre la lista y elimina un nodo en una posición dada.

        :param pos: Número de la posición del nodo a borrar
        :type pos: int
        :return: Nodo borrado
        :rtype: NodoLSE
        """         
        nodo_actual = self.nodo_cab
        cr_pos = 0

        # Ciclo que recorre la lista y termina cuando 
        # nodo_actual ubica una posición válida a borrar.
        while cr_pos < pos and nodo_actual:
            cr_pos += 1
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
                
        # True: Se encuentra el nodo a ser borrado. También se valida que la posición sea mayor o igual a 0.
        if nodo_actual and pos >= 0: 
            if self.nodo_cab is nodo_actual: # Si nodo_actual es el primer nodo.
                self.nodo_cab = self.nodo_cab.sig
            else: # Si nodo_actual corresponde a cualquier otro nodo intermedio o final.
                nodo_anterior.sig = nodo_actual.sig # El último nodo retorna None.
            return True
        return False
   
    def borrar(self, dato_borrar):
        """Elimina todas las ocurrencia del dato a borrar en la lista. Devuelve un valor booleano que determina si se elminó al menos un nodo.

        :param dato_borrar: Dato a borrar recursivamente en la lista
        :type dato_borrar: object
        :return: True -> Si se elimina al menos un nodo. De lo contrario, False.
        :rtype: bool
        """

        nodo_actual = self.nodo_cab
        nodo_anterior = nodo_actual
        nodo_borrado = False # Bandera que determina si un nodo fue borrado.

        #Ciclo que recorre la lista hasta que llega el último elemento.
        while nodo_actual:            
            if(nodo_actual.dato == dato_borrar):
                if(self.nodo_cab is nodo_actual): # Si el nodo a borrar es el primero en la lista.
                    self.nodo_cab = nodo_actual.sig                    
                    nodo_actual = self.nodo_cab # Ahora, el nodo_actual será el nuevo nodo cabecera.
                else: # Si nodo_actual corresponde a cualquier otro nodo intermedio o final.
                    nodo_anterior.sig = nodo_actual.sig
                    nodo_actual = nodo_anterior # Se resetea las variables auxiliares
                nodo_borrado = True
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
        return nodo_borrado

    def __len__(self):
        """Retorna un entero que determina el tamaño total de la lista

        :return: Valor que determina cuantos nodos tiene la lista
        :rtype: int
        """

        ctr_len = 0
        nodo_actual = self.nodo_cab            
        while nodo_actual:
            ctr_len += 1            
            nodo_actual = nodo_actual.sig
        return ctr_len

    def __str__(self):
        """Devuelve una cadena con los datos de cada nodo en un formato determinado.

        :return: Cadena con la información de todos los nodos de la lista
        :rtype: str
        """

        nodo_actual = self.nodo_cab
        cadena = ""
        while nodo_actual:
            cadena += "[" + str(nodo_actual)  + "]"
            if nodo_actual.sig:
                cadena += "\n!\n"
            nodo_actual = nodo_actual.sig
        return cadena

    def __iter__(self):
        """Permite a lista enlazada de las capacidades de un objeto iterable,
        por lo que retona cada nodo haciendo un solo uso de memoria a la vez.
        Para devolver el siguiente nodo, se hace al llamado del método next(),
        siendo aplicado por al objeto iterable.
        :return: Objeto iterable de la ListaSE
        :rtype: Iterator[YieldType]
        """
        
        nodo_actual = self.nodo_cab
        while nodo_actual:
            yield nodo_actual
            nodo_actual = nodo_actual.sig