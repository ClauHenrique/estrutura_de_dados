class node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def inserir(self, elem):
        if self.head:
            # o ponteiro recebe o conteudo da cabeça
            ponteiro = self.head
            while ponteiro.next:
                ponteiro = ponteiro.next

            ponteiro.next = node(elem)

        else:
            # primeira inserção
            self.head = node(elem)

        self.size += 1

    def imprimir(self):
        ponteiro = self.head
        while ponteiro != None:
            print(ponteiro.dado, end=', ')
            ponteiro = ponteiro.next

    #retornar o tamanho da lista
    def __len__(self):
        return self.size

    # pegar elemento
    def get(self, index):
        # como ele vai fzr o for ate o valor de index, ele vai parar em determinado elemento
        # entao o ponteiro vai guardar esse elemento
        ponteiro = self.head
        for c in range(index):
            # como o ultimo elemento aponta para null. Ele nao entra no if se ponteiro for true
            # caso alguem passe um valor maior do que o da minha lista
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError('list index out of range')
        if ponteiro:
            return ponteiro.dado
        else:
            raise IndexError('list index out of range')

    def set(self, index, elem):
        ponteiro = self.head
        for c in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError('list index out of range')
        if ponteiro:
            ponteiro.dado = elem
        else:
            raise IndexError('list index out of range')

lista = linkedList()
lista.inserir(2)
lista.inserir(24)
lista.inserir(7)
lista.inserir(9)
a = len(lista)
print(a)
print(lista.get(1))

# trocar 24 - 5
lista.set(1, 5)
lista.imprimir()
