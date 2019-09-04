

# 无向图
import heapq


class UndirectGraph(object):
    def __init__(self):
        self.nodes = []
        self.edge = {}

    def insert(self,a, b):
        if not(a in self.nodes):
            self.nodes.append(a)
            self.edge[a] = list()
        if not(b in self.nodes):
            self.nodes.append(b)
            self.edge[b] = list()
        self.edge[a].append(b)
        self.edge[b].append(a)

    def succ(self,a ):
        return self.edge[a]

    def show_nodes(self):
        return  self.nodes

    def show_egde(self):
        print(self.edge)

    def dfs(self,s, S=None, res = None):
        if S is None:
            S = set()

        if res is None:
            res = []

        res.append(s)
        S.add(s)
        for u in self.edge[s]:
            if u in S:
                continue
            S.add(u)
            self.dfs(u,S,res)

        return res

    def bfs(self, s):
        explored, queue = [], [s]
        explored.append(s)
        while queue:
            v = queue.pop(0)
            for w in self.edge[v]:
                if w not in explored:
                    explored.append(w)
                    queue.append(w)

        return explored


     def dijkstra(self, s,e):
        heap = [(0, s)]
        visited = []
        while heap:
            (cost, u) = heapq.heappop(heap)
            if u in visited:
                continue
            visited.append(u)
            if u == e:
                return cost
            for v,c in self.edge[u]:  # self.edge 带权边
                if v in visited:
                    continue
                next = cost + c
                heap.heappush(heap, (next, v))






# 有向图

class DirectGraph(object):
    def __init__(self):
        self.nodes = []
        self.edge = {}

    def insert(self, a, b):
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a] = list()
        if not ( b in self.nodes):
            self.nodes.append(b)
            self.edge[b] = list()

        self.edge[a].append(b)

    def succ(self, a):
        return self.edge[a]

    def show_egde(self):
        print(self.edge)

    def show_nodes(self):
        return self.nodes


class UndirectGraphMatrix(object):
    def __init__(self, vertex):
        self.vertex =vertex
        self.graph = [[0]*vertex for i in range(vertex)]

    def insert(self, u, v):
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1

    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(" ")





graph= UndirectGraphMatrix(5)
graph.insert(1,4)
graph.insert(4,2)
graph.insert(4,5)
graph.insert(2,5)
graph.insert(5,3)
graph.show()


#
#
# graph = UndirectGraph()
# graph.insert('0', '1')
# graph.insert('1','2')
# graph.insert('2', '3')
# graph.insert('0','2')
# graph.insert('0','1')
# graph.show_egde()
