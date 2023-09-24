# Definição da classe Node para representar os nós da lista
class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó
        self.prev = None  # Referência para o nó anterior

# Definição da classe DoublyLinkedList para representar a lista duplamente encadeada
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Referência para o primeiro nó da lista
        self.tail = None  # Referência para o último nó da lista

    # Método para adicionar um elemento ao final da lista
    def append(self, data):
        new_node = Node(data)
        # Verifica se a lista está vazia.
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Método para exibir a lista
    def display(self):
        current = self.head
        # Percorre a lista duplamente encadeada e imprime os dados de cada nó da lista.
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

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

# Exemplo de uso:
dllist = DoublyLinkedList()
dllist.append(5)
dllist.append(2)
dllist.append(9)
dllist.append(1)
dllist.append(6)

print("Lista original")
dllist.display()

insertion_sort_dllist(dllist)

print("Lista após o Insertion Sort")
dllist.display()
