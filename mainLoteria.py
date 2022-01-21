import sys, random
from PyQt5 import QtWidgets, QtCore
from loteria import Loteria, Premio, Concursante

class AppLoteria(QtWidgets.QWidget):
    """Clase que crea un QWidget para mostrar una interfaz gráfica del funcionamiento
    de una lotería.
    """

    def __init__(self, *args, **kwargs):
        """Constructor de la AppLotería, en él se crean todos los elementos de la interfaz gráfica.
        """

        super().__init__(*args,*kwargs)

        # Variables globales        
        self.loteria = Loteria(0.0) #Se inicia la loteria sin valor de boleta aún

        # 1.Widgets BOLETERIA
        self.lyoutBoleteria = QtWidgets.QFormLayout()              
        
        self.lEditCostoBol = QtWidgets.QLineEdit()
        self.btnGuardarCostoBol = QtWidgets.QPushButton('Guardar')
        self.btnResetearLoteria = QtWidgets.QPushButton('Resetear')

        self.btnesBoleteria = QtWidgets.QHBoxLayout() 
        self.btnesBoleteria.addWidget(self.btnGuardarCostoBol)
        self.btnesBoleteria.addWidget(self.btnResetearLoteria)

        self.lyoutBoleteria.addRow('BOLETERÍA',None)
        self.lyoutBoleteria.addRow('Costo boleta:',self.lEditCostoBol)
        self.lyoutBoleteria.addRow(None, self.btnesBoleteria)

        # 2.Widgets MANEJO DE PREMIOS        
        self.lyoutMnjPremios = QtWidgets.QVBoxLayout()

        #Datos
        self.lyoutDatosPremios = QtWidgets.QFormLayout()
        self.lEditNomPremio = QtWidgets.QLineEdit()
        self.lEditValPremio = QtWidgets.QLineEdit()        

        self.lyoutDatosPremios.addRow('MANEJO DE PREMIOS',None)
        self.lyoutDatosPremios.addRow('Nombre:',self.lEditNomPremio)
        self.lyoutDatosPremios.addRow('Valor:',self.lEditValPremio)

        #Se agrupa los botones en un QHbox y los añade
        self.btnAgregarPremio = QtWidgets.QPushButton('Guardar')
        self.btnEstPremio = QtWidgets.QPushButton('Estadísticas')
        self.btnesMnjPremios = QtWidgets.QHBoxLayout()
        self.btnesMnjPremios.addWidget(self.btnAgregarPremio)
        self.btnesMnjPremios.addWidget(self.btnEstPremio)        
        
        self.lyoutMnjPremios.addLayout(self.lyoutDatosPremios)
        self.lyoutMnjPremios.addLayout(self.btnesMnjPremios)

        # 3. Widgets VENDER BOLETAS
        self.lyoutVenderBol = QtWidgets.QFormLayout()

        self.lEditNomConcur = QtWidgets.QLineEdit()
        self.btnRegistrarConcur = QtWidgets.QPushButton('Registrar')

        self.lyoutVenderBol.addRow('VENDER BOLETAS',None)
        self.lyoutVenderBol.addRow('Nombre del concursante:',self.lEditNomConcur)
        self.lyoutVenderBol.addRow(self.btnRegistrarConcur,None)

        # 4. Se agrupa lo anterior en un QHbox
        self.lyoutSuperior = QtWidgets.QHBoxLayout()
        self.lyoutSuperior.addLayout(self.lyoutBoleteria)
        self.lyoutSuperior.addLayout(self.lyoutMnjPremios)
        self.lyoutSuperior.addLayout(self.lyoutVenderBol)

        # 5. Widgets INFORMACIÓN
        self.lyoutMitad = QtWidgets.QVBoxLayout()

        self.lblInfo = QtWidgets.QLabel('INFORMACIÓN')
        self.tEditInfo = QtWidgets.QTextEdit()
        self.tEditInfo.setReadOnly(True)
        # Se agrupan los dos botones en un HBox
        self.btnesInfo = QtWidgets.QHBoxLayout()
        self.btnGenInforme = QtWidgets.QPushButton('Generar informe')
        self.btnLimpiarInfo = QtWidgets.QPushButton('Limpiar')
        self.btnesInfo.addWidget(self.btnGenInforme)
        self.btnesInfo.addWidget(self.btnLimpiarInfo)

        self.btnSortear = QtWidgets.QPushButton('¡SORTEAR!')
        self.btnSortear.setMinimumHeight(50)

        self.lyoutMitad.addWidget(self.lblInfo)
        self.lyoutMitad.addWidget(self.tEditInfo)
        self.lyoutMitad.addLayout(self.btnesInfo)
        self.lyoutMitad.addWidget(self.btnSortear)
        
        # 6. Widgets ULTIMO GANADOR
        self.lyoutInferior = QtWidgets.QFormLayout()

        self.lEditUltGanador = QtWidgets.QLineEdit()
        self.lEditUltGanador.setReadOnly(True)
        self.lEditUltGanador.setMinimumHeight(30)
        self.lyoutInferior.addRow('Último ganador',self.lEditUltGanador)

        self.lyoutPrincipal = QtWidgets.QVBoxLayout()
        self.lyoutPrincipal.addLayout(self.lyoutSuperior)
        self.lyoutPrincipal.addLayout(self.lyoutMitad)
        self.lyoutPrincipal.addLayout(self.lyoutInferior)

        self.setLayout(self.lyoutPrincipal)


        # Funcionalidad
        self.btnGuardarCostoBol.clicked.connect(self.guardarCostoBol)
        self.btnAgregarPremio.clicked.connect(self.agregarPremio)
        self.btnRegistrarConcur.clicked.connect(self.registrarConcur)
        self.btnEstPremio.clicked.connect(self.estadisticasPremio)
        self.btnSortear.clicked.connect(self.sortear)
        self.btnGenInforme.clicked.connect(self.generarInforme)
        self.btnLimpiarInfo.clicked.connect(self.limpiar)
        self.btnResetearLoteria.clicked.connect(self.resetearLoteria)
       
        self.setFixedWidth(1000)
        self.setFixedHeight(550)
 
        self.show()

    def guardarCostoBol(self):
        """Método que guarda el valor del costo de la boleta en el objeto lotería de la aplicación.

        :raises Exception: Excepción lanzada cuando el costo de la boleta es negativo o cero.
        """

        costoBol = self.lEditCostoBol.text()
        try:
            costoBol = float(costoBol)
            if costoBol <= 0: # El costo de la boleta debe positivo
                raise Exception()
            else:
                self.loteria.precio_boleta = costoBol #Se asigna el precio al obj loteria           
                self.lEditCostoBol.setEnabled(False)
                QtWidgets.QMessageBox.information(self,
                'Precio guardado','Se guardó el valor de la boleta satisfactoriamente')
                self.generarInforme() 
        except Exception:
            QtWidgets.QMessageBox.critical(self,
            'Error','Ingrese un costo válido de boleta')   

    def agregarPremio(self): 
        """Método que agrega un Premio a la lista de premios de la lotería.

        :raises Exception: Excepción que se lanza cuando el valor del premio es negativo o cero.
        """   

        nomPremio = self.lEditNomPremio.text()
        valPremio = self.lEditValPremio.text()

        if nomPremio and valPremio: #Si las cadenas tienen algo
            try:
                valPremioNew = float(valPremio)
                if valPremioNew <= 0: # El valor del premio debe positivo
                    raise Exception()
                else:
                    #Se crear y añade un premio
                    premio = Premio(nomPremio,valPremio)
                    self.loteria.listaPremios.adicionar(premio)
                    self.loteria.listaPremios.recorrer()

                    #Se limpia los lEdit
                    self.lEditNomPremio.clear()
                    self.lEditValPremio.clear()                    

                    QtWidgets.QMessageBox.information(self,
                    'Premio guardado','Se añadió el premio satisfactoriamente')

                    self.generarInforme() 
            except Exception:
                QtWidgets.QMessageBox.critical(self,
                'Error','Ingrese un valor válido del premio')
        else:
            QtWidgets.QMessageBox.critical(self,
                'Error','Ingrese datos válidos para agregar el premio')

    def registrarConcur(self):
        """Método que agrega un Concursante a la lista de concursantes de la lotería.
        """     

        #Primero se debe verificar que el valor de la boleta ya se ha seleccionado.
        if self.loteria.precio_boleta == 0.0:
            QtWidgets.QMessageBox.critical(self,
                'Error','Antes de vender boletas debe guardar el precio!')
            return

        nomConcu = self.lEditNomConcur.text()

        # Si se escribe un nombre, se crea un objeto concursante
        if nomConcu:           
            concursante = Concursante(nomConcu)
        else:
            QtWidgets.QMessageBox.critical(self,
                'Error','Ingrese datos válidos para registrar el concursante')        
        
        if not self.loteria.listaConcur.es_vacia() and self.loteria.listaConcur.buscar(concursante): #Si el concursante ya existe
            QtWidgets.QMessageBox.warning(self,
                'Error','El concursante ya existe. No se puede registrarlo')
            self.lEditNomConcur.clear()
        else:
            self.lEditNomConcur.clear()
            self.loteria.listaConcur.adicionar(concursante)
            QtWidgets.QMessageBox.information(self,
                'Boleta vendida!','Se vendió la boleta a ' + str(concursante.nombre))
            #Al final actualiza el text edit
            self.generarInforme()        

    def estadisticasPremio(self):
        """Método que busca un Premio en la lista de premios de la lotería, a través de 
        los valores ingresados. Si lo encuentra, muestra las estadísticas de dicho premio
        en relación a los demás existentes en la lotería.
        """    

        self.tEditInfo.clear()#Se limpia el tEdit apriori
        nomPremio = self.lEditNomPremio.text() 
        valPremio = self.lEditValPremio.text()   

        estPremio = "ESTADÍSTICAS PREMIO\n-------------------------------------\n"
        buscar_cuantos = 0.0
        total_premios = 0.0
        porcentaje = 0.0
        if nomPremio and valPremio:            
            premio = Premio(nomPremio,valPremio)            
            if not self.loteria.listaPremios.es_vacia(): #Si la lista no está vacía
                if self.loteria.listaPremios.buscar(premio): #Si lo encuentra
                    estPremio += "Premio: " + str(premio)
                    buscar_cuantos = self.loteria.cuantos_premios(premio)
                    total_premios = len(self.loteria.listaPremios)
                    porcentaje = (buscar_cuantos * 100) / total_premios
                    estPremio += "\nCantidad del mismo premio: " + str(buscar_cuantos)
                    estPremio += "\nCantidad total de premios: " + str(total_premios)
                    estPremio += "\nPORCENTAJE: " + str(porcentaje) + " %"
                    self.tEditInfo.setText(estPremio)
                    self.lEditNomPremio.clear()
                    self.lEditValPremio.clear()
                    return
        else:
            QtWidgets.QMessageBox.critical(self,
                'Error','Ingrese datos válidos para buscar el premio')
            return
        
        QtWidgets.QMessageBox.warning(self,
                'Error','No se encontró el premio')         

    def sortear(self):
        """Método que realiza un sorteo aleatorio entre los concursantes, entregandoles 
        un premio, también aleatorio. El resultado se imprime en un lineEdit de la GUI.
        """

        #Ganador y premio son de tipo NodoLSE
        ganador, premio = self.loteria.sortear(random.randint(0,100),random.randint(0,100))            
        if (ganador,premio) == (None,None): # Si no se pudo realizar el sorteo
            self.lEditUltGanador.setText("No se pudo realizar el sorteo")
        else: # Sorteo exitoso: No puede darse el resultado Concursante, None o None,Premio                                   
            self.lEditUltGanador.setText(str(ganador.dato.nombre) + " ganó el premio " + str(premio.dato))
            self.generarInforme()

    def generarInforme(self):
        """Método que muestra la información de la lotería en el text edit de la GUI.
        """        

        self.tEditInfo.setText(str(self.loteria))   

    def limpiar(self):
        """Método que limpia la información del text edit de la GUI.
        """        

        self.tEditInfo.clear() 

    def resetearLoteria(self):
        """Método que permite cambiar el costo de la boleta de la lotería,
        y que consigo, borra todos los datos ingresados anteriormente para un nuevo sorteo.
        """        

        respuesta = QtWidgets.QMessageBox.question(self,
                'Resetear lotería','Al resetear el costo de la boleta se borrarán todos los datos ingresados. \n¿Está seguro?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if respuesta == QtWidgets.QMessageBox.Yes:
            self.loteria = Loteria(0)
            self.lEditCostoBol.setEnabled(True)
            self.lEditCostoBol.clear()
            self.tEditInfo.clear()
            self.lEditUltGanador.clear()
        
        self.loteria = Loteria(0)
        self.lEditCostoBol.setEnabled(True)

stylesheet = """


QLabel{
    color: Teal;
    font: 14px "Franklin Gothic Medium"
}

QPushButton{
    background-color: Teal;
    color: white;
    font: 14px "Franklin Gothic Medium"
}

QTextEdit{
    color: Teal;
    font: 14px "Franklin Gothic Medium"
}

QLineEdit{
    font: 14px "Franklin Gothic Medium"
}

"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    ventana = AppLoteria()
    ventana.setStyleSheet(stylesheet)
    sys.exit(app.exec_())