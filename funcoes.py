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
    quantidade = 0

    for i in range(len(lista) - 1):
        if lista[i] == lista[i+1]:
            quantidade += 1
        else:
            quantidade = 0

    if quantidade >= 4:
        return 50

    return 0
