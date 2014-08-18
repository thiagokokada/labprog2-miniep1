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
