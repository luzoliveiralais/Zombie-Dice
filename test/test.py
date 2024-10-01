import pytest
from unittest.mock import patch
from src.zombie_dice import iniciar_jogo, obter_quantidade_jogadores

# Simula as entradas para dois jogadores, e para cada jogador, a resposta "n" para não continuar o turno
@patch('builtins.input', side_effect=['Jogador1', 'Jogador2', 'n', 'n'])
def test_iniciar_jogo(mock_input):
    jogadores = 2
    placar_final = iniciar_jogo(jogadores)
    assert len(placar_final) == 2  # Verifica se o placar final foi criado corretamente
    assert placar_final[0]['cerebros'] == 0  # Verifica o placar inicial


# Corrigindo o nome da função para obter_quantidade_jogadores
@patch('builtins.input', side_effect=['1', '2'])  # Simulando entrada inválida e válida
def test_obter_quantidade_jogadores(mock_input):
    quantidade_jogadores = obter_quantidade_jogadores()
    assert quantidade_jogadores == 2  # Verifica se a função retornou 2 após a entrada correta
