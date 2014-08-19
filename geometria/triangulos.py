import math

from geometria.poligono import Poligono, NaoPoligono


class NaoTriangulo(NaoPoligono):
    pass


class Triangulo(Poligono):
    "Classe base de um triângulo"

    def __init__(self, *lados):
        if len(lados) != 3:
            raise NaoTriangulo

        super().__init__(*lados)

    # Métodos que começam com '_' são "privados" no Python, ou seja, são
    # detalhes de implementação e não devem ser chamados diretamente.
    def _area(self):
        return (self.base * self.altura) / 2


class Isosceles(Triangulo):

    def __init__(self, base, lado):
        self.base = base
        super().__init__(base, lado, lado)

    @property
    def altura(self):
        return math.sqrt(math.pow(self.lados[1], 2) - math.pow(self.base, 2) / 4)

    def area(self):
        return self._area()

class Equilatero(Triangulo):
    "Classe que representa um triangulo equilátero"

    def __init__(self, lado):
        self.base = lado
        super().__init__(lado, lado, lado)

    @property
    def altura(self):
        return (self.base * math.sqrt(3)) / 2

    def area(self):
        return self._area()
