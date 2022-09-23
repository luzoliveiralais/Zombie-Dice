# Nome: Laís de Oliveira Luz (Análise e desenvolvimento de sistemas)

# Importações dos módulos necessários ao desenvolvimento do jogo:
from random import choice, randint
from time import sleep


def cabecalho():
    # Cabeçalho/Apresentação do nome do jogo
    print('\033[1;35m*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\033[m')
    print('\033[1;32m        ZOMBIE DICE!\033[m')
    print('\033[1;35m*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\033[m')
    print()

def printa_na_tela(frase):
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

def pega_dados_do_copo(quantidade):
    dados_sorteados = []
    for i in range(quantidade):
        sorteador = randint(0, len(copo_dados()) - 1)
        dado = copo_dados()[sorteador]
        dados_sorteados.append(dado)
    return dados_sorteados

def tira_dados_do_copo(copo):
    if len(copo) > 0:
        print('O copo está vazio!')

def lanca_dados(dados):
    faces_sorteadas = []
    for i in dados:
        face = choice(i)
        faces_sorteadas.append(face)
    return faces_sorteadas

def cores_dados(dados):
    cores = []
    for dado in dados:
        if dado == pega_dado_verde():
            cores.append('Verde')
        elif dado == pega_dado_amarelo():
            cores.append('Amarelo')
        elif dado == pega_dado_vermelho():
            cores.append('Vermelho')
    return cores

def mostra_cores(lista_cores):
    printa_na_tela('As cores dos dados sorteados foram:')
    print(f'{lista_cores[0]}, {lista_cores[1]}, {lista_cores[2]}')

def mostra_face(faces):
    for letra in faces:
        if letra == 'C':
            print(f'CÉREBRO (Você comeu um cérebro!)')

        elif letra == 'P':
            print(f'PEGADAS (Sua vítima escapou!)')

        elif letra == 'T':
            print(f'TIRO (Você levou um tiro!)')

def mostra_pontuacao_rodada(pontos_rodada):
    print(f"Você levou {pontos_rodada['tiros']} tiro(s) até agora.")
    print(f"Você comeu {pontos_rodada['cerebros']} cérebro(s) até agora.")

def mostra_placar_final(pontos_finais,jogador):
    print(f"Você comeu {pontos_finais[jogador]['cerebros']} cérebros.")

def adc_pontos_placar_rodada(pontos_rodada, faces):
    for face in faces:
        if face == 'C':
            pontos_rodada['cerebros'] += 1
        elif face == 'T':
            pontos_rodada['tiros'] += 1
        elif face == 'P':
            pontos_rodada['pegadas'] += 1

def adc_pontos_placar_final(pontos_rodada, pontos_finais, jogador):
    pontos_finais[jogador]['cerebros'] += pontos_rodada['cerebros']

def zera_placar_rodada(pontos_rodada):
    pontos_rodada['cerebros'] = 0
    pontos_rodada['tiros'] = 0
    pontos_rodada['pegadas'] = 0


cabecalho()

# REGISTRO DA QUANTIDADE E CRIAÇÃO DA LISTA DE JOGADORES:
jogadores = int(input('Informe a quantidade de jogadores:'))
if jogadores < 2:
    while jogadores < 2:
        print('Para jogar \033[1;32mZOMBIE DICE\033[m você precisa de pelo menos 2 jogadores.')
        print('Tente novamente!')
        jogadores = int(input('Informe a quantidade de jogadores:'))
        if jogadores >= 2:
            print()
            print('\033[1;35mE quem são os jogadores?\033[m')
            print()
else:
    print()
    print('\033[1;35mE quem são os jogadores?\033[m')
    print()

nomes_jogadores = []  # lista que armazena o nome dos jogadores
nomes_parametro = 1
while nomes_parametro <= jogadores:
    nomes_jogadores.append(str(input(f'Digite aqui o nome do jogador {nomes_parametro}:')))
    nomes_parametro += 1

# JOGADOR ATUAL:
jogador_atual = 0

# INICIO DO JOGO
printa_na_tela('Vamos começar...')

# PONTUACAO
placar_rodada = {'cerebros':0, 'tiros':0, 'pegadas':0}
placar_final = []
for nome in nomes_jogadores:
    placar_final.append({'cerebros':0})

# INICIO DA LÓGICA DO JOGO
while placar_final[jogador_atual]["cerebros"] < 13:

    # SORTEANDO OS DADOS
    dados = pega_dados_do_copo(3)

    # SORTEANDO A FACE DOS DADOS
    faces_sorteadas = lanca_dados(dados)

    # MOSTRANDO AS CORES SORTEADAS

    printa_na_tela(f'Turno do(a) {nomes_jogadores[jogador_atual]}')
    printa_na_tela(f'Sorteando os dados em 3,2,1...')
    sleep(2)

    cores = cores_dados(dados)
    mostra_cores(cores)

    # MOSTRANDO AS FACES
    printa_na_tela("As faces sorteadas foram:")
    mostra_face(faces_sorteadas)
    print()

    # ADICIONANDO PONTOS
    adc_pontos_placar_rodada(placar_rodada, faces_sorteadas)
    mostra_pontuacao_rodada(placar_rodada)

    # PRIMEIRAS CHECAGENS
    if placar_rodada["tiros"] >= 3:
        printa_na_tela('Você foi morto, seu turno acabou!x.x')
        mostra_placar_final(placar_final, jogador_atual)
        zera_placar_rodada(placar_rodada)
        copo_dados()
        jogador_atual += 1
        if jogador_atual == len(nomes_jogadores):
            jogador_atual = 0

    elif placar_final[jogador_atual]['cerebros'] >= 13:
        printa_na_tela(f"Parabéns {nomes_jogadores[jogador_atual]}, você comeu "
                       f"{placar_final[jogador_atual]['cerebros']} e ganhou o jogo!")

    else:
        printa_na_tela('Você deseja continuar?')
        continua_turno = str(input('\033[1;35mSIM ou NÃO?\033[m').strip().lower())

        # SE O JOGADOR OPTAR EM CONTINUAR: SORTEIO DE DADOS COM PEGADAS E NOVOS DADOS.
        while continua_turno == 'sim':
            dados_na_mao = []
            for face in faces_sorteadas:
                if face == 'P':
                    index_de_p = faces_sorteadas.index('P')
                    dados_na_mao.append(dados[index_de_p])

            dados_a_rolar = []
            if len(dados_na_mao) == 1:
                dados_na_mao.append(pega_dados_do_copo(2))
                dados_a_rolar = [dados_na_mao[0], dados_na_mao[1][0], dados_na_mao[1][1]]
            elif len(dados_na_mao) == 2:
                dados_na_mao.append(pega_dados_do_copo(1))
                dados_a_rolar = [dados_na_mao[0], dados_na_mao[1], dados_na_mao[2][0]]
            elif len(dados_na_mao) == 3:
                dados_a_rolar = [dados_na_mao[0], dados_na_mao[1], dados_na_mao[2]]
            elif len(dados_na_mao) == 0:
                dados_a_rolar = pega_dados_do_copo(3)
            printa_na_tela(f'Continuando o turno do(a) {nomes_jogadores[jogador_atual]}')
            printa_na_tela(f'Sorteando novos dados e dados com pegadas em 3,2,1...')
            sleep(2)
            novas_faces = lanca_dados(dados_a_rolar)


            # MOSTRA AS FACES E CORES DOS DADOS SORTEADOS
            mostra_face(novas_faces)
            novas_cores = cores_dados(dados_a_rolar)
            mostra_cores(novas_cores)

            # ADICIONANDO PONTUAÇÃO DOS DADOS SORTEADOS
            # Como o jogador deicidiu continuar jogando,
            # ao placar da rodada serão somados os novos pontos.
            adc_pontos_placar_rodada(placar_rodada, novas_faces)
            mostra_pontuacao_rodada(placar_rodada)

            if placar_rodada['tiros'] >= 3:
                printa_na_tela('Você foi morto, seu turno acabou!x.x')
                zera_placar_rodada(placar_rodada)
                mostra_placar_final(placar_final, jogador_atual)
                jogador_atual += 1
                if jogador_atual == len(nomes_jogadores):
                    jogador_atual = 0
                break

            else:
                printa_na_tela('Você deseja continuar?')
                continua_turno = str(input('\033[1;35mSIM ou NÃO?\033[m').strip().lower())

        if continua_turno == 'não':
            adc_pontos_placar_final(placar_rodada, placar_final, jogador_atual)
            zera_placar_rodada(placar_rodada)
            mostra_placar_final(placar_final, jogador_atual)
            if placar_final[jogador_atual]['cerebros'] >= 13:
                printa_na_tela(f"Parabéns {nomes_jogadores[jogador_atual]}, você comeu "
                               f"{placar_final[jogador_atual]['cerebros']} e ganhou o jogo!")
                break
            jogador_atual += 1
            if jogador_atual == len(nomes_jogadores):
                jogador_atual = 0