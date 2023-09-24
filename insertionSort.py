# Função de ordenação usando o algoritmo Insertion Sort na lista duplamente encadeada
def insertion_sort_dllist(dllist):
    # Verifica se a lista duplamente encadeada passada como argumento para a função está vazia ou contém apenas um elemento.
    if dllist.head is None or dllist.head.next is None:
        return
    # Inicializa a variável current, que será usada para percorrer os nós da lista duplamente encadeada durante a ordenação por inserção.
    current = dllist.head.next

    # Percorre os elementos da lista duplamente encadeada a ser ordenada.
    while current:
        key = current.data
        prev_node = current.prev

        # Move os elementos maiores que key para a direita
        while prev_node and prev_node.data > key:
            prev_node.next.data = prev_node.data
            prev_node = prev_node.prev

        # Insere key na posição correta
        if prev_node is None:
            dllist.head.data = key
        else:
            prev_node.next.data = key

        current = current.next