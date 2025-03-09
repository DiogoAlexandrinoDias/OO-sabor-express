from model.avaliacao import Avaliacao

class Restaurante:
    """Classe que representa um restaurante e suas operações.

    Attributes:
        nome (str): Nome do restaurante.
        categoria (str): Categoria do restaurante (ex: gourmet, japonesa).
        ativo (bool): Status de atividade do restaurante.
        avaliacoes (list[Avaliacao]): Lista de avaliações dos clientes.
    """

    restaurantes = []  # Lista estática para armazenar todos os restaurantes

    def __init__(self, nome, categoria):
        """Inicializa um restaurante com nome, categoria e status inativo.

        Args:
            nome (str): Nome do restaurante.
            categoria (str): Categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna representação em string do restaurante (nome e categoria)."""
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma tabela formatada com todos os restaurantes cadastrados."""
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """str: Retorna símbolo ✓ se ativo ou ☐ se inativo."""
        return '✓' if self._ativo else '☐'

    def alternar_estado(self):
        """Alterna o status de atividade do restaurante (ativo/inativo)."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Registra uma nova avaliação para o restaurante.

        Args:
            cliente (str): Nome do cliente.
            nota (float): Nota da avaliação (0 a 5).
        """
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """float: Calcula e retorna a média das avaliações (arredondada para 1 decimal)."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media