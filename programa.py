##--------------------------------AVISO------------------------------
## Vou copiar e colar todas as funções nesse programa porque não esta rodando sem
##-------------------------------------------------------------------
import random
def rolar_dados(quantidade):
    lista=[]
    for i in range(quantidade):
        x=0
        x=random.randint(1,6)
        lista.append(x)
    return lista


def guardar_dado(dados_rolados, dados_no_estoque, indice):
    lista_nova = []

    i = 0
    while i<len(dados_rolados):
        if i != indice:
            lista_nova.append(dados_rolados[i])
        i = i+1
    dados_no_estoque.append(dados_rolados[indice])

    return [lista_nova, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, indice):
    dado_removido = dados_no_estoque[indice]

    novo_estoque = []
    i = 0
    while i < len(dados_no_estoque):
        if i != indice:
            novo_estoque.append(dados_no_estoque[i])
        i += 1

    novos_rolados = dados_rolados + [dado_removido]

    return [novos_rolados, novo_estoque]     

def calcula_pontos_regra_simples(lista_dados):
    pontos = {}

    for face in range(1,7):
        soma = 0
        i = 0
        while i < len(lista_dados):
            if lista_dados[i] == face:
                soma += face
            i+=1
        pontos[face] = soma
    return pontos

def calcula_pontos_soma(lista):
    soma = 0 
    for i in lista:
        soma += i
    return soma 


def calcula_pontos_sequencia_baixa(lista_inteiros): 
    contador = 0

    for num in range (1,7): 
        if num in lista_inteiros:
            contador += 1
            if contador == 4:
                return 15
        else:
            contador = 0
    return 0
        

def calcula_pontos_sequencia_alta(lista_num_inteiros):
    contador = 0
    for num in range (1,7):
        if num in lista_num_inteiros:
            contador += 1
            if contador == 5:
                return 30
        else:
            contador = 0
    return 0


def calcula_pontos_full_house(lista5):
    contador1 = 0 
    contador2 = 0
    soma = 0

    numero1 = lista5[0]
    numero2 = 0
     
    for num in lista5:
        if num != numero1:
            numero2 = num
             
    for num in lista5:
        soma += num
        if num == numero1: 
            contador1 += 1
        elif num == numero2:
            contador2 += 1
            
    if (contador1 == 3 and contador2 == 2) or (contador1 == 2 and contador2 == 3):
        return soma 

    return 0 

def calcula_pontos_quadra(lista):
    for i in range(len(lista)):
        quantidade=1
        for j in range(i+1,len(lista)):
            if lista[i]==lista[j]:
                quantidade+=1
        if quantidade==4:
            return calcula_pontos_soma(lista)
    return 0

def calcula_pontos_quina(lista):
    for i in range(len(lista)):
        qnt = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                qnt += 1

        if qnt >= 5:
            return 50

    return 0

def calcula_pontos_regra_avancada(lista):
    resultados = {}

    resultados['cinco_iguais'] = calcula_pontos_quina(lista)
    resultados['full_house'] = calcula_pontos_full_house(lista)
    resultados['quadra'] = calcula_pontos_quadra(lista)
    resultados['sem_combinacao'] = calcula_pontos_soma(lista)
    resultados['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    resultados['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)

    return resultados

def faz_jogada(dados, categoria, cartela):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancada = calcula_pontos_regra_avancada(dados)

    if categoria in ['1', '2', '3', '4', '5', '6']:
        cartela['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    else:
        cartela['regra_avancada'][categoria] = pontos_avancada[categoria]

    return cartela

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
##a partir daqui é o nosso codigo

from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1,
    }
}      
combinacoes=['1','2','3','4','5','6','cinco_iguais','full_house','quadra','sem_combinacao','sequencia_alta','sequencia_baixa']

imprime_cartela(cartela)

for rodada in range(12):
    dados=rolar_dados(5)
    guardados=[]
    rerrolagem=0
    terminou=False

    print("Dados rolados:",dados)
    print("Dados guardados:",guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação.")

    while not terminou:
        opcao=input()

        if opcao=='1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            i=int(input())
            dados, guardados=guardar_dado(dados,guardados,i)
        elif opcao =='2':
            print ("Digite o índice do dado a ser removido (0 a 4):")
            i=int(input())
            dados, guardados=remover_dado(dados,guardados,i)

        elif opcao =="3":
            if rerrolagem>=2:
                print ("Você já usou todas as suas rerrolagens.")
            else:
                dados=rolar_dados(len(dados))
                rerrolagem+=1

        elif opcao =="4":
            imprime_cartela(cartela)

        elif opcao=='0':
            print("Digite a combinação desejada.")
            while True:
                comb = input()

                if comb not in combinacoes:
                    print("Combinação inválida. Tente novamente.")
                    continue

                if comb in cartela['regra_avancada']:
                    usada = cartela['regra_avancada'][comb] != -1
                else:
                    usada = cartela['regra_simples'][int(comb)] != -1

                if usada:
                    print("Essa combinação já foi utilizada.")
                    continue

                total = dados + guardados
                faz_jogada(total, comb, cartela)
                break

            terminou = True

        else:
            print("Opção inválida. Tente novamente.")

        if not terminou:
            print("Dados rolados:", dados)
            print("Dados guardados:", guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")


# pontuação final
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
            