class NaoPoligono(Exception):
    pass


class Poligono(object):
    "Classe que representa um polígono genérico"  # Isso é uma docstring
    # Uma docstring é definida por uma string ("string" ou """string""") no
    # inicio de um método/classe/função/módulo e facilitam a documentação do
    # código. Ferramentas automatizadas podem converter o texto dentro de uma
    # docstring em documentação da API automaticamente, além de IDEs podem
    # extrair essa informação para facilitar a vida do programador.

    """Isso não é uma docstring, é um comentário (pois não aparece no inicio
    da definição da classe).

    Você pode usar três aspas simples ou duplas para fazer comentários de
    várias linhas, apesar que geralmente é mais recomendado usar # mesmo.
    """

    def __init__(self, *lados):
        # Polígono necessita de no mínimo dois lados
        if len(lados) <= 2:
            raise NaoPoligono

        for i in lados:
            # Se qualquer lado for 0 ou negativo é inválido
            if i <= 0:
                raise ArithmeticError

        self.lados = lados

    def num_lados(self):
        """Retorna o número de lados

        Retorno: um valor inteiro com o número de lados do polígono
        """

        return len(self.lados)
