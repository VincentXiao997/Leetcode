class GraphNode:
    def __init__(self, id):
        self.val = None
        self.id = id
        self.edges = []

class Graph:
    def __init__(self, n):
        self.nodes = [GraphNode(i) for i in range(n)]

def solution(N, arr1, arr2):
    graph = Graph(N)
    for i in range(len(arr1)):
        graph.nodes[arr1[i]].edges.append(arr2[i])
        graph.nodes[arr2[i]].edges.append(arr1[i])
    nodeInfo = [(len(node.edges), node.id) for node in graph.nodes]
    nodeInfo.sort(reverse = 1)
    val = N
    for _, i in nodeInfo:
        graph.nodes[i].val = val
        val -= 1
    result = 0
    for i in range(len(arr1)):
        result += (graph.nodes[arr1[i]].val + graph.nodes[arr2[i]].val)
    return result

print(solution(5, [], []))