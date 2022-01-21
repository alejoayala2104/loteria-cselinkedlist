from ed.secuenciales.nodo import NodoLSE

class ListaCSE:
    """Clase que implementa el funcionamiento básico de una lista circular simplemente enlazada.
    Permite la utilización de cualquier tipo de dato.

    :param: nodo_cab: Cabecera de la lista
    """    

    def __init__(self):
        """Constructor de la clase ListaCSE. Se crea con un nodo cabecera, por defecto None.
        
        :param nodo_cab: Cabecera de la lista. Por defecto None
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
        """Crea un nodo con el dato suministrado y lo inserta al final de la lista.
        Verifica que el dato ingresado corresponda al tipo de dato ya determinado.
        Retorna un valor booleano dependiendo si se pudo adicionar el dato o no.

        :param nuevo_dato: Dato a insertar al final de la lista
        :type nuevo_dato: object     
        :return: Valor que indica si el adicionamiento fue exitoso o no
        :rtype: bool
        """

        if self.es_vacia():
            self.nodo_cab = NodoLSE(nuevo_dato)
            self.nodo_cab.sig = self.nodo_cab
        else:
            if type(nuevo_dato) is not type(self.nodo_cab.dato):            
                return False
            
            nodo_actual = self.nodo_cab
            while nodo_actual.sig != self.nodo_cab:
                nodo_actual = nodo_actual.sig                
            nuevo_nodo = NodoLSE(nuevo_dato)
            nodo_actual.sig = nuevo_nodo
            nuevo_nodo.sig = self.nodo_cab
        return True

    def insertar(self,pos,nuevo_dato):
        """Crea un nodo con el dato suministrado y lo inserta en una posición válida de la lista.
        Si la lista está vacía, solamente es posible insertar datos en la posición 0.
        Retorna un valor booleano dependiendo si se pudo realizar la inserción o no.

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
        if pos == 0:

            if self.es_vacia():
                self.nodo_cab = NodoLSE(nuevo_dato)
                self.nodo_cab.sig = self.nodo_cab
                return True
            else:
                #Se obtiene el último de la lista
                nodo_actual = self.nodo_cab
                while nodo_actual.sig != self.nodo_cab:
                    nodo_actual = nodo_actual.sig
                
                #Al salir del while nodo_actual es el último de la lista
                nueva_cab = NodoLSE(nuevo_dato)
                vieja_cab = self.nodo_cab
                self.nodo_cab = nueva_cab
                self.nodo_cab.sig = vieja_cab            
                #Se asigna la nueva cabecera al último de la lista
                nodo_actual.sig = self.nodo_cab
                return True

        if pos < 0:
            print("Error: No se puede insertar el dato en una posición negativa")
            return False

        cdr_pos = 0
        nodo_actual = self.nodo_cab
        nodo_anterior = nodo_actual
        nuevo_nodo = NodoLSE(nuevo_dato)

        while cdr_pos < pos:
            cdr_pos += 1
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
        
        #Si se llega al último nodo, pero la posición es la inmediatamente siguiente a la final.
        #Entonces asigne el nuevo dato como nueva cabecera y dirija nuevamente las referencias.
        if pos != len(self) and nodo_actual == self.nodo_cab:
            self.nodo_cab = nuevo_nodo
            nodo_anterior.sig = self.nodo_cab
            nuevo_nodo.sig = nodo_actual            
            return True
        else: #Si no, inserte el nuevo_nodo en la posición deseada.
            nodo_anterior.sig = nuevo_nodo
            nuevo_nodo.sig = nodo_actual
            return True
        return False
        
    def borrar(self, item, por_pos=False):
        """Recorre la lista en búsqueda de un dato determinado para eliminarlo.
        Puede ser configurado para buscar por dato o por posición, su configuración por defecto.

        :param item: Dato o posición a eliminar
        :type item: object
        :param por_pos: Valor que determina la configuración de búsqueda, por defecto Falso
        :type por_pos: bool, optional
        :return: Valor que indica si se encontró el dato o no
        :rtype: bool
        """     
           
        if por_pos:
            # Borrado por posición (cuando por_dato = False e item se asume como posición)
            # La posición tiene que estar en el rango válido de 0 hasta n-1 donde n es el total de nodos de la lista.
            size = self.__len__()
            if(item < 0 or item > (size - 1)):
                print("La posición a buscar está fuera de los limites de la lista")
                return False
            
            if item == 0:            
                #Se obtiene el último de la lista
                nodo_actual = self.nodo_cab
                while nodo_actual.sig != self.nodo_cab:
                    nodo_actual = nodo_actual.sig
                
                #Se borra la cabecera haciendo que el segundo sea el primero en la lista.
                nueva_cab = self.nodo_cab.sig
                self.nodo_cab = nueva_cab
                #Al salir del while el nodo_actual es el último de la lista         
                #Se asigna la nueva cabecera al último
                nodo_actual.sig = self.nodo_cab
                return True
                
            cdr_pos = 0
            nodo_actual = self.nodo_cab
            nodo_anterior = nodo_actual       

            while cdr_pos < item:
                cdr_pos += 1
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig
            
            #Si es el último nodo, el nodo anterior debe apuntar al cabecera.
            if nodo_actual.sig == self.nodo_cab: 
                nodo_anterior.sig = self.nodo_cab
                return True
            else: #Si no, es cualquier nodo intermedio. Se asignan las referencias.
                nodo_anterior.sig = nodo_actual.sig            
                return True

        else:
            
            if item == self.nodo_cab.dato:
                #Se obtiene el último de la lista
                nodo_actual = self.nodo_cab
                while nodo_actual.sig != self.nodo_cab:
                    nodo_actual = nodo_actual.sig
                
                #Se borra la cabecera haciendo que el segundo sea el primero en la lista.
                nueva_cab = self.nodo_cab.sig
                self.nodo_cab = nueva_cab
                #Al salir del while el nodo_actual es el último de la lista         
                #Se asigna la nueva cabecera al último
                nodo_actual.sig = self.nodo_cab
                return True

            nodo_actual = self.nodo_cab
            nodo_anterior = nodo_actual
            #Recorre hasta encontrar el item o hasta el final de la lista
            while nodo_actual.dato != item and nodo_actual.sig != self.nodo_cab:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.sig            
            if nodo_actual.dato == item: #Si lo encontró, nodo_actual es el item buscado.
                if nodo_actual == self.nodo_cab: #Si el item encontrado es la cabecera
                    self.nodo_cab = nodo_actual.sig
                nodo_anterior.sig = nodo_actual.sig #Borrar, ajustando las referencias
                return True
        return False

    def buscar(self,dato_buscar):
        """Recorre la lista en búsqueda de un dato determinado.
        Si lo encuentra, devuelve dicho valor. En otro caso retorna None.

        :return: Dato a buscar, por defecto None
        :rtype: object
        """        

        nodo_actual = self.nodo_cab
        while nodo_actual.dato != dato_buscar and nodo_actual.sig != self.nodo_cab:
            nodo_actual = nodo_actual.sig

        if nodo_actual.dato == dato_buscar:
            return nodo_actual.dato
        return None


    def buscar_cuantos(self,dato_buscar):
        """Recorre la lista en búsqueda de un dato.
        Retorna el número de veces que dicho dato se encuentra en la lista.

        :param dato_buscar: Dato a buscar en la lista
        :type dato_buscar: object
        :return: Contador del número de veces que el dato aparece en la lista
        :rtype: int
        """

        ctr_bus = 0
        for nodo in self:
            if nodo.dato == dato_buscar:
                ctr_bus = ctr_bus+ 1

        return ctr_bus

    def ruleta_rusa(self,pos):
        """Recorre la listaCSE hasta una posición dada.
        Al terminar la lista, se avanza el conteo hasta la posición 0 en adelante
        hasta llegar a pos. Después, se retorna el valor en dicha posición.

        :param pos: Posición del dato a devolver
        :type pos: int
        :return: Dato en la posición indicada
        :rtype: object
        """        

        if pos < 0:
            print("El número ingresado está fuera de los límites de la lista")
            return None
        
        cdr_pos = 0
        nodo_actual = self.nodo_cab
        while cdr_pos < pos:
            cdr_pos += 1
            nodo_actual = nodo_actual.sig

        return nodo_actual

    def recorrer(self,sep=" "):
        """Recorre la lista e imprime cada nodo con un separador recibido como parámetro.

        :param sep: Separador entre cada impresión de nodos, por defecto es " "
        :type sep: str, optional
        """     

        if self.es_vacia(): #Si la lista está vacía, no imprima nada
            return
        else:
            nodo_actual = self.nodo_cab
            while True:
                if nodo_actual.sig == self.nodo_cab:
                    print(str(nodo_actual))
                else:
                    print(str(nodo_actual) , end=sep)
                nodo_actual = nodo_actual.sig
                if nodo_actual == self.nodo_cab:                    
                    break

    def __len__(self):
        """Retorna un entero que determina el tamaño total de la lista.

        :return: Valor que determina cuantos nodos tiene la lista
        :rtype: int
        """

        if self.es_vacia(): #Si la lista está vacía, no haga nada.
            return 0
        else:
            ctr_len = 0
            nodo_actual = self.nodo_cab
            while True:
                ctr_len += 1
                nodo_actual = nodo_actual.sig
                if nodo_actual == self.nodo_cab:
                    break
            return ctr_len

    def __iter__(self):
        """Permite a la listaCSE de las capacidades de un objeto iterable,
        por lo que retona cada nodo haciendo un solo uso de memoria a la vez.
        Para devolver el siguiente nodo, se hace al llamado del método next(),
        siendo aplicado por al objeto iterable.

        :yield: Objeto iterable de la ListaSE
        :rtype: Iterator[YieldType]
        """
      
        if self.es_vacia(): #Si la lista está vacía, no haga nada.
            return
        else:
            nodo_actual = self.nodo_cab
            while True:
                yield nodo_actual
                nodo_actual = nodo_actual.sig
                if nodo_actual == self.nodo_cab:
                    break