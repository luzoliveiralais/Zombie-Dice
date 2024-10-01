import pytest
from src.zombie_dice import pega_dado_verde
from src.zombie_dice import adc_pontos_placar_rodada

def test_pega_dado_verde():
    esperado = ("C", "P", "C", "T", "P", "C")  # Faces do dado verde
    resultado = pega_dado_verde()
    assert resultado == esperado, f"Esperado {esperado}, mas retornou {resultado}"


def test_adc_pontos_placar_rodada():
    pontos_rodada = {'cerebros': 0, 'tiros': 0, 'pegadas': 0}
    faces = ['C', 'T', 'P']  # Uma rodada onde o jogador comeu um cérebro, levou um tiro e teve pegadas
    resultado = adc_pontos_placar_rodada(pontos_rodada, faces)
    
    esperado = {'cerebros': 1, 'tiros': 1, 'pegadas': 1}
    assert resultado == esperado, f"Esperado {esperado}, mas retornou {resultado}"
