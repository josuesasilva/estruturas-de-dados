#!usr/bin/env python
# -*- coding: utf-8 -*-

class No(object):
    
    def __init__(self, item=None):
        self.item = item
        self.esq = None
        self.dir = None


class ArvoreBinaria(object):

    def __init__(self):
        self.raiz = None
        self._flag = False

    def inserir(self, item, no=None):
        if (no == None):
            if (self.raiz == None):
                self.raiz = No(item)
            else:
                self.inserir(item, self.raiz)
        else:
            if (item < no.item):
                if (no.esq == None):
                    no.esq = No(item)
                else:
                    self.inserir(item, no.esq)
            else:
                if (no.dir == None):
                    no.dir = No(item)
                else:
                    self.inserir(item, no.dir)

    def mostraEmOrdem(self, no=None):
        if (no == None and not self._flag):
            self._flag = True
            self.mostraEmOrdem(self.raiz)
        if (no != None and self._flag):
            self.mostraEmOrdem(no.esq)
            print str(no.item),
            self.mostraEmOrdem(no.dir)

# testes
def main():
    teste = ArvoreBinaria()
    teste.inserir(1)
    teste.inserir(3)
    teste.inserir(2)
    teste.mostraEmOrdem()

if __name__ == '__main__':
    main()
