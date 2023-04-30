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


class VistaSolido:
    def pedir_datos(self):
        opcion = input(
            "Seleccione el sólido que desea calcular (parámetros requeridos se indican en paréntesis):\n1. Cubo (arista)\n2. Esfera (radio)\n3. Cilindro (radio y altura)\n4. Pirámide (lado de la base y altura)\n5. Cono (radio y altura)\n")
        medidas = input("Ingrese las medidas separadas por comas sin espacios: ").split(",")
        medidas = [float(medida) for medida in medidas]
        return opcion, medidas

    def mostrar_resultado(self, volumen):
        print("El volumen es:", volumen, " unidades cúbicas")