from geometria.poligono import Poligono, NaoPoligono

class NaoQuadrilatero(NaoPoligono):
    pass

class Quadrilatero(Poligono):
    "Classe que representa quadrilátero base"

    def __init__(self, *lados):
        if len(lados) != 4:
            raise NaoQuadrilatero

        super().__init__(*lados)


class Retangulo(Quadrilatero):
    def __init__(self, base, altura):
        super().__init__(base, altura, base, altura)

    def area(self):
        return self.lados[0] * self.lados[1]


class Quadrado(Retangulo):
    "Classe que representa um quadrado"

    def __init__(self, tamanho):
        super().__init__(tamanho, tamanho)

