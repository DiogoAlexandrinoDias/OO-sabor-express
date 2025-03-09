from model.restaurante import Restaurante

# Criação de restaurantes e avaliações de exemplo
restaurante_japa = Restaurante('japa', 'japones')
restaurante_japa.receber_avaliacao('Gui', 4.5)
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Lais', 4)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    """Função principal que executa a listagem de restaurantes."""
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    # Ponto de entrada do programa
    main()