#!/usr/bin/env python3

from geometria.quadrilateros import Quadrado
from geometria.triangulos import Equilatero


quadrado = Quadrado(8)
print('Área do quadrado:', quadrado.area())
print('Número de lados:', quadrado.num_lados())

equilatero = Equilatero(5)
print('Área do triangulo:', equilatero.area())
print('Número de lados:', equilatero.num_lados())