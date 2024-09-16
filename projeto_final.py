# Nome: Laís de Oliveira Luz (Análise e desenvolvimento de sistemas)

# Importações dos módulos necessários ao desenvolvimento do jogo:
from random import choice, randint
from time import sleep


def cabecalho():
    print('\033[1;30;42m o.o \033[m \033[1;35m             \033[m \033[1;30;42m x.x \033[m')
    print(' \033[1;30;42m  _ \033[m \033[1;35m ZOMBIE DICE!\033[m  \033[1;30;42m _ \033[m')
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


def pega_dados_do_copo(quantidade, copo):
    dados_sorteados = []
    for i in range(quantidade):
        sorteador = randint(0, len(copo) - 1)
        dado = copo[sorteador]
        dados_sorteados.append(dado)
        copo.remove(dado)
    return dados_sorteados, copo


def mostra_cores_copo(copo):
    printa_na_tela(f'Cores dos dados que ainda restam no copo:')
    for i in copo:
        if i == pega_dado_verde():
            print('\033[1;32mVERDE\033[m', end=' ')
        elif i == pega_dado_amarelo():
            print('\033[1;33mAMARELO\033[m', end=' ')
        elif i == pega_dado_vermelho():
            print('\033[1;31mVERMELHO\033[m', end=' ')


def checa_e_devolve_cerebros_ao_copo(copo, dados_a_pegar, cerebros):
    if len(copo) < dados_a_pegar or len(copo) == 0:
        print('Adicionando cérebros ao copo !')
        for cerebro in cerebros:
            copo.append(cerebro)
        cerebros = []
    return copo, cerebros


def lanca_dados(dados, lista_cerebros):
    faces_sorteadas = []
    for dado in dados:
        face = choice(dado)
        faces_sorteadas.append(face)
        if face == 'C':
            lista_cerebros.append(dado)
    return faces_sorteadas, lista_cerebros


def cores_dados(dados):
    printa_na_tela(f'Cores dos dados sorteados :')
    for dado in dados:
        if dado == pega_dado_verde():
            print('\033[1;32mVERDE\033[m', end=' ')
        elif dado == pega_dado_amarelo():
            print('\033[1;33mAMARELO\033[m', end=' ')
        elif dado == pega_dado_vermelho():
            print('\033[1;31mVERMELHO\033[m', end=' ')
    print()


def mostra_face(faces):
    printa_na_tela('As faces sorteadas foram:')
    for letra in faces:
        if letra == 'C':
            print(f'CÉREBRO - Você comeu um cérebro! ★.★ ')

        elif letra == 'P':
            print(f'PEGADAS - Sua vítima escapoou! (╥﹏╥)')

        elif letra == 'T':
            print(f'TIRO - Você levou um tiro! ︻┳═一')


def retorna_pegadas_na_mao(lista_dados, lista_faces):
    dados_na_mao = []
    contador = 0
    for dado in lista_dados:
        if lista_faces[contador] == 'P':
            dados_na_mao.append(dado)
        contador += 1
        if contador == 3:
            break
    return dados_na_mao


def mostra_pontuacao_rodada(pontos_rodada, placar_parcial=0):
    printa_na_tela('Pontos acumulados:')
    print(f"Você comeu {pontos_rodada['cerebros']} cérebro(s) até agora.")
    print(f"Você levou {pontos_rodada['tiros']} tiro(s) até agora.")
    print(f"Se parar agora, você fica com \033[1;91m{placar_parcial}\033[m cérebro(s) no placar final!")


def mostra_placar_final(pontos_finais, jogador):
    print(f"Você comeu {pontos_finais[jogador]['cerebros']} cérebros até agora {nomes_jogadores[jogador_atual]}!")


def adc_pontos_placar_rodada(pontos_rodada, faces):
    for face in faces:
        if face == 'C':
            pontos_rodada['cerebros'] += 1
        elif face == 'T':
            pontos_rodada['tiros'] += 1
        elif face == 'P':
            pontos_rodada['pegadas'] += 1
    return pontos_rodada


def adc_pontos_placar_final(pontos_rodada, pontos_finais, jogador):
    pontos_finais[jogador]['cerebros'] += pontos_rodada['cerebros']


def zera_placar_rodada(pontos_rodada):
    pontos_rodada['cerebros'] = 0
    pontos_rodada['tiros'] = 0
    pontos_rodada['pegadas'] = 0

