# Vista
class VistaFigura:
    def pedir_datos(self):
        opcion = input(
            "Seleccione la figura que desea calcular (parámetros requeridos se indican en paréntesis):\n1. Rectángulo (base, altura)\n2. Cuadrado (lado)\n3. Triángulo (lado1, lado2, lado3)\n4. Círculo (radio)\n5. Polígono regular (número de lados, lado)\n6. Rombo (diagonal1, diagonal2)\n")
        medidas = input("Ingrese las medidas separadas por comas sin espacios: ").split(",")
        medidas = [float(medida) for medida in medidas]
        return opcion, medidas

    def mostrar_resultado(self, area, perimetro):
        print("El área es:", area, " unidades cuadradas")
        print("El perímetro es:", perimetro, " unidades")