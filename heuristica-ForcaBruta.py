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
        origem_anterior = origem

        caminho.append(origem)
        if origem == destino:
            print("Origem = destino, você já chegou!")
        while origem != destino:
            for j in range(len(grafo.vizinhos[origem])):
                custo_aresta = grafo.obterCustoAresta(origem,grafo.vizinhos[origem][j])
                custo[custo_aresta] = grafo.vizinhos[origem][j]
            #print(custo)
            print("a partir de",origem)
            print("Menor custo dentre os caminhos = ",min(custo),"do vertice ",custo[min(custo)])
            if custo[min(custo)] not in caminho:
                caminho.append(custo[min(custo)])
                custo_caminho = custo_caminho + min(custo)
                origem_anterior = origem
                origem = custo[min(custo)]
                print("origem anterior",origem_anterior)
                print("caminho ate então2",caminho)
                print("new origem",origem)
            else:
                print("Já estive na lista",custo[min(custo)])
                print("eu tava em ",origem)
                grafo.vizinhos[origem].remove(custo[min(custo)]) #retir o repetido da lista de vizinhos e tenta dnv
                #print("quess",custo)
            dict.clear(custo) #limpa dicionario p não conter tdas as outras arestas
            if origem_anterior in grafo.vizinhos[origem]:
                grafo.vizinhos[origem].remove(origem_anterior)
        arq.write("\n")
        arq.write("Caminho")
        arq.write(str(caminho))
        arq.write("\n")
        arq.write("Custo = ")
        arq.write(str(custo_caminho))
        #print("Caminho = ",caminho)
        #print("Custo Caminho = ",custo_caminho)

    def Forca_Bruta(self,origem,destino):
        vetor = [1,2,3,4]
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
                        grafo.pos+= 1
                        #print(grafo.caminho)
                #        try:
                        grafo.caminho[possibilidades[0]].append(possibilidades)
                        grafo.custo[possibilidades[0]].append(grafo.obterCustoCaminho(possibilidades))
                        #print(grafo.caminho)
                #        except Exception as e:
                #            print (e)
                        #print(grafo.caminho)
            par_comb+= 1
        print()
        k = 0
        #arq.write("## Possibilidades de todos para todos ##")
        #arq.write("\n")
        for i in range(1,grafo.num_vertices + 1):
            for j in range(1,grafo.num_vertices + 1):
                menor_custo = 100000000
                for k in range(len(grafo.caminho[i])):
                    if(grafo.caminho[i][k][0] == i and grafo.caminho[i][k][len(grafo.caminho[i][k]) - 1] == j):
                        print(grafo.caminho[i][k],"custa ",grafo.custo[i][k])
                        #arq.write(str(grafo.caminho[i][k]))
                        #arq.write(" custo = ")
                        #arq.write(str(grafo.custo[i][k]))
                        if grafo.custo[i][k] < menor_custo:
                            #print("menor caminho atual", grafo.caminho[i][k])
                            menor_custo = grafo.custo[i][k]
                            grafo.guarda_coord_i = i
                            grafo.guarda_coord_k = k

                if i != j:
                    print("menor é", grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k]," de custo ",grafo.custo[grafo.guarda_coord_i][grafo.guarda_coord_k])
                    arq.write("\n")
                    arq.write("De ")
                    arq.write(str(grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k][0]))
                    arq.write(" para ")
                    arq.write(str(grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k][len(grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k]) - 1]))
                    arq.write("\n")
                    arq.write("Caminho ")
                    arq.write(str(grafo.caminho[grafo.guarda_coord_i][grafo.guarda_coord_k]))
                    arq.write(" de custo ")
                    arq.write(str(grafo.custo[grafo.guarda_coord_i][grafo.guarda_coord_k]))
                    arq.write(" é o menor")
                    arq.write("\n")

