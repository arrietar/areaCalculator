from model import Figura, Solido
from view import VistaFigura, VistaSolido


def main():
    opcion_figura = input("¿Desea calcular áre y perímetro de una figura? (s/n): ")
    if opcion_figura.lower() == "s":
        vista_figura = VistaFigura()
        opcion, medidas = vista_figura.pedir_datos()
        figura = Figura(opcion, medidas)
        area, perimetro = figura.calcular_area_perimetro()
        vista_figura.mostrar_resultado(area, perimetro)

    opcion_solido = input("¿Desea calcular volumen de un sólido? (s/n): ")
    if opcion_solido.lower() == "s":
        vista_solido = VistaSolido()
        opcion, medidas = vista_solido.pedir_datos()
        solido = Solido(opcion, medidas)
        volumen = solido.calcular_volumen()
        vista_solido.mostrar_resultado(volumen)


if __name__ == '__main__':
    main()
