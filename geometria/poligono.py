class NaoPoligono(Exception):
    pass


class Poligono(object):
    "Classe que representa um polígono genérico"

    def __init__(self, *lados):
        if len(lados) <= 2:
            raise NaoPoligono

        for i in lados:
            if i <= 0:
                raise ArithmeticError

        self.lados = lados

    def num_lados(self):
        return len(self.lados)
