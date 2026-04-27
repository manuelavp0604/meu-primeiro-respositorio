def rolar_dados(quantidade):
    lista=[]
    for i in range(quantidade):
        x=0
        x=random.randint(1,6)
        lista.append(x)
    return lista


def guardar_dados(dados_rolados, dados_no_estoque, indice):
    lista_nova = []

    i = 0
    while i<len(dados_rolados):
        if i != indice:
            lista_nova.append(dados_rolados[i])
        i = i+1
    dados_no_estoque.append(dados_rolados[indice])

    return [lista_nova, dados_no_estoque]

        
