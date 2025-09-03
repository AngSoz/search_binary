def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    contador = 0

    while inicio <= fim:
        contador += 1 
        meio_lista  = (inicio + fim) // 2
        if lista[meio_lista] == alvo:
            print(f"Encontrei o meu algo {alvo}")
            print(f'--> Contador : {contador}')
            break
        elif lista[meio_lista] < alvo:
            inicio = meio_lista + 1
        else:
            fim = meio_lista - 1
            
def busca_normal(lista, alvo):
    contator = 0
    
    for elemento in lista:
        contator += 1
        if lista[elemento] == alvo: 
            print(f"[NORMAL] Encontrei o meu algo {alvo}")
            print(f'[NORMAL] --> Contador : {contator}')
            break
    
lista = list(range(1, 100001))

busca_normal(lista, 80532)
busca_binaria(lista, 80532)

print("FIM")