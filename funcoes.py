import random
def rolar_dados(quantidade):
    lista=[]
    for i in range(quantidade):
        x=0
        x=random.randint(1,6)
        lista.append(x)
    return lista
