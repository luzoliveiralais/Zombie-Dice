from random import choice, randint
from time import sleep


def cabecalho():
    """Função para exibir o cabeçalho do jogo."""
    print('\033[1;30;42m o.o \033[m \033[1;35m             \033[m \033[1;30;42m x.x \033[m')
    print(' \033[1;30;42m  _ \033[m \033[1;35m ZOMBIE DICE!\033[m  \033[1;30;42m _ \033[m')
    print()


def printa_na_tela(frase):
    """Função para exibir mensagens coloridas."""
    print()
    print(f'\033[1;35m{frase}\033[m')


def pega_dado_verde():
    return "C", "P", "C", "T", "P", "C"


def pega_dado_amarelo():
    return "T", "P", "C", "T", "P", "C"


def pega_dado_vermelho():
    return "T", "P", "T", "C", "P", "T"


def copo_dados():
    copo = [pega_dado_verde(), pega_dado_verde(), pega_dado_verde(),
            pega_dado_verde(), pega_dado_verde(), pega_dado_amarelo(),
            pega_dado_amarelo(), pega_dado_amarelo(), pega_dado_amarelo(),
            pega_dado_vermelho(), pega_dado_vermelho(), pega_dado_vermelho()]
    return copo


def pega_dados_do_copo(quantidade, copo):
    dados_sorteados = []
    for i in range(quantidade):
        sorteador = randint(0, len(copo) - 1)
        dado = copo[sorteador]
        dados_sorteados.append(dado)
        copo.remove(dado)
    return dados_sorteados, copo


def lanca_dados(dados, lista_cerebros):
    faces_sorteadas = []
    for dado in dados:
        face = choice(dado)
        faces_sorteadas.append(face)
        if face == 'C':
            lista_cerebros.append(dado)
    return faces_sorteadas, lista_cerebros


def mostra_face(faces):
    """Função para exibir as faces dos dados sorteados."""
    printa_na_tela('As faces sorteadas foram:')
    for letra in faces:
        if letra == 'C':
            print(f'CÉREBRO - Você comeu um cérebro! ★.★ ')
        elif letra == 'P':
            print(f'PEGADAS - Sua vítima escapou! (╥﹏╥)')
        elif letra == 'T':
            print(f'TIRO - Você levou um tiro! ︻┳═一')


def adc_pontos_placar_rodada(pontos_rodada, faces):
    """Atualiza o placar da rodada com base nas faces sorteadas."""
    for face in faces:
        if face == 'C':
            pontos_rodada['cerebros'] += 1
        elif face == 'T':
            pontos_rodada['tiros'] += 1
        elif face == 'P':
            pontos_rodada['pegadas'] += 1
    return pontos_rodada


def adc_pontos_placar_final(pontos_rodada, pontos_finais, jogador):
    """Adiciona os pontos acumulados ao placar final do jogador."""
    pontos_finais[jogador]['cerebros'] += pontos_rodada['cerebros']


def zera_placar_rodada(pontos_rodada):
    """Zera os pontos da rodada se o jogador for morto."""
    pontos_rodada['cerebros'] = 0
    pontos_rodada['tiros'] = 0
    pontos_rodada['pegadas'] = 0


def continua_sim_ou_nao():
    """Função que pergunta ao jogador se ele quer continuar jogando no turno."""
    resposta = input('Você deseja continuar jogando? (s/n): ').strip().lower()
    return resposta == 's'


def iniciar_jogo(jogadores):
    """Função que contém a lógica do jogo com base no número de jogadores."""
    cabecalho()

    nomes_jogadores = []
    for i in range(1, jogadores + 1):
        nome = input(f'Digite o nome do jogador {i}: ')
        nomes_jogadores.append(nome)

    print(f'Jogadores registrados: {", ".join(nomes_jogadores)}')

    # Inicia o placar para cada jogador
    placar_final = [{'cerebros': 0} for _ in range(jogadores)]

    # Executa as rodadas até que um jogador atinja 13 cérebros
    jogador_atual = 0
    jogo_ativo = True

    while jogo_ativo:
        print(f"\nTurno do(a) {nomes_jogadores[jogador_atual]}")
        placar_rodada = {'cerebros': 0, 'tiros': 0, 'pegadas': 0}
        turnos_jogador(jogador_atual, placar_rodada, placar_final)

        # Checa se algum jogador atingiu 13 cérebros para encerrar o jogo
        if placar_final[jogador_atual]['cerebros'] >= 13:
            jogo_ativo = False
            print(f"\nParabéns {nomes_jogadores[jogador_atual]}, você ganhou com {placar_final[jogador_atual]['cerebros']} cérebros!")
        else:
            # Passa o turno para o próximo jogador
            jogador_atual = (jogador_atual + 1) % jogadores

    return placar_final


def turnos_jogador(jogador_atual, placar_rodada, placar_final):
    """Função que gerencia os turnos e a pontuação de cada jogador."""
    cerebros_acumulados = []
    copo = copo_dados()

    continuar_turno = True
    while continuar_turno:
        # Sorteia 3 dados
        dados_sorteados, copo = pega_dados_do_copo(3, copo)
        faces_sorteadas, cerebros_acumulados = lanca_dados(dados_sorteados, cerebros_acumulados)
        
        # Mostra as faces dos dados sorteados
        mostra_face(faces_sorteadas)

        # Atualiza o placar da rodada
        adc_pontos_placar_rodada(placar_rodada, faces_sorteadas)

        # Checa se o jogador foi morto (3 tiros)
        if placar_rodada['tiros'] >= 3:
            print(f"\nVocê foi morto! Turno encerrado sem pontuação.")
            zera_placar_rodada(placar_rodada)
            return

        # Mostra pontuação acumulada da rodada
        print(f"\nVocê comeu {placar_rodada['cerebros']} cérebro(s) e levou {placar_rodada['tiros']} tiro(s).")
        
        # Pergunta se o jogador quer continuar ou encerrar o turno
        continuar_turno = continua_sim_ou_nao()
    
    # Atualiza o placar final do jogador após o turno
    adc_pontos_placar_final(placar_rodada, placar_final, jogador_atual)


def obter_quantidade_jogadores():
    """Função para obter a quantidade de jogadores via input."""
    jogadores = int(input('Informe a quantidade de jogadores: '))
    while jogadores < 2:
        print('Você precisa de pelo menos 2 jogadores para iniciar o jogo.')
        jogadores = int(input('Informe a quantidade de jogadores: '))
    return jogadores


def main():
    jogadores = obter_quantidade_jogadores()
    iniciar_jogo(jogadores)


if __name__ == "__main__":
    main()
