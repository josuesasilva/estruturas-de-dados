#!/usr/bin/env python
# *-* coding: utf-8 *-*

class Celula(object):

    def __init__(self, item=None, prox=None):
        self.item = item
        self.prox = prox


class ListaSimples(object):

    def __init__(self):
        self.primeiro = Celula();
        self.ultimo = Celula();
        self.qtd = 0

    def inserirNoInicio(self, item):
        novo = Celula(item, self.primeiro.prox)
        self.primeiro.prox = novo
        if (novo.prox == None): self.ultimo = novo
        self.qtd+=1

    def inserirNoFim(self, item):
        self.ultimo.prox = Celula(item);
        self.ultimo = self.ultimo.prox
        self.qtd+=1

    def removerNoInicio(self):
        remove = self.primeiro.prox
        self.primeiro.prox = remove.prox
        return remove.item

    def removerNoFim(self):
        aux = self.primeiro
        while (aux != self.ultimo):
            prev = aux
            aux = aux.prox
        remove = aux
        self.ultimo = prev
        self.ultimo.prox = None
        return remove.item

    def mostra(self):
        aux = self.primeiro.prox
        while (aux):
            print aux.item
            aux = aux.prox


def main():
    teste = ListaSimples()
    teste.inserirNoInicio(1)
    teste.inserirNoInicio(2)
    teste.inserirNoFim(5)
    teste.removerNoInicio()
    teste.removerNoFim()
    teste.mostra()

if __name__ == '__main__':
    main()
