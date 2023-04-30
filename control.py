# Controlador
from model import Figura, Solido
from view import VistaFigura, VistaSolido


class ControladorFigura:
    def __init__(self):
        self.figura = Figura()
        self.vista = VistaFigura()

    def calcular_area_perimetro(self):
        opcion, medidas = self.vista.pedir_datos()
        self.figura.opcion = opcion
        self.figura.medidas = medidas
        area, perimetro = self.figura.calcular_area_perimetro()
        self.vista.mostrar_resultado(area, perimetro)


class ControladorSolido:
    def __init__(self):
        self.solido = Solido()
        self.vista = VistaSolido()

    def calcular_volumen(self):
        opcion, medidas = self.vista.pedir_datos()
        self.solido.opcion = opcion
        self.solido.medidas = medidas
        volumen = self.solido.calcular_volumen()
        self.vista.mostrar_resultado(volumen)
