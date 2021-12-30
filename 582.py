class Solution:
    class Graph:
        def __init__(self, pid, ppid):
            self.nodes = {0:[]}
            for i in range(len(pid)):
                if pid[i] not in self.nodes:
                    self.nodes[pid[i]] = []
                if ppid[i] not in self.nodes:
                    self.nodes[ppid[i]] = []
                self.nodes[ppid[i]].append(pid[i])
            
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = self.Graph(pid, ppid)
        toRemove = set([kill])
        queue = collections.deque([kill])
        while queue:
            node = queue.popleft()
            for child in graph.nodes[node]:
                toRemove.add(child)
                queue.append(child)
        return toRemove
