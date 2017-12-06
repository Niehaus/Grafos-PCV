#!/bin/python
# encoding: utf-8
import random, math
from haversine import haversine

class Aresta:

    def __init__(self, origem, destino, custo):
        self.origem = origem
        self.destino = destino
        self.custo = custo
        self.visitado = 1

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

        self.caminho = []
        self.caminho_antes = []
        self.caminho_lista = []
        self.custo = {}
        self.custo_caminho = {}
        self.visitados = []
        self.pos = 0
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

    def obterCustoCaminho(self, caminho):
        custo = 0
        for i in range(self.num_vertices - 1):
            custo += self.obterCustoAresta(caminho[i], caminho[i+1])
        # adiciona o último custo
        custo += self.obterCustoAresta(caminho[-1], caminho[0])
        return custo

    def setaVisitados(self):
        for i in range(1,self.num_vertices):
            self.visitados.append(0)
            return self.visitados



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
        #print("custo = ",grafo.obterCustoAresta(origem,min(grafo.vizinhos[origem])))
        caminho.append(origem)
        if origem == destino:
            print("Origem = destino, você já chegou!")
        #print("## INICIO ##")
        while origem != destino:
            #print("Caminhos possiveis:",grafo.vizinhos[origem])
            for j in range(len(grafo.vizinhos[origem])):
                custo_aresta = grafo.obterCustoAresta(origem,grafo.vizinhos[origem][j])
                custo[custo_aresta] = grafo.vizinhos[origem][j]
            print(custo)
            print("Menor custo dentre os caminhos = ",min(custo))
            print("Vem do vertice = ",custo[min(custo)])
            caminho.append(custo[min(custo)])
            custo_caminho = custo_caminho + min(custo)
            print("new path",caminho)
            origem_anterior = origem
            origem = custo[min(custo)]
            dict.clear(custo) #limpa dicionario p não conter tdas as outras arestas
            if origem_anterior in grafo.vizinhos[origem]:
                grafo.vizinhos[origem].remove(origem_anterior)
            print("new origem",origem)
            print("old origem",origem_anterior)
        print("Caminho = ",caminho)
        print("Custo Caminho = ",custo_caminho)

    def Forca_Bruta(self,origem,destino):
        j = 0
        print(grafo.visitados)
        if origem not in grafo.caminho_lista:
            grafo.caminho_lista.append(origem)


             #aquele vertice foi visitado
            #print("INDEX",origem)
        #print("V.ORIGINAL = ",origem)
        #print("custo = ",grafo.obterCustoAresta(origem,min(grafo.vizinhos[origem])))
        for j in range(len(grafo.vizinhos[origem])):
            print("Vizinho",j, "da origem",origem,"=",grafo.vizinhos[origem][j])
            if grafo.vizinhos[origem][j] not in grafo.caminho_lista:
                print("Não estou na lista")#grafo.caminho_lista.append(grafo.vizinhos[origem][j])
            else:
                #print("Eu já estava na lista",grafo.vizinhos[origem][j])
                continue #Ainda a ser analisado
            print("Caminho Lista =",grafo.caminho_lista)
            if grafo.vizinhos[origem][j] == destino: #Se o vertice a frente da origem for o destino.
                grafo.caminho_lista.append(destino)
                grafo.lista_aux = grafo.caminho_lista[:]
                grafo.caminho.insert(grafo.pos,grafo.lista_aux)
                print("Caminhos possiveis: ",grafo.caminho)
                grafo.caminho_lista.pop()
                print("Caminho Lista.pop =",grafo.caminho_lista)
                print(len(grafo.caminho_lista))
                #print(grafo.caminho_lista[len(grafo.caminho_lista)])
                print(grafo.visitados)
            else:
                print("Não sou destino",grafo.vizinhos[origem][j])
            #Se não for destino e não tiver mais vizinhos viaveis, então NÃO É SOLUÇÃO.
            #Se eu não estiver na caminho_lista posso ser adicionado
                if grafo.vizinhos[origem][j] not in grafo.caminho_lista:
                    grafo.caminho_lista.append(grafo.vizinhos[origem][j])
                    print("VISITOU",grafo.vizinhos[origem][j])
                    print(grafo.caminho_lista)
                #if grafo.visitados[grafo.vizinhos[origem][j]] == 1:
                #    print("FUI VISITADO",grafo.vizinhos[origem][j])
                Distances(grafo.vizinhos).Forca_Bruta(grafo.vizinhos[origem][j],destino)
                print(grafo.caminho_lista)
























"""
        print(grafo.vizinhos[origem][j],"vizinho de",origem)
            if grafo.vizinhos[origem][j] == destino:
                grafo.caminho_lista.append(grafo.vizinhos[origem][j])
                grafo.lista_aux = grafo.caminho_lista[:]
                grafo.caminho.insert(grafo.pos,grafo.lista_aux)
                if any(existe != None for existe in range(grafo.vizinhos[origem][j])):
                #    print("origem atual =",origem)
                #    print("intervalo",grafo.caminho_lista[origem - 1:destino])
                #    print("oldlist =",grafo.caminho_lista)
                    del grafo.caminho_lista[origem - 1:destino]
                    #grafo.caminho_lista.remove(origem)
                    #grafo.caminho_lista.remove(destino)
                #    print("newlist =",grafo.caminho_lista)
                else:
                #    print("não tem mais vizinhos, limpa lista antiga = ",grafo.caminho_lista)
                    grafo.caminho_lista = []
                grafo.pos += 1
                print("Caminhos possiveis",grafo.caminho)

            #print(caminho_lista)
            if grafo.vizinhos[origem][j] != destino:
                if grafo.vizinhos[origem][j] in grafo.caminho_lista:
                    print("Já estou na lista == ", grafo.vizinhos[origem][j])
                    continue
                print(grafo.vizinhos[origem][j],"não é destino")
                origem_anterior = grafo.vizinhos[origem][j]
                #print("Lista de predecessores =",grafo.pred)
                if origem not in grafo.caminho_lista:
                    grafo.caminho_lista.append(origem)

                grafo.caminho_lista.append(grafo.vizinhos[origem][j])
                #print("LISTA ATE AQUI - ANTERIOR = ",grafo.vizinhos[origem])
                if origem in grafo.vizinhos[grafo.vizinhos[origem][j]]:
                    print("Removi",origem,"da lista de",grafo.vizinhos[origem][j])
                    grafo.vizinhos[grafo.vizinhos[origem][j]].remove(origem) #remove anterior p evitar loop
                #print("vizinho anterior de ",origem,":",origem_anterior)
                #print("vizinhos de",grafo.vizinhos[origem][j],":",grafo.vizinhos[grafo.vizinhos[origem][j]])
                #print("caminho lista",grafo.caminho_lista)
                print("FIM V ATUAL")
                Distances(grafo.vizinhos).Forca_Bruta(grafo.vizinhos[origem][j],destino)


                print(grafo.caminho)"""


if __name__ == "__main__":

    grafo = Grafo(num_vertices = 7)
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
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
