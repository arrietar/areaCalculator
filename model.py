#modelo

import math

#Se tienen dos tipos de objetos: Figura y Solido
#Cada objeto requiere de unos parámetros específicos
#para poder calcular su área perímetro o volumen.

#A las figuras planas sólo se les puede calcular área y perímetro
class Figura:
    def __init__(self, opcion, medidas):
        self.opcion = opcion
        self.medidas = medidas

    def calcular_area_perimetro(self):
        if self.opcion == "1":
            return self.calcular_area_perimetro_rectangulo()
        elif self.opcion == "2":
            return self.calcular_area_perimetro_cuadrado()
        elif self.opcion == "3":
            return self.calcular_area_perimetro_triangulo()
        elif self.opcion == "4":
            return self.calcular_area_perimetro_circulo()
        elif self.opcion == "5":
            return self.calcular_area_perimetro_poligono_regular()
        elif self.opcion == "6":
            return self.calcular_area_perimetro_trapecio()
        else:
            raise ValueError("Opción inválida")


    def calcular_area_perimetro_rectangulo(self):
        b, h = self.medidas
        area = b * h
        perimetro = 2 * (b + h)
        return area, perimetro

    def calcular_area_perimetro_cuadrado(self):
        l = self.medidas[0]
        area = l ** 2
        perimetro = 4 * l
        return area, perimetro

    def calcular_area_perimetro_triangulo(self):
        l1, l2, l3 = self.medidas
        s = sum(self.medidas) / 2
        area = math.sqrt((s - l1) * (s - l2) * (s - l3) * s)
        perimetro = sum(self.medidas)
        return area, perimetro

    def calcular_area_perimetro_circulo(self):
        r = self.medidas[0]
        area = math.pi * r ** 2
        perimetro = 2 * math.pi * r
        return area, perimetro

    def calcular_area_perimetro_poligono_regular(self):
        nl, l = self.medidas
        a = (l / 2) / math.tan(math.pi / nl)
        perimetro = nl * l
        area = nl * l * a / 2
        return area, perimetro

    def calcular_area_perimetro_trapecio(self):
        d1, d2 = self.medidas
        area = d1 * d2 / 2
        perimetro = 2 * math.sqrt(d1 ** 2 + d2 ** 2)
        return area, perimetro


#A los sólidos se les puede calcular volumen
class Solido:
    def __init__(self, opcion, medidas):
        self.opcion = opcion
        self.medidas = medidas

    def calcular_volumen(self):
        if self.opcion == "1":
            return self.calcular_volumen_cubo()
        elif self.opcion == "2":
            return self.calcular_volumen_esfera()
        elif self.opcion == "3":
            return self.calcular_volumen_cilindro()
        elif self.opcion == "4":
            return self.calcular_volumen_piramide()
        elif self.opcion == "5":
            return self.calcular_volumen_cono()
        else:
            raise ValueError("Opción inválida")

    def calcular_volumen_cubo(self):
        lado = self.medidas[0]
        volumen = lado ** 3
        return volumen

    def calcular_volumen_esfera(self):
        radio = self.medidas[0]
        volumen = 4 / 3 * math.pi * radio ** 3
        return volumen

    def calcular_volumen_cilindro(self):
        radio, altura = self.medidas
        volumen = math.pi * radio ** 2 * altura
        return volumen

    def calcular_volumen_piramide(self):
        base, altura = self.medidas
        volumen = 1 / 3 * base ** 2 * altura
        return volumen

    def calcular_volumen_cono(self):
        radio, altura = self.medidas
        volumen = 1 / 3 * math.pi * radio ** 2 * altura
        return volumen

