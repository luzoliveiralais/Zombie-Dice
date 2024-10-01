import pytest
from unittest.mock import patch
from src.zombie_dice import iniciar_jogo, obter_quantidade_jogadores, turnos_jogador


@patch('builtins.input', side_effect=['Jogador1', 'Jogador2'])
def test_iniciar_jogo(mock_input):
    jogadores = 2
    placar_final = iniciar_jogo(jogadores)
    assert len(placar_final) == 2  # Verifica se o placar final foi criado corretamente
    assert placar_final[0]['cerebros'] == 0  # Verifica o placar inicial


@patch('builtins.input', side_effect=['1', '2'])  # Simulando entrada inválida e válida
def test_obter_quantidade_jogadores(mock_input):
    quantidade_jogadores = obter_quantidade
