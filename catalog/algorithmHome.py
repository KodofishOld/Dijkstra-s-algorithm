import numpy as np

inf = np.inf


class Graph:
    graphTable = []
    graphEdge = []
    graphDict = None
    nodesDict = {}
    nodes = []
    nodesCost = []

    def __init__(self,graphTable,nodesCost,nodes):
        self.graphTable = graphTable
        self.nodes = nodes
        self.nodesCost = nodesCost
        print("graphTable", graphTable, nodes, nodesCost)
        self.convertFormat()

    def convertFormat(self):
        nodes = self.nodes
        nodesCost = self.nodesCost
        graphTable = self.graphTable
        graphEdge = self.graphEdge
        graphDict = {}
        for i, j in enumerate(nodes):
            self.nodesDict.update({j: nodesCost[i]})
        for i in nodes:
            for j in nodes:
                if (graphTable[nodes.index(i)][nodes.index(j)] != inf):
                    graphEdge.append([i, j, graphTable[nodes.index(i)][nodes.index(j)]])
            # (head,tail,cost)
        print("graphEdge", graphEdge)
        print("length_graphEdge", len(graphEdge))

        for i in range(0, len(graphEdge)):
            sN = graphEdge[i][0]
            dN = graphEdge[i][1]
            c = graphEdge[i][2]
            print(sN, dN, c)
            if (sN != dN):
                print("length_graphEdge", "AAA")
                for x in range(0, len(graphEdge)):
                    if (graphEdge[x][0] == dN and graphEdge[x][0] == graphEdge[x][1]):
                        addition = graphEdge[x][2]
                        graphEdge[i][2] = addition + graphEdge[i][2]
                        break

        for tail, head, cost in graphEdge:
            if (tail == head):
                cost = 0
            graphDict.setdefault(tail, {}).update({head: cost})
        print("graphDict", graphDict)
        # 'n1':[('n1',cost), ... ]
        self.nodes = nodes
        self.graphTable = graphTable
        self.graphEdge = graphEdge
        self.graphDict = graphDict


def getMinNode(costTable, foundTable):
    minNode = None
    minCost = inf
    print("costTable，foundTable", costTable, foundTable)
    for i in costTable:
        if not foundTable.get(i):
            if (costTable.get(i) < minCost):
                print("FUCK")
                minCost = costTable.get(i)
                minNode = i
    print("minNode", minNode)
    return minNode


def dijkstra(graphDict, nodesDict, sN, dN):
    print("grapgDict", len(graphDict))
    nodeNum = len(graphDict)
    print("keys", graphDict.keys())
    foundTable = {}
    costTable = {}
    routeTable = {}
    # init
    for i in graphDict.keys():
        costTable.update({i: inf})
        foundTable.update({i: False})
        routeTable.update({i: sN})
    foundTable.update({sN: True})
    for i in graphDict.get(sN):
        costTable.update({i: graphDict.get(sN).get(i)})
    print("CF", costTable, foundTable)
    # end init
    print("RF", routeTable, foundTable)
    for _ in range(nodeNum):
        minCostNode = getMinNode(costTable, foundTable)

        foundTable.update({minCostNode: True})
        for i in costTable.keys():
            try:
                newCost = costTable.get(minCostNode) + graphDict.get(minCostNode).get(i)
            except TypeError:
                newCost = inf  # costTable.get(minCostNode)
            except AttributeError:
                newCost = inf
            print("compare", i, costTable.get(i), newCost)
            if (costTable.get(i) > newCost):
                costTable.update({i: newCost})
                routeTable.update({i: minCostNode})
                print("rt", routeTable)
    minCost = costTable.get(dN) - nodesDict.get(dN)
    print(routeTable)
    minRoute = dN
    pN = dN
    print("minCost", minCost)
    while (routeTable.get(pN) != sN):
        pN = str(routeTable.get(pN))
        minRoute = pN + '->' + minRoute
    minRoute = sN + '->' + minRoute
    print("minCost", minCost, minRoute)
    return minCost,minRoute

# print(dijkstra(graphDict,"n1","n4"))

def inputNodesInfoByConsole():
    nodeN = int(input())
    inp = str(input())
    graphTable = []
    nodes = []
    for i in range(nodeN):
        nodes.append(str('n%d' % (i + 1)))
        graphTable.append([inf] * nodeN)

    # nodeCost
    nodeCost = inp.split()
    print("nodeCost", nodeCost)
    for i in range(nodeN):
        nodeCost[i] = int(nodeCost[i])
        graphTable[i][i] = nodeCost[i]
    print("graphTable", graphTable)
    # edgeCost
    connectN = int(input())
    for i in range(connectN):
        inp = str(input())
        connectCost = inp.split()
        print("connectCost", connectCost)
        graphTable[int(connectCost[0]) - 1][int(connectCost[1]) - 1] = int(connectCost[2])
        graphTable[int(connectCost[1]) - 1][int(connectCost[0]) - 1] = int(connectCost[2])
    # sN dN
    inp = str(input())
    sdN = inp.split()
    sN = str('n%s' % (sdN[0]))
    dN = str('n%s' % (sdN[1]))
    graph = Graph(graphTable, nodeCost, nodes)
    dijkstra(graph.graphDict, graph.nodesDict, sN, dN)


if __name__ == '__main__':
    # inputNodesInfoByConsole()
    graph = Graph()
    # inputNodesInfoByConsole()
    dijkstra(graph.graphDict, graph.nodesDict, "n1", "n4")