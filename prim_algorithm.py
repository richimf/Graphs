import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
             for row in range(vertices)]

    # Imprime el vertice y peso
    def printMST(self, parent):
        print ("Edge \tWeight \tTotalweight")
        total_Weight = 0
        for i in range(1,self.V):
            total_Weight = total_Weight + self.graph[i][ parent[i]]
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ],"\t",total_Weight)


    # Funcion que encuentra el vertice con el valor minimo
    def minKey(self, key, mstSet):

        # encuentra el valor minimo
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index
    # construye el MST usando la matriz de adyacencias
    def primMST(self):
        #Key escoge el peso minimo en la arista de corte
        key = [sys.maxsize] * self.V
        parent = [None] * self.V #guarda el MST
        key[0] = 0   # si el vetice ya fue seleccionado lo vuelve cero
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):

            
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            # Actualiza el valor de los vertices adyacentes al vertice elegido
            #si la distancia es mas grande que la nueva distancia

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        self.printMST(parent)
