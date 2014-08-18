from geometria.poligono import Poligono, NaoPoligono


class NaoQuadrilatero(NaoPoligono):
    pass

class Quadrilatero(Poligono):
    "Classe que representa quadrilátero base"

    # '*' em funções permite que você passe qualquer número de itens de entrada.
    # O Python converte isso para uma tupla:
    # Exemplo: exemplo(*exemplos) -> exemplo('teste1', 'teste2', 'teste3')
    # Resultado: ('teste1', 'teste2', 'teste3')
    def __init__(self, *lados):
        # Todo quadrilátero tem 4 lados
        if len(lados) != 4:
            raise NaoQuadrilatero

        # '*' em variáveis expande qualquer variável iterável no Python
        # (tuplas, dicionários, sequências, listas, etc.)
        # Exemplo: entrada = ('teste1', 'teste2', 'teste3') -> *entrada
        # Resultado: 'teste1' 'teste2' 'teste3'
        super().__init__(*lados)


class Retangulo(Quadrilatero):
    "Classe que representa um retângulo"

    def __init__(self, base, altura):
        # Retângulo é um quadrilátero com lados iguais dois a dois
        super().__init__(base, altura, base, altura)

    def area(self):
        """Retorna a área do retângulo

        Retorna um número (int ou float) com a área do retângulo
        """

        # Área = base * altura
        return self.lados[0] * self.lados[1]


class Quadrado(Retangulo):
    "Classe que representa um quadrado"

    def __init__(self, tamanho):
        # Quadrado é um retângulo com todos os lados iguais
        super().__init__(tamanho, tamanho)

