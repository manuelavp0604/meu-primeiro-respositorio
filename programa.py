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
cartela = {'regra_simples': { 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},'regra_avancada': {'sem_combinacao': -1,'quadra': -1,'full_house': -1,'sequencia_baixa': -1,'sequencia_alta': -1,'cinco_iguais': -1}}
def eh_numero_valido(texto):
    if texto == "":
        return False
    for letra in texto:
        if letra < "0" or letra > "9":
            return False
    return True


def criar_cartela_vazia():
    simples = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
    avancada = {"sem_combinacao": -1, "quadra": -1, "full_house": -1, "sequencia_baixa": -1, "sequencia_alta": -1, "cinco_iguais": -1}
    return {"regra_simples": simples, "regra_avancada": avancada}


def combinacao_existe_na_cartela(cartela, escolha):
    if eh_numero_valido(escolha):
        numero = int(escolha)
        if numero in cartela["regra_simples"]:
            return True
        return False
    if escolha in cartela["regra_avancada"]:
        return True
    return False


def combinacao_foi_usada(cartela, escolha):
    if eh_numero_valido(escolha):
        numero = int(escolha)
        if numero in cartela["regra_simples"]:
            return cartela["regra_simples"][numero] != -1
        return False
    if escolha in cartela["regra_avancada"]:
        return cartela["regra_avancada"][escolha] != -1
    return False


def mostrar_dados_da_rodada(dados_atuais, dados_guardados):
    print(f"Dados rolados: {dados_atuais}")
    print(f"Dados guardados: {dados_guardados}")


def calcular_total(cartela):
    total_simples = 0
    for valor in cartela["regra_simples"].values():
        if valor != -1:
            total_simples = total_simples + valor

    total_avancado = 0
    for valor in cartela["regra_avancada"].values():
        if valor != -1:
            total_avancado = total_avancado + valor

    bonus = 0
    if total_simples >= 63:
        bonus = 35

    return total_simples + total_avancado + bonus


def jogo():
    cartela = criar_cartela_vazia()
    imprime_cartela(cartela)

    for rodada in range(12):
        dados_atuais = rolar_dados(5)
        dados_guardados = []
        vezes_rerroladas = 0
        terminou_rodada = False
        mostrar_menu = True

        while terminou_rodada == False:
            if mostrar_menu:
                mostrar_dados_da_rodada(dados_atuais, dados_guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

            mostrar_menu = True
            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = input()

                if eh_numero_valido(indice):
                    indice = int(indice)
                    if indice >= 0 and indice < len(dados_atuais):
                        resultado = guardar_dado(dados_atuais, dados_guardados, indice)
                        dados_atuais = resultado[0]
                        dados_guardados = resultado[1]

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = input()

                if eh_numero_valido(indice):
                    indice = int(indice)
                    if indice >= 0 and indice < len(dados_guardados):
                        resultado = remover_dado(dados_atuais, dados_guardados, indice)
                        dados_atuais = resultado[0]
                        dados_guardados = resultado[1]

            elif opcao == "3":
                if vezes_rerroladas >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    quantidade = 5 - len(dados_guardados)
                    dados_atuais = rolar_dados(quantidade)
                    vezes_rerroladas = vezes_rerroladas + 1

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":
                todos_os_dados = dados_atuais + dados_guardados
                print("Digite a combinação desejada:")

                escolha_certa = False
                while escolha_certa == False:
                    escolha = input()

                    if combinacao_existe_na_cartela(cartela) == False:
                        print("Combinação inválida. Tente novamente.")
                    elif combinacao_foi_usada(cartela, escolha):
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(todos_os_dados, escolha, cartela)
                        escolha_certa = True
                        terminou_rodada = True

            else:
                print("Opção inválida. Tente novamente.")
                mostrar_menu = False

    imprime_cartela(cartela)
    pontos = calcular_total(cartela)
    print(f"Pontuação total: {pontos}")


jogo()