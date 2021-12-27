def solution(s):
    if not s or s.strip():
        return "E5"
    s.strip()
    edges = s.split(" ")
    edges = [(chrs.split(",")[0][1:], chrs.split(",")[1][:-1]) for chrs in edges]
    graph = [[False for _ in range(26)] for _ in range(26)]
    children = {i: [] for i in range(26)}
    nodes = set()
    A = ord("A")
    # E1 more than 2 children; E2 Duplicate Edges
    E1, E2 = False, False
    for node1, node2 in edges:
        if graph[ord(node1) - A][ord(node2) - A]:
            E2 = True
        graph[ord(node1) - A][ord(node2) - A] = True
        if len(children[ord(node1) - A]) >= 2:
            E1 = True
        else:
            children[ord(node1) - A].append(ord(node2) - A)
        nodes.add(ord(node1) - A)
        nodes.add(ord(node2) - A)
    if E1:
        return "E1"
    if E2:
        return "E2"

    # E3: cycle; E4 multiple roots
    E3, E4 = False, False
    roots = set()
    for node2 in nodes:
        isRoot = True
        for node1 in range(26):
            if graph[node1][node2]:
                isRoot = False
        if isRoot:
            roots.add(node2)
        if not E3:
            visited = [False for _ in range(26)]
            E3 = isCycle(graph, node2, visited)
    if E3:
        return "E3"
    if len(roots) == 0:
        return "E3"
    if len(roots) > 1:
        return "E4"
    



def isCycle(graph, node, visited):
    pass
    


    # E2 

s = "(A,B) (C,D)"
solution(s)