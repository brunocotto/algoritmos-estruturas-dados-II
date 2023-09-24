from DoublyLinkedList import DoublyLinkedList
from insertionSort import insertion_sort_dllist

# Exemplo de uso, adicionando elementos a lista
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