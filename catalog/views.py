import catalog.algorithmHome as myhome
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render



# Create your views here.
def homepage(request):
    return render(request, 'index.html', locals())



def inputByWeb(nodeCost, edgeCost, sdN):
    # nodeCost = 1 2 3 4
    # edgeCost = 1 2 3\n 1 3 5
    inp = str(nodeCost)
    nodeCost = inp.split()
    nodeN = len(nodeCost)
    graphTable = []
    nodes = []
    for i in range(nodeN):
        nodes.append(str('n%d' % (i + 1)))
        graphTable.append([myhome.inf] * nodeN)
    for i in range(nodeN):
        nodeCost[i] = int(nodeCost[i])
        graphTable[i][i] = nodeCost[i]
    # edgeCost
    inp = str(edgeCost)
    edgeCost = inp.split('\r\n')
    connectN = len(edgeCost) - 1
    for i in range(connectN):
        connectCost = edgeCost[i].split(" ")
        graphTable[int(connectCost[0]) - 1][int(connectCost[1]) - 1] = int(connectCost[2])
        graphTable[int(connectCost[1]) - 1][int(connectCost[0]) - 1] = int(connectCost[2])
    # sN dN
    sdN = sdN.split()
    print(sdN)
    sN = str('n%s' % (sdN[0]))
    dN = str('n%s' % (sdN[1]))
    graph = myhome.Graph(graphTable, nodeCost, nodes)
    minCost, minRoute = myhome.dijkstra(graph.graphDict, graph.nodesDict, sN, dN)
    return str(str(minCost)+" "+minRoute)

def home(request,n = '0000'):
    if request.method == 'POST':
        st1 = request.POST['value1']
        st2 = request.POST['value2']
        st3 = request.POST['value3']
        st = str(inputByWeb(st1, st2, st3))
    if n == '0000':
        return render(request, 'index.html', locals())
    else:
        return render(request, 'ok.html', {'string': st})


def question_id(args):
    pass


def printf(request):

    st = 'None input'
    if request.method == 'POST':
        a = request.POST['value1']
        b = request.POST['value2']
        c = request.POST['value3']
        print(a, b,c)
        st = str(inputByWeb(a, b, c))
    return render(request, 'ok.html', locals())

