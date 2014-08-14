#!/usr/bin/env python3

class NaoPoligono(Exception):
    pass

class NaoQuadrilatero(NaoPoligono):
    pass

class Poligono(object):
    "Classe que representa um polígono genérico"

    def __init__(self, *lados):
        if len(lados) < 2:
            raise NaoPoligono

        for i in lados:
            if i <= 0:
                raise ArithmeticError

        self.lados = lados

    def num_lados(self):
        return len(self.lados)

class Quadrilatero(Poligono):
    "Classe que representa quadrilátero base"

    def __init__(self, *lados):
        if len(lados) != 4:
            raise NaoQuadrilatero

        super().__init__(*lados)

class Quadrado(Quadrilatero):
    "Classe que representa um quadrado"

    def __init__(self, tamanho):
        super().__init__(tamanho, tamanho, tamanho, tamanho)

    def area(self):
        return self.lados[0] ** 2      

quadrado = Quadrado(8)
print('Área do quadrado:', quadrado.area())
print('Número de lados:', quadrado.num_lados())
