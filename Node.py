# Definição da classe Node para representar os nós da lista
class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó
        self.prev = None  # Referência para o nó anterior