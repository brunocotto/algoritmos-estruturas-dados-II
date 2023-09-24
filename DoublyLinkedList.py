from Node import Node

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