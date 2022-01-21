from ed.secuenciales.listaCSE import ListaCSE
import locale

#!/usr/bin/env python
"""La Loteria se realiza con la participación de uno o varios concursantes, que
compran una boleta, para poder ganar un único premio.
En este módulo se implementan las clases Premio, Concursante y Loteria, para
evaluar la utilización del módulo 'ed.secuenciales.listaCSE'
Author : ANDRÉS ALEJANDRO AYALA CHAMORRO
"""
class Premio:
    """Esta clase representa un premio a ser entregado a un feliz ganador, el
    cual tiene como características el nombre y valor
    """

    def __init__(self, nombre, valor):
        """Consructor de la clase Premio
        Parameters
        ----------
        nombre : str
        El nombre del premio
        valor : float
        El valor del premio
        """        
        self.nombre = nombre
        self.valor = valor

    def __eq__(self, otro_premio):
        """Método de comparación por igualdad con otro objeto de tipo Premio,
        según el nombre y el valor
        Parameters
        ----------
        otro_premio : Premio
        El premio con el cual se realiza la comparación de igualdad
        Returns
        -------
        bool
        True, si los dos premios son iguales. False, en caso contrario
        """
        if(self.nombre  == otro_premio.nombre and self.valor == otro_premio.valor):
            return True
        else:
            return False
            
    def __repr__(self):
        """Método que retorna una cadena de presentación del premio
        Returns
        -------
        str
        Una cadena con la presentación del premio, en el formato:
        '[nombre : $ valor_con_separador_de_miles_y_una_cifra_decimal]'
        El valor del premio se tiene que mostrar con separador de miles de
        su localidad (.), en este caso de Colombia, y una cifra decimal
        separadas por coma (,)
        Ejm: '[TV LG 45 pulgadas : $ 1.250.000,0]'
        """
        locale.setlocale(locale.LC_ALL, 'de_DE')
        valor_modif = locale.format('%.1f', float(self.valor), 1)
        return "[" + str(self.nombre) + " : $ " + str(valor_modif) + "]"

        
class Concursante:
    """Esta clase representa al Concursante que participa en un sorteo, y si
    tiene buena suerte, ganará un premio. El concursante solamente se
    identificará a través de su nombre
    """

    def __init__(self, nombre):
        """Consructor de la clase Concursante
        Parameters
        ----------
        nombre : str
        El nombre del Concursante
        """
        self.nombre = nombre

    def __eq__(self, otro_concursante):
        """Método de comparación por igualdad con otro objeto de tipo
        Concursante, según el nombre
        Parameters
        ----------
        otro_concursante : Concursante
        El Concursante con el cual se realiza la comparación de igualdad
        Returns
        -------
        bool
        True, si los dos Concursantes son iguales. False, en caso contrario
        """
        if(self.nombre == otro_concursante.nombre):
            return True
        else:
            return False

    def __repr__(self):
        """Método que retorna una cadena de presentación del Concursante
        Returns
        -------
        str
        Una cadena con la presentación del Concursante, en el formato:
        '(nombre_del_concursante)'
        Ejm: '(Juan Pérez)'
        """
        return "(" + str(self.nombre) + ")"