if __name__ == "__main__":

    arq = open('resultados.txt', 'w')
    grafo = Grafo(num_vertices = 4)
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
     'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15}

    # DE A PARA TODOS #
    grafo.adicionarAresta(d['A'], d['B'], 737)
    grafo.adicionarAresta(d['B'], d['A'], 737)

    grafo.adicionarAresta(d['A'], d['C'], 586)
    grafo.adicionarAresta(d['C'], d['A'], 586)

    grafo.adicionarAresta(d['A'], d['D'], 878)
    grafo.adicionarAresta(d['D'], d['A'], 878)

    grafo.adicionarAresta(d['A'], d['E'], 139)
    grafo.adicionarAresta(d['E'], d['A'], 139)

    grafo.adicionarAresta(d['A'], d['F'], 121)
    grafo.adicionarAresta(d['F'], d['A'], 121)

    grafo.adicionarAresta(d['A'], d['G'], 70)
    grafo.adicionarAresta(d['G'], d['A'], 70)

    grafo.adicionarAresta(d['A'], d['H'], 1803)
    grafo.adicionarAresta(d['H'], d['A'], 1803)

    grafo.adicionarAresta(d['A'], d['I'], 524)
    grafo.adicionarAresta(d['I'], d['A'], 524)

    grafo.adicionarAresta(d['A'], d['J'], 370)
    grafo.adicionarAresta(d['J'], d['A'], 370)

    grafo.adicionarAresta(d['A'], d['K'], 670)
    grafo.adicionarAresta(d['K'], d['A'], 670)

    grafo.adicionarAresta(d['A'], d['L'], 576)
    grafo.adicionarAresta(d['L'], d['A'], 576)

    grafo.adicionarAresta(d['A'], d['M'], 2786)
    grafo.adicionarAresta(d['M'], d['A'], 2786)

    grafo.adicionarAresta(d['A'], d['N'], 3820)
    grafo.adicionarAresta(d['N'], d['A'], 3820)

    grafo.adicionarAresta(d['A'], d['O'], 113)
    grafo.adicionarAresta(d['O'], d['A'], 113)

    # DE B PARA TODOS #
    grafo.adicionarAresta(d['B'], d['C'], 207)
    grafo.adicionarAresta(d['C'], d['B'], 207)

    grafo.adicionarAresta(d['B'], d['D'], 1138)
    grafo.adicionarAresta(d['D'], d['B'], 1138)

    grafo.adicionarAresta(d['B'], d['E'], 871)
    grafo.adicionarAresta(d['E'], d['B'], 871)

    grafo.adicionarAresta(d['B'], d['F'], 852)
    grafo.adicionarAresta(d['F'], d['B'], 852)

    grafo.adicionarAresta(d['B'], d['G'], 807)
    grafo.adicionarAresta(d['G'], d['B'], 807)

    grafo.adicionarAresta(d['B'], d['H'], 2196)
    grafo.adicionarAresta(d['H'], d['B'], 2196)

    grafo.adicionarAresta(d['B'], d['I'], 213)
    grafo.adicionarAresta(d['I'], d['B'], 213)

    grafo.adicionarAresta(d['B'], d['J'], 478)
    grafo.adicionarAresta(d['J'], d['B'], 478)

    grafo.adicionarAresta(d['B'], d['K'], 610)
    grafo.adicionarAresta(d['K'], d['B'], 610)

    grafo.adicionarAresta(d['B'], d['L'], 273)
    grafo.adicionarAresta(d['L'], d['B'], 273)

    grafo.adicionarAresta(d['B'], d['M'], 3362)
    grafo.adicionarAresta(d['M'], d['B'], 3362)

    grafo.adicionarAresta(d['B'], d['N'], 4369)
    grafo.adicionarAresta(d['N'], d['B'], 4369)

    grafo.adicionarAresta(d['B'], d['O'], 624)
    grafo.adicionarAresta(d['O'], d['B'], 624)

    # DE C PARA TODOS #
    grafo.adicionarAresta(d['C'], d['D'], 920)
    grafo.adicionarAresta(d['D'], d['C'], 920)

    grafo.adicionarAresta(d['C'], d['E'], 674)
    grafo.adicionarAresta(d['E'], d['C'], 674)

    grafo.adicionarAresta(d['C'], d['F'], 655)
    grafo.adicionarAresta(d['F'], d['C'], 655)

    grafo.adicionarAresta(d['C'], d['G'], 666)
    grafo.adicionarAresta(d['G'], d['C'], 666)

    grafo.adicionarAresta(d['C'], d['H'], 1978)
    grafo.adicionarAresta(d['H'], d['C'], 1978)

    grafo.adicionarAresta(d['C'], d['I'], 107)
    grafo.adicionarAresta(d['I'], d['C'], 107)

    grafo.adicionarAresta(d['C'], d['J'], 306)
    grafo.adicionarAresta(d['J'], d['C'], 306)

    grafo.adicionarAresta(d['C'], d['K'], 504)
    grafo.adicionarAresta(d['K'], d['C'], 504)

    grafo.adicionarAresta(d['C'], d['L'], 101)
    grafo.adicionarAresta(d['L'], d['C'], 101)

    grafo.adicionarAresta(d['C'], d['M'], 3163)
    grafo.adicionarAresta(d['M'], d['C'], 3163)

    grafo.adicionarAresta(d['C'], d['N'], 4184)
    grafo.adicionarAresta(d['N'], d['C'], 4184)

    grafo.adicionarAresta(d['C'], d['O'], 519)
    grafo.adicionarAresta(d['O'], d['C'], 519)

    #DE D PARA TODOS#
    grafo.adicionarAresta(d['D'], d['E'], 739)
    grafo.adicionarAresta(d['E'], d['D'], 739)

    grafo.adicionarAresta(d['D'], d['F'], 757)
    grafo.adicionarAresta(d['F'], d['D'], 757)

    grafo.adicionarAresta(d['D'], d['G'], 826)
    grafo.adicionarAresta(d['G'], d['D'], 826)

    grafo.adicionarAresta(d['D'], d['H'], 1142)
    grafo.adicionarAresta(d['H'], d['D'], 1142)

    grafo.adicionarAresta(d['D'], d['I'], 925)
    grafo.adicionarAresta(d['I'], d['D'], 925)

    grafo.adicionarAresta(d['D'], d['J'], 652)
    grafo.adicionarAresta(d['J'], d['D'], 652)

    grafo.adicionarAresta(d['D'], d['K'], 1281)
    grafo.adicionarAresta(d['K'], d['D'], 1281)

    grafo.adicionarAresta(d['D'], d['L'], 858)
    grafo.adicionarAresta(d['L'], d['D'], 858)

    grafo.adicionarAresta(d['D'], d['M'], 2302)
    grafo.adicionarAresta(d['M'], d['D'], 2302)

    grafo.adicionarAresta(d['D'], d['N'], 3309)
    grafo.adicionarAresta(d['N'], d['D'], 3309)

    grafo.adicionarAresta(d['D'], d['O'], 929)
    grafo.adicionarAresta(d['O'], d['D'], 929)

    # DE E PARA TODOS#
    grafo.adicionarAresta(d['E'], d['F'], 18)
    grafo.adicionarAresta(d['F'], d['E'], 18)

    grafo.adicionarAresta(d['E'], d['G'], 59)
    grafo.adicionarAresta(d['G'], d['E'], 59)

    grafo.adicionarAresta(d['E'], d['H'], 1664)
    grafo.adicionarAresta(d['H'], d['E'], 1664)

    grafo.adicionarAresta(d['E'], d['I'], 658)
    grafo.adicionarAresta(d['I'], d['E'], 658)

    grafo.adicionarAresta(d['E'], d['J'], 442)
    grafo.adicionarAresta(d['J'], d['E'], 442)

    grafo.adicionarAresta(d['E'], d['K'], 809)
    grafo.adicionarAresta(d['K'], d['E'], 809)

    grafo.adicionarAresta(d['E'], d['L'], 647)
    grafo.adicionarAresta(d['L'], d['E'], 647)

    grafo.adicionarAresta(d['E'], d['M'], 2647)
    grafo.adicionarAresta(d['M'], d['E'], 2647)

    grafo.adicionarAresta(d['E'], d['N'], 3681)
    grafo.adicionarAresta(d['N'], d['E'], 3681)

    grafo.adicionarAresta(d['E'], d['O'], 252)
    grafo.adicionarAresta(d['O'], d['E'], 252)

    #DE F PAR TODOS#
    grafo.adicionarAresta(d['F'], d['G'], 41)
    grafo.adicionarAresta(d['G'], d['F'], 41)

    grafo.adicionarAresta(d['F'], d['H'], 1682)
    grafo.adicionarAresta(d['H'], d['F'], 1682)

    grafo.adicionarAresta(d['F'], d['I'], 639)
    grafo.adicionarAresta(d['I'], d['F'], 639)

    grafo.adicionarAresta(d['F'], d['J'], 423)
    grafo.adicionarAresta(d['J'], d['F'], 423)

    grafo.adicionarAresta(d['F'], d['K'], 790)
    grafo.adicionarAresta(d['K'], d['F'], 790)

    grafo.adicionarAresta(d['F'], d['L'], 629)
    grafo.adicionarAresta(d['L'], d['F'], 629)

    grafo.adicionarAresta(d['F'], d['M'], 2665)
    grafo.adicionarAresta(d['M'], d['F'], 2665)

    grafo.adicionarAresta(d['F'], d['N'], 3699)
    grafo.adicionarAresta(d['N'], d['F'], 3699)

    grafo.adicionarAresta(d['F'], d['O'], 234)
    grafo.adicionarAresta(d['O'], d['F'], 234)

    #DE G PARA TODOS#
    grafo.adicionarAresta(d['G'], d['H'], 1751)
    grafo.adicionarAresta(d['H'], d['G'], 1751)

    grafo.adicionarAresta(d['G'], d['I'], 594)
    grafo.adicionarAresta(d['I'], d['G'], 594)

    grafo.adicionarAresta(d['G'], d['J'], 440)
    grafo.adicionarAresta(d['J'], d['G'], 440)

    grafo.adicionarAresta(d['G'], d['K'], 739)
    grafo.adicionarAresta(d['K'], d['G'], 739)

    grafo.adicionarAresta(d['G'], d['L'], 645)
    grafo.adicionarAresta(d['L'], d['G'], 645)

    grafo.adicionarAresta(d['G'], d['M'], 2734)
    grafo.adicionarAresta(d['M'], d['G'], 2734)

    grafo.adicionarAresta(d['G'], d['N'], 3768)
    grafo.adicionarAresta(d['N'], d['G'], 3768)

    grafo.adicionarAresta(d['G'], d['O'], 183)
    grafo.adicionarAresta(d['O'], d['G'], 183)

    #DE H PARA TODOS#
    grafo.adicionarAresta(d['H'], d['I'], 1983)
    grafo.adicionarAresta(d['I'], d['H'], 1983)

    grafo.adicionarAresta(d['H'], d['J'], 1710)
    grafo.adicionarAresta(d['J'], d['H'], 1710)

    grafo.adicionarAresta(d['H'], d['K'], 2263)
    grafo.adicionarAresta(d['K'], d['H'], 2263)

    grafo.adicionarAresta(d['H'], d['L'], 1845)
    grafo.adicionarAresta(d['L'], d['H'], 1845)

    grafo.adicionarAresta(d['H'], d['M'], 1437)
    grafo.adicionarAresta(d['M'], d['H'], 1437)

    grafo.adicionarAresta(d['H'], d['N'], 2442)
    grafo.adicionarAresta(d['N'], d['H'], 2442)

    grafo.adicionarAresta(d['H'], d['O'], 1911)
    grafo.adicionarAresta(d['O'], d['H'], 1911)

    #DE I PARA TODOS#
    grafo.adicionarAresta(d['I'], d['J'], 356)
    grafo.adicionarAresta(d['J'], d['I'], 356)

    grafo.adicionarAresta(d['I'], d['K'], 397)
    grafo.adicionarAresta(d['K'], d['I'], 397)

    grafo.adicionarAresta(d['I'], d['L'], 197)
    grafo.adicionarAresta(d['L'], d['I'], 197)

    grafo.adicionarAresta(d['I'], d['M'], 3172)
    grafo.adicionarAresta(d['M'], d['I'], 3172)

    grafo.adicionarAresta(d['I'], d['N'], 4193)
    grafo.adicionarAresta(d['N'], d['I'], 4193)

    grafo.adicionarAresta(d['I'], d['O'], 411)
    grafo.adicionarAresta(d['O'], d['I'], 411)

    #DE J PARA TODOS#
    grafo.adicionarAresta(d['J'], d['K'], 712)
    grafo.adicionarAresta(d['K'], d['J'], 712)

    grafo.adicionarAresta(d['J'], d['L'], 205)
    grafo.adicionarAresta(d['L'], d['J'], 205)

    grafo.adicionarAresta(d['J'], d['M'], 2884)
    grafo.adicionarAresta(d['M'], d['J'], 2884)

    grafo.adicionarAresta(d['J'], d['N'], 3891)
    grafo.adicionarAresta(d['N'], d['J'], 3891)

    grafo.adicionarAresta(d['J'], d['O'], 360)
    grafo.adicionarAresta(d['O'], d['J'], 360)

    #DE K PARA TODOS#
    grafo.adicionarAresta(d['K'], d['L'], 584)
    grafo.adicionarAresta(d['L'], d['K'], 584)

    grafo.adicionarAresta(d['K'], d['M'], 3344)
    grafo.adicionarAresta(d['M'], d['K'], 3344)

    grafo.adicionarAresta(d['K'], d['N'], 4355)
    grafo.adicionarAresta(d['N'], d['K'], 4355)

    grafo.adicionarAresta(d['K'], d['O'], 556)
    grafo.adicionarAresta(d['O'], d['K'], 556)

    #DE L PARA TODOS#
    grafo.adicionarAresta(d['L'], d['M'], 3089)
    grafo.adicionarAresta(d['M'], d['L'], 3089)

    grafo.adicionarAresta(d['L'], d['N'], 4096)
    grafo.adicionarAresta(d['N'], d['L'], 4355)

    grafo.adicionarAresta(d['L'], d['O'], 556)
    grafo.adicionarAresta(d['O'], d['L'], 556)

    #DE M PARA TODOS#
    grafo.adicionarAresta(d['M'], d['N'], 1034)
    grafo.adicionarAresta(d['N'], d['M'], 1034)

    grafo.adicionarAresta(d['M'], d['O'], 2912)
    grafo.adicionarAresta(d['O'], d['M'], 2912)

    # DE N PARA todos
    grafo.adicionarAresta(d['N'], d['O'], 3936)
    grafo.adicionarAresta(d['O'], d['N'], 3936)
    print(grafo.vizinhos)
    #print("minimo",min(grafo.vizinhos[5]))
    #print("tam_list",len(grafo.vizinhos[5]))

    arq.write("Heuristica")
    #for i in range(1,3):
        #for j in range(1,3):
    Distances(grafo.vizinhos).Heuristica(1,3)
    print()
    print("Força Bruta")
    arq.write("\n")
    arq.write("Força Bruta")
    arq.write("\n")
    #Distances(grafo.vizinhos).Forca_Bruta(d['A'],d['F'])
    print("Fim!")
    arq.close()
