import math

from geometria.poligono import Poligono, NaoPoligono


class NaoTriangulo(NaoPoligono):
    pass


class Triangulo(Poligono):
    "Classe base de um triângulo"

    def __init__(self, *lados):
        # Triângulo obrigatoriamente tem três lados
        if len(lados) != 3:
            raise NaoTriangulo

        super().__init__(*lados)

    # Métodos que começam com '_' são "privados" no Python, ou seja, são
    # detalhes de implementação e não devem ser chamados diretamente.
    def _area(self):
        # Esses atributos não existem ainda, e serão implementados nas classes
        # filhas.
        return (self.base * self.altura) / 2


class Isosceles(Triangulo):
    "Classe que define um triângulo isóceles"

    def __init__(self, base, lado):
        # Defino a base como atributo para ser usável no método _area()
        self.base = base
        super().__init__(base, lado, lado)

    # Properties é algo interessante do Python que permite evitar a você criar
    # getters/setters para tudo. Se você precisar realizar o encapsulamento
    # do atributo pode fazer depois que a necessidade surgir, apenas criando
    # um método com o nome do atributo e definindo seu property
    @property
    def altura(self):
        """Retorna a altura do triângulo isósceles

        Retorno: float com a altura do triângulo isósceles
        """

        # Veja a fórmula da altura triângulo isósceles para detalhes =)
        return math.sqrt(math.pow(self.lados[1], 2) - math.pow(self.base, 2) / 4)

    def area(self):
        """Retorna a área do triângulo isósceles

        Retorno: float com a área do triângulo isósceles
        """

        # Usando o método privado definido na classe pai fica fácil definir
        # a área de seus filhos
        return self._area()

class Equilatero(Triangulo):
    "Classe que representa um triangulo equilátero"

    def __init__(self, lado):
        self.base = lado
        super().__init__(lado, lado, lado)

    @property
    def altura(self):
        """Retorna a altura do triângulo Equilatero

        Retorno: float com a altura do triângulo equilátero
        """

        return (self.base * math.sqrt(3)) / 2       

    def area(self):
        """Retorna a área do triângulo equilátero

        Retorno: float com a área do triângulo equilátero
        """

        return self._area()
