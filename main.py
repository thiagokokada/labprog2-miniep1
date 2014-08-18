#!/usr/bin/env python3

from geometria.quadrilateros import Quadrado
from geometria.triangulos import Equilatero, Isosceles


quadrado = Quadrado(8)
print('Área do quadrado:', quadrado.area())
print('Número de lados:', quadrado.num_lados())

equilatero = Equilatero(5)
print('Área do triangulo equilátero:', equilatero.area())
print('Número de lados:', equilatero.num_lados())

isosceles = Isosceles(2, 6)
print('Área do triangulo isósceles:', isosceles.area())
print('Número de lados:', isosceles.num_lados())
