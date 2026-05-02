from funcoes import *

cartela = {'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}, 'regra_avancada': {'sem_combinacao': -1, 'quadra': -1, 'full_house': -1, 'sequencia_baixa': -1, 'sequencia_alta': -1, 'cinco_iguais': -1}}   
combinacoes=['1','2','3','4','5','6','cinco_iguais','full_house','quadra','sem_combinacao','sequencia_alta','sequencia_baixa']

imprime_cartela(cartela)

for rodada in range(12):
    dados=rolar_dados(5)
    guardados=[]
    rerrolagem=0
    terminou=False

    print("Dados rolados:",dados)
    print("Dados guardados:",guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    while not terminou:
        opcao=input()

         if opcao == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            i = int(input())
            if 0 <= i < len(dados):
                dados, guardados = guardar_dado(dados, guardados, i)
            else:
                print("Índice inválido.")
 
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            if 0 <= i < len(guardados):
                dados, guardados = remover_dado(dados, guardados, i)
            else:
                print("Índice inválido.")
 
        elif opcao == '3':
            if rerrolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados = rolar_dados(len(dados))
                rerrolagem += 1
 
        elif opcao == '4':
            imprime_cartela(cartela)
 
        elif opcao == '0':
            print("Digite a combinação desejada:")
            while True:
                comb = input()
 
                if comb not in combinacoes:
                    print("Combinação inválida. Tente novamente.")
                    print("Digite a combinação desejada:")
                    continue
 
                if comb in cartela['regra_avancada']:
                    usada = cartela['regra_avancada'][comb] != -1
                else:
                    usada = cartela['regra_simples'][int(comb)] != -1
 
                if usada:
                    print("Essa combinação já foi utilizada.")
                    print("Digite a combinação desejada:")
                    continue
 
                total = dados + guardados
                faz_jogada(total, comb, cartela)
                imprime_cartela(cartela)
                break
 
            terminou = True
 
        else:
            print("Opção inválida. Tente novamente.")
 
        if not terminou:
            print("Dados rolados:", dados)
            print("Dados guardados:", guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
 
imprime_cartela(cartela)
 
soma_simples = 0
for v in cartela['regra_simples'].values():
    if v != -1:
        soma_simples += v
 
soma_avancada = 0
for v in cartela['regra_avancada'].values():
    if v != -1:
        soma_avancada += v
 
bonus = 0
if soma_simples >= 63:
    bonus = 35
 
total = soma_simples + soma_avancada + bonus
 
print("Pontuação total:", total)