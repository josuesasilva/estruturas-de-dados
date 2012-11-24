#!/usr/bin/env python

class No(object):
    def __init__(self, item=None, ant=None):
        self.item = item
        self.ant = ant

class Pilha(object):
    def __init__(self):
        self.topo = No()
        self.qtd = 0

    def push(self, item):
        novono = No(item, self.topo)
        self.topo = novono
        self.qtd+=1

    def pop(self):
        if (self.qtd == 0): return
        self.topo = self.topo.ant
        self.qtd-=1

    def mostra(self):
        aux = self.topo
        while (True):
            if (aux.item == None): return
            print aux.item
            aux = aux.ant


def main():
    teste = Pilha()
    teste.push(3);
    teste.push(1);
    teste.push(5);
    teste.mostra();
    teste.pop()
    teste.mostra();


if __name__ == '__main__':
    main()
