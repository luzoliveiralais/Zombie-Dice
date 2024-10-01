from unittest.mock import patch
from src.zombie_dice import pega_dado_verde, pega_dado_amarelo, pega_dado_vermelho, copo_dados, adc_pontos_placar_rodada, adc_pontos_placar_final, iniciar_jogo

@patch('builtins.input', side_effect=[2])  # Simulando que o usuário entrou "2" como número de jogadores
def test_iniciar_jogo(mock_input):
    jogadores = iniciar_jogo(2)  # Testa o início do jogo com 2 jogadores
    assert jogadores == 2


def test_pega_dado_verde():
    resultado = pega_dado_verde()
    esperado = ("C", "P", "C", "T", "P", "C")
    assert resultado == esperado


def test_pega_dado_amarelo():
    resultado = pega_dado_amarelo()
    esperado = ("T", "P", "C", "T", "P", "C")
    assert resultado == esperado


def test_pega_dado_vermelho():
    resultado = pega_dado_vermelho()
    esperado = ("T", "P", "T", "C", "P", "T")
    assert resultado == esperado


def test_pega_dados_do_copo():
    copo = copo_dados()
    dados_sorteados, copo_restante = pega_dados_do_copo(3, copo)
    assert len(dados_sorteados) == 3
    assert len(copo_restante) == 9


def test_adc_pontos_placar_rodada():
    placar_rodada = {'cerebros': 0, 'tiros': 0, 'pegadas': 0}
    faces = ['C', 'T', 'P']
    resultado = adc_pontos_placar_rodada(placar_rodada, faces)
    assert resultado['cerebros'] == 1
    assert resultado['tiros'] == 1
    assert resultado['pegadas'] == 1


def test_adc_pontos_placar_final():
    placar_rodada = {'cerebros': 2, 'tiros': 1, 'pegadas': 1}
    placar_final = [{'cerebros': 5}, {'cerebros': 8}]
    jogador_atual = 0
    adc_pontos_placar_final(placar_rodada, placar_final, jogador_atual)
    assert placar_final[0]['cerebros'] == 7  # 5 anteriores + 2 da rodada