def continua_sim_ou_nao():
    printa_na_tela('Você deseja continuar?')
    continua_turno = str(input('\033[1;35mSIM ou NÃO?(Responda "s" ou "n")\033[m').strip().lower())
    return continua_turno

def testa_fim_jogo(placar, condicao):
    for jogador in placar_final:
        for value in jogador.values():
            if value >= 13:
                if turnos[0] != turnos[len(turnos) - 1]:
                    continue
                elif turnos[0] == turnos[len(turnos) - 1]:
                    return True
            elif turnos[0] == turnos[len(turnos) - 1] and placar_final[0]['cerebros'] >= 13:
                return True
            elif turnos[0] == turnos[len(turnos) - 1] and placar_final[jogador_atual]['cerebros'] >= 13:
                return True


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

jogador_atual = 0

# INICIO DO JOGO

copo2 = []
condicao = True

printa_na_tela(f'Vamos começar...')
printa_na_tela('Lembre-se que sempre que faltarem dados no copo, os dados \n'
               'sorteados com face cérebro serão devolvidos a ele \n'
               'Mas não se preocupe, seus pontos não serão afetados!')

# PONTUACAO
placar_rodada = {'cerebros': 0, 'tiros': 0, 'pegadas': 0}
placar_final = []
for nome in nomes_jogadores:
    placar_final.append({'cerebros': 0})
placar_parcial = 0

# CONTADOR DE TURNOS
turnos = []
for nome in nomes_jogadores:
    turnos.append(0)

