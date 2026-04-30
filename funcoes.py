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
    contador = 1

    for i in range (len(lista_inteiro)):
        for j in range(len(lista_inteiro)):
            if lista[i]+1 == lista [j]:
                contador += 1
        if contador >= 4:
            return 15
        return 0
