import pytest
from unittest.mock import patch
from src.zombie_dice import iniciar_jogo, obter_quantidade_jogadores

# Teste para verificar o início do jogo e registro dos jogadores
@patch('builtins.input', side_effect=['2', 'Jogador1', 'Jogador2'])
def test_iniciar_jogo(mock_input):
    # Simula a entrada de 2 jogadores
    quantidade_jogadores = obter_quantidade_jogadores()
    assert quantidade_jogadores == 2

    # Simula o início do jogo com 2 jogadores
    nomes_jogadores = iniciar_jogo(quantidade_jogadores)
    assert len(nomes_jogadores) == 2
    assert nomes_jogadores == ['Jogador1', 'Jogador2']