class Loteria:
    """La Loteria se puede representar como una lista de premios a ser
    sorteados entre una lista de concursantes
    """

    def __init__(self, precio_boleta):
        """Construir la Loteria, con nuevos premios y nuevos concursantes. Es
        necesario conocer el precio de la boleta que tendrá que pagar cada
        concursante
        Parameters
        ----------
        precio_boleta : float
        El precio de la boleta que paga cada concursante
        listaPremios: ListaCSE()
        Lista de premios vigentes para sorteo
        listaConcur: ListaCSE()
        Lista de concursantes vigentes para sorteo, es decir, que no han ganado premios
        dinero_entregado: float
        Total de dinero (en premios) entregado en la lotería
        num_ganadores: int
        Número de concursantes ganadores en la lotería
        """
        self.precio_boleta = precio_boleta
        self.listaPremios = ListaCSE()
        self.listaConcur = ListaCSE()
        self.dinero_entregado = 0.0 #Dinero en premios entregado
        self.num_ganadores = 0 #Número de ganadores de la lotería

    def agregar_premio(self, nuevo_premio):
        """Método que adiciona un nuevo premio al final de la lista de premios
        Parameters
        ----------
        nuevo_premio : Premio
        El nuevo premio a ser adicionado
        Returns
        -------
        bool
        True, si el premio es realmente válido y pudo ser adicionado a la
        lista de premios. False, en caso contrario
        """
        return self.listaPremios.adicionar(nuevo_premio)

    def quitar_premios(self, el_premio):
        """Método que permite quitar todos los premios coincidentes con el
        premio
        Parameters
        ----------
        el_premio : Premio
        El premio que se quita de la lista de premios
        Returns
        -------
        bool
        True, si al menos se elimina un premio de la lista. False, en caso
        contrario
        """
        ctr = 0
        band = False
        for nodo in self.listaPremios:
            if el_premio == nodo.dato:
                self.listaPremios.borrar(el_premio)
                band = True
            ctr += 1
        return band

    def agregar_concursante(self, nuevo_concursante):
        """Método que adiciona un nuevo concursante al final de la lista de
        concursantes, teniendo en cuenta que el nuevo concursante no debe estar
        registrado con anterioridad en la lista
        Parameters
        ----------
        nuevo_concursante : concursante
        El nuevo concursante a ser adicionado
        Returns
        -------
        bool
        True, si el concursante es realmente válido y pudo ser adicionado
        a la lista de concursantes. False, en caso contrario
        """
        if self.listaConcur.es_vacia():
            self.listaConcur.adicionar(nuevo_concursante)
            return True
        elif self.listaConcur.buscar(nuevo_concursante.nombre) is not None:
            self.listaConcur.adicionar(nuevo_concursante)
            return True
        else:
            return False

    def pozo(self):
        """Método que permite cuantificar el valor total de los premios que
        ofrece la loteria
        Returns
        -------
        float
        El valor total acumulado de los premios que tiene la loteria
        """
        valor_acum_premios = 0.0
        for nodo in self.listaPremios:
            premio = nodo.dato
            valor_acum_premios += float(premio.valor)
        
        return valor_acum_premios

    def cuantos_premios(self, un_premio):
        """Método que determina cuántos premios existen de un determinado
        premio
        Parameters
        ----------
        un_premio : Premio
        El premio que se cuantifica, según el número de veces que se
        encuentre en la lista de premios
        Returns
        -------
        int
        El número de veces que un premio se encuentra en la lista de
        premios
        """
        return self.listaPremios.buscar_cuantos(un_premio)

    def sortear(self, pos_conc, pos_premio):
        """Método que permite realizar el sorteo de un premio entre el grupo de
        concursantes. Para maximizar las ganancias del sorteo, hay que tener en
        cuenta que cada sorteo es posible realizarlo cuando el valor sumado de
        todas las boletas vendidas es igual o supera en un 20% el valor total
        de premios.
        Ejm: Si el total de premios suma $101 y el total vendido por boletas
        suma $120 (cuando el costo de la boleta es $10 y el número de boletas
        vendidas o de concursantes es de 12), entonces no es posible realizar
        el sorteo. En cambio, si el total de premios suma $100 y el total de
        vendido por boletas suma $120, entonces si es posible realizar el
        sorteo.
        En el caso de que el premio sea entregado al concursante, ese premio y
        el concursante ganador deberán salir de la lista correspondiente
        Parameters
        ----------
        pos_conc : int
        Un valor entero que determina la posición del concursante en la
        lista
        pos_premio : int
        Un valor entero que determina la posición del premio en la
        lista
        Returns
        -------
        tuple
        Retorna una tupla (concursante, premio), indicando el concursante
        que gano el premio. Puede retornar (None, None) en el caso de que
        no sea posible entregar el premio al concursante
        ATENCIÓN: Nunca sera posible retornar (None, premio) o
        (concursante, None)
        """
        if self.listaConcur.es_vacia() or self.listaPremios.es_vacia():
            return (None,None)

        pozo = self.pozo()
        total_boletas = 0.0
        for concursante in self.listaConcur:
            total_boletas += self.precio_boleta
        
        if total_boletas >= (1.20 * pozo):
            nodoGanador = self.listaConcur.ruleta_rusa(pos_conc)
            nodoPremio = self.listaPremios.ruleta_rusa(pos_premio)

            if nodoGanador != None and nodoPremio != None: #Si no son None

                #Si solo hay uno, entonces al borrar la lista queda vacía
                if len(self.listaConcur) == 1:
                    self.listaConcur = ListaCSE()
                else:
                    self.listaConcur.borrar(nodoGanador.dato)
                
                if len(self.listaPremios) == 1:
                    self.listaPremios = ListaCSE()
                else:                    
                    self.listaPremios.borrar(nodoPremio.dato)

                self.dinero_entregado += float(nodoPremio.dato.valor)
                self.num_ganadores +=1                    
                return (nodoGanador,nodoPremio)
        else:
            return (None,None)

    def __str__(self):
        """Método que construye y retorna una cadena con información de los
        premios y los concursantes actuales
        Returns
        -------
        str
        Una cadena con la presentación del los premios y los concursantes
        en juego, de la forma:
        'Premios: {[premio : $ valor] [premio : $ valor]}
        [$ total_dinero_entregado_en_premios]
        Concursantes: {(concursante) (concursante)}
        [total_de_concursantes_ganadores]'
        Ejms:
        'Premios: {[TV LG : $ 1.000.000,0] [Blu-ray LG : $ 800.000,0]}
        [$ 0]
        Concursantes: {(Pedro) (María) (Juan)}
        [0]'
        'Premios: {}
        [$ 1800000]
        Concursantes: {(Juan)}
        [2]'
        """

        cad_premios = ""
        ctr_premios = 1
        for premio in self.listaPremios:
            if ctr_premios == len(self.listaPremios):
                cad_premios += str(premio)
            else:
                cad_premios += str(premio) + " "
            ctr_premios += 1

        cad_concur = ""
        ctr_concur = 1
        for concur in self.listaConcur:
            if ctr_concur == len(self.listaConcur):
                cad_concur += str(concur)
            else:
                cad_concur += str(concur) + " "
            ctr_concur += 1

        cadena = "Premios: {" + cad_premios + "}\n[$ " + str(self.dinero_entregado) + "]" + "\nConcursantes: {" + cad_concur + "}\n[" + str(self.num_ganadores) + "]"
        return cadena