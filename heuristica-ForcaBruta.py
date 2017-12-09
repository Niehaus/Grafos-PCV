#!/bin/python
# encoding: utf-8
import random, math, itertools
from haversine import haversine

class Aresta:

    def __init__(self, origem, destino, custo):
        self.origem = origem
        self.destino = destino
        self.custo = custo

    def setOrigem(self):
        return self.origem

    def setDestino(self):
        return self.destino

    def setCusto(self):
        return self.custo

# classe que representa um grafo (grafos completos)
class Grafo:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices # número de vértices do grafo
        self.arestas = {} # dicionário com as arestas
        self.vizinhos = {} # dicionário com todos os vizinhos de cada vértice

        self.vizinhos_visitados = 0
        self.pos = 0
        self.guarda_coord_i = 1
        self.guarda_coord_k = 1
        self.caminho = {}
        self.menores_caminhos = {}
        self.custo = {}
        self.custo_caminho = {}
        self.caminho_antes = []
        self.caminho_lista = []
        self.visitados = []
        self.lista_aux = []

    def adicionarAresta(self, origem, destino, custo):
        aresta = Aresta(origem = origem, destino = destino, custo = custo)
        self.arestas[(origem, destino)] = aresta
        if origem not in self.vizinhos:
            self.vizinhos[origem] = [destino]
        else:
            self.vizinhos[origem].append(destino)

    def obterCustoAresta(self, origem, destino):
        return self.arestas[(origem, destino)].setCusto()
#vetor2 = [3,2,1]
    def obterCustoCaminho(self, caminho):
        custo = 0
        for i in range(0,len(caminho) - 1):
            custo += self.obterCustoAresta(caminho[i], caminho[i+1])
        return custo

class GrafoCompleto(Grafo):
    # gera um grafo completo
    def gerar(self):
        for i in range(1, self.num_vertices + 1):
            for j in range(1, self.num_vertices + 1):
                if i != j:
                    peso = random.randint(1, 10)
                    self.adicionarAresta(i, j, peso)

class Distances(Grafo):

    def Heuristica(self, origem, destino):
        print(grafo.vizinhos)
        caminho = []
        custo = {}
        custo_caminho = 0
        lista = []

        caminho.append(origem)
        if origem == destino:
            print("Origem = destino, você já chegou!")
        while origem != destino:
            for j in range(len(grafo.vizinhos[origem])):
                custo_aresta = grafo.obterCustoAresta(origem,grafo.vizinhos[origem][j])
                custo[custo_aresta] = grafo.vizinhos[origem][j]
            #print(custo)
            #print("Menor custo dentre os caminhos = ",min(custo))
            #print("Vem do vertice = ",custo[min(custo)])
            caminho.append(custo[min(custo)])
            custo_caminho = custo_caminho + min(custo)
            origem_anterior = origem
            origem = custo[min(custo)]
            dict.clear(custo) #limpa dicionario p não conter tdas as outras arestas
            if origem_anterior in grafo.vizinhos[origem]:
                grafo.vizinhos[origem].remove(origem_anterior)
        print("Caminho = ",caminho)
        print("Custo Caminho = ",custo_caminho)

    def Forca_Bruta(self,origem,destino):
        vetor = [1,2,3,4,5,6]
        for i in range(1,grafo.num_vertices + 1):
            grafo.caminho[i] = []
            grafo.custo[i] = []
        par_comb = 2
        while(par_comb != grafo.num_vertices + 1):
            for possibilidades in itertools.permutations(vetor,par_comb): #Verificação se é um caminho possivel baseado no grafo
                grafo.vizinhos_visitados = 0
                for i in range(0,len(possibilidades) - 1):
                    if possibilidades[i] in grafo.vizinhos[possibilidades[i + 1]]:#Verifica se i é vizinho de i + 1
                        grafo.vizinhos_visitados+= 1
                    if grafo.vizinhos_visitados == (len(possibilidades) - 1):#guarda caminhos possiveis baseado nos vizinhos e seus custos
                        print("Caminhos possiveis:",possibilidades)
                        grafo.pos+= 1
                        grafo.caminho[possibilidades[0]].append(possibilidades)
                        grafo.custo[possibilidades[0]].append(grafo.obterCustoCaminho(possibilidades))
            par_comb+= 1
        print()
        k = 0
        print("## Possibilidades de todos para todos ##")
        for i in range(1,grafo.num_vertices + 1):
            for j in range(1,grafo.num_vertices + 1):
                menor_custo = 100000000
                for k in range(len(grafo.caminho[i])):
                    if(grafo.caminho[i][k][0] == i and grafo.caminho[i][k][len(grafo.caminho[i][k]) - 1] == j):
                        #print("i = ",i,"j = ",j)
                        print(grafo.caminho[i][k],"custo = ",grafo.custo[i][k])
                        if grafo.custo[i][k] < menor_custo:
                            menor_custo = grafo.custo[i][k]
                            grafo.guarda_coord_i = i
                            grafo.guarda_coord_k = k
                if i != j:
                    print("De",grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k][0] ,"para",grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k][len(grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k]) - 1])
                    print("Caminho",grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k],"de custo",grafo.custo[grafo.guarda_coord_i][grafo.guarda_coord_k],"é o menor")
                    print()

if __name__ == "__main__":

    grafo = Grafo(num_vertices = 6)
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
    grafo.adicionarAresta(d['A'], d['B'], 3)
    grafo.adicionarAresta(d['B'], d['A'], 3)

    grafo.adicionarAresta(d['A'], d['E'], 10)
    grafo.adicionarAresta(d['E'], d['A'], 10)

    grafo.adicionarAresta(d['B'], d['D'], 2)
    grafo.adicionarAresta(d['D'], d['B'], 2)

    grafo.adicionarAresta(d['C'], d['E'], 1)
    grafo.adicionarAresta(d['E'], d['C'], 1)

    grafo.adicionarAresta(d['C'], d['B'], 1)
    grafo.adicionarAresta(d['B'], d['C'], 1)

    grafo.adicionarAresta(d['C'], d['D'], 3)
    grafo.adicionarAresta(d['D'], d['C'], 3)

    grafo.adicionarAresta(d['E'], d['F'], 4)
    grafo.adicionarAresta(d['F'], d['E'], 4)

    grafo.adicionarAresta(d['F'], d['D'], 6)
    grafo.adicionarAresta(d['D'], d['F'], 6)


    print(grafo.vizinhos)
    #print("minimo",min(grafo.vizinhos[5]))
    #print("tam_list",len(grafo.vizinhos[5]))

    print("Heuristica")
    #Distances(grafo.vizinhos).Heuristica(d['F'],d['A'])
    print()
    print("Força Bruta")
    Distances(grafo.vizinhos).Forca_Bruta(d['A'],d['F'])