while condicao:
    cerebros_acumulados = []
    turnos[jogador_atual] += 1

    # SORTEANDO OS DADOS
    dados, copo1 = pega_dados_do_copo(3, copo_dados())

    # SORTEANDO A FACE DOS DADOS E RESERVANDO OS CÉREBROS
    faces_sorteadas, cerebros_acumulados = lanca_dados(dados, cerebros_acumulados)
    sleep(0.8)
    printa_na_tela(f'Turno do(a) {nomes_jogadores[jogador_atual]}!')
    sleep(0.8)
    printa_na_tela(f'SORTEANDO OS DADOS EM 3,2,1...')
    sleep(2)

    # MOSTRANDO INFORMAÇÕES NA TELA
    cores_dados(dados)
    mostra_face(faces_sorteadas)
    mostra_cores_copo(copo1)
    print()

    # ADICIONANDO PONTOS
    placar_parcial = adc_pontos_placar_rodada(placar_rodada, faces_sorteadas)
    placar_parcial = placar_rodada['cerebros'] + placar_final[jogador_atual]['cerebros']

    # MANTEM NA MÃO OS DADOS COM FACE PEGADAS
    dados_na_mao = retorna_pegadas_na_mao(dados, faces_sorteadas)

    # PRIMEIRAS CHECAGENS
    if placar_rodada["tiros"] >= 3:
        print('\033[1;31mVocê foi morto, seu turno acabou!\033[m \033[1;30;42m X  \033[m')
        print('                                  \033[1;30;42m X   P \033[m')
        print(f'Você levou {placar_rodada["tiros"]} e não vai pontuar!')
        zera_placar_rodada(placar_rodada)
        if testa_fim_jogo(placar_final, condicao):
            condicao = False
            break
        else:
            jogador_atual += 1
            if jogador_atual == len(nomes_jogadores):
                jogador_atual = 0


    else:
        mostra_pontuacao_rodada(placar_rodada, placar_parcial)
        if placar_parcial >= 13:
            printa_na_tela(f"Parabéns {nomes_jogadores[jogador_atual]}, você comeu "
                           f"{placar_parcial} cérebros pense se deseja continuar.")
            continua_turno = continua_sim_ou_nao()
        else:
            continua_turno = continua_sim_ou_nao()

        # SE O JOGADOR OPTAR POR CONTINUAR: SORTEIO DE DADOS COM PEGADAS E NOVOS DADOS.
        while continua_turno == 's':

            dados_a_rolar = []
            if len(dados_na_mao) == 1:
                copo1, cerebros_acumulados = checa_e_devolve_cerebros_ao_copo(copo1, 1, cerebros_acumulados)
                dados, copo1 = (pega_dados_do_copo(2, copo1))
                dados_na_mao.append(dados)
                dados_a_rolar = [dados_na_mao[0], dados_na_mao[1][0], dados_na_mao[1][1]]

            elif len(dados_na_mao) == 2:
                copo1, cerebros_acumulados = checa_e_devolve_cerebros_ao_copo(copo1, 2, cerebros_acumulados)
                dados, copo1 = (pega_dados_do_copo(1, copo1))
                dados_na_mao.append(dados)
                dados_a_rolar = [dados_na_mao[0], dados_na_mao[1], dados_na_mao[2][0]]

            elif len(dados_na_mao) == 3:
                dados_a_rolar = [dados_na_mao[0], dados_na_mao[1], dados_na_mao[2]]
                copo2 = copo1

            elif len(dados_na_mao) == 0:
                copo1, cerebros_acumulados = checa_e_devolve_cerebros_ao_copo(copo1, 3, cerebros_acumulados)
                dados_a_rolar, copo1 = pega_dados_do_copo(3, copo1)

            printa_na_tela(f'Continuando o turno do(a) {nomes_jogadores[jogador_atual]}!')
            printa_na_tela(f'Sorteando novos dados e dados com pegadas...')
            sleep(2)

            # SORTEIA FACES
            novas_faces, cerebros_acumulados = lanca_dados(dados_a_rolar, cerebros_acumulados)

            # MOSTRA AS FACES E CORES DOS DADOS SORTEADOS
            cores_dados(dados_a_rolar)
            mostra_face(novas_faces)
            mostra_cores_copo(copo1)
            print()

            # ADICIONANDO PONTUAÇÃO DOS DADOS SORTEADOS
            adc_pontos_placar_rodada(placar_rodada, novas_faces)
            dados_na_mao = retorna_pegadas_na_mao(dados_a_rolar, novas_faces)

            if placar_rodada['tiros'] >= 3:
                print()
                print('\033[1;31mVocê foi morto, seu turno acabou!\033[m \033[1;30;42m X  \033[m')
                print('                                  \033[1;30;42m X   P \033[m')
                print(f'Você levou {placar_rodada["tiros"]} e não vai pontuar!')
                zera_placar_rodada(placar_rodada)
                mostra_placar_final(placar_final, jogador_atual)
                if testa_fim_jogo(placar_final, condicao):
                    condicao = False
                    break
                else:
                    jogador_atual += 1
                    if jogador_atual == len(nomes_jogadores):
                        jogador_atual = 0
                    break

            elif placar_rodada['tiros'] < 3:
                placar_parcial = placar_rodada['cerebros'] + placar_final[jogador_atual]['cerebros']
                mostra_pontuacao_rodada(placar_rodada, placar_parcial)
                if placar_parcial >= 13:
                    printa_na_tela(f"Parabéns {nomes_jogadores[jogador_atual]}, você já comeu "
                                   f"{placar_parcial} cérebros pense se deseja continuar.")
                    continua_turno = continua_sim_ou_nao()
                else:
                    continua_turno = continua_sim_ou_nao()

        if continua_turno == 'n':
            adc_pontos_placar_final(placar_rodada, placar_final, jogador_atual)
            zera_placar_rodada(placar_rodada)
            mostra_placar_final(placar_final, jogador_atual)
            # Faz a verificação do turno  e placar para encerrar o jogo. De acordo com a regra de finalização
            # que fala sobre continuar o jogo até que o último jogador jogue sua vez.
            for jogador in placar_final:
                for value in jogador.values():
                    if value >= 13:
                        if turnos[0] != turnos[len(turnos) - 1]:
                            continue
                        elif turnos[0] == turnos[len(turnos) - 1]:
                            condicao = False
                    elif turnos[0] == turnos[len(turnos) - 1] and placar_final[0]['cerebros'] >= 13:
                        condicao = False
                    elif turnos[0] == turnos[len(turnos) - 1] and placar_final[jogador_atual]['cerebros'] >= 13:
                        condicao = False

            jogador_atual += 1
            if jogador_atual == len(nomes_jogadores):
                jogador_atual = 0

print()
print('\033[1;30;42m o.o \033[m  \033[1;35m            \033[m')
print('\033[1;30;42m _  \033[m   \033[1;35mFIM DE JOGO!\033[m')

contador = 0
for nome in nomes_jogadores:
    print(f'        {nome}:\033[1;35m{placar_final[contador]["cerebros"]}\033[m')
    contador += 1
