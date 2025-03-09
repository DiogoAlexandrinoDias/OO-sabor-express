class Avaliacao:
    """Classe que representa uma avaliação de um cliente a um restaurante.

    Attributes:
        cliente (str): Nome do cliente que fez a avaliação.
        nota (float): Nota atribuída pelo cliente (entre 0 e 5).
    """

    def __init__(self, cliente, nota):
        """Inicializa uma avaliação com cliente e nota.

        Args:
            cliente (str): Nome do cliente.
            nota (float): Nota da avaliação (0 a 5).

        Raises:
            ValueError: Se a nota estiver fora do intervalo permitido.
        """
        if not (0 <= nota <= 5):
            raise ValueError("Nota deve ser entre 0 e 5")
        self._cliente = cliente
        self._nota = nota

    # ----------- Propriedades para encapsulamento -----------
    @property
    def cliente(self):
        """str: Nome do cliente (somente leitura)."""
        return self._cliente

    @property
    def nota(self):
        """float: Nota da avaliação (somente leitura)."""
        return self._nota