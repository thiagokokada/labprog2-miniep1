from geometria.poligono import Poligono, NaoPoligono


class NaoPentagono(NaoPoligono):
    pass


class Pentagono(Poligono):
    "Classe base de um pentágono"

    def __init__(self, *lados):
        if len(lados) != 5:
            raise NaoTriangulo

        super().__init__(*lados)

class Regular(Pentagono):
    """Implementação de um pentágono regular"""

    def __init__(self, arg):
        super(Regular, self).__init__(5) # outra forma equivalente a super()
        self.aresta = aresta

    def perimetro(self):
        per = self.aresta *self.lados

        return per