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
