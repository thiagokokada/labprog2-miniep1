from geometria.poligono import Poligono, NaoPoligono


class NaoPentagono(NaoPoligono):
    pass


class Pentagono(Poligono):
    "Classe base de um pentágono"

    def __init__(self, *lados):
        if len(lados) != 5:
            raise NaoTriangulo

        super().__init__(*lados)
