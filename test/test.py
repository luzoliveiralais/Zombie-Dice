from unittest.mock import patch
from src.zombie_dice import iniciar_jogo, obter_quantidade_jogadores

@patch('builtins.input', side_effect=[2, 'Jogador1', 'Jogador2'])
def test_iniciar_jogo(mock_input):
    # Testa a função iniciar_jogo com dois jogadores simulados
    nomes = iniciar_jogo(2)
    assert len(nomes) == 2
    assert nomes == ['Jogador1', 'Jogador2']

@patch('builtins.input', side_effect=[2])
def test_obter_quantidade_jogadores(mock_input):
    # Testa a função obter_quantidade_jogadores simulando a entrada de "2"
    jogadores = obter_quantidade_jogadores()
    assert jogadores == 2
