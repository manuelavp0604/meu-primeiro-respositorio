from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada
from funcoes import faz_jogada
from funcoes import imprime_cartela

cartela = {'regra_simples': { 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},'regra_avancada': {'sem_combinacao': -1,'quadra': -1,'full_house': -1,'sequencia_baixa': -1,'sequencia_alta': -1,'cinco_iguais': -1}}

imprime_cartela(cartela)

rodada = 0

while rodada < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    marcou = False

    while not marcou:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")

            combinacao_valida = False

            while not combinacao_valida:
                categoria = input()

                if categoria in ["1", "2", "3", "4", "5", "6"]:
                    categoria_int = int(categoria)

                    if cartela["regra_simples"][categoria_int] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(dados, categoria, cartela)
                        combinacao_valida = True
                        marcou = True

                elif categoria in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(dados, categoria, cartela)
                        combinacao_valida = True
                        marcou = True

                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodada += 1

pontuacao = 0

soma_simples = 0
for valor in cartela["regra_simples"].values():
    soma_simples += valor
    pontuacao += valor

for valor in cartela["regra_avancada"].values():
    pontuacao += valor

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")