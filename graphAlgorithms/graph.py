from pathfinder import Pathfinder;

class Node:
    name = ""

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.weights = {}

        self.path = [name]
        self.weight = None
        print("NodeName: " + self.name)

    def addChild(self, child, weight):
        self.children.append(child)
        self.weights[child.name] = weight

    def addParent(self, parent, weight):
        self.parents.append(parent)
        self.weights[parent.name] = weight

    def _reset(self):
        self.path = [self.name]
        self.weight = None
    

class Edge:
    weight = 0

    def __init__(self, parentId, childId, weight):
        self.parent = parentId[0],
        self.child = childId,
        self.weight = weight
        # print(parentId)



    
class Graph:
    def __init__(self, edges):
        self.nodes = {}
        self.edges = []
        self.pathFinder = Pathfinder()
        for e in edges:
            self.edges.append(Edge(e[0], e[1], e[2]))

            parent = self.nodes.get(e[0])
            child = self.nodes.get(e[1])
            if parent == None:
                parent = Node(e[0])
                self.nodes[e[0]] = parent
            if child == None:
                child = Node(e[1])
                self.nodes[e[1]] = child
            parent.addChild(self.nodes[e[1]], e[2])
            child.addParent(self.nodes[e[0]], e[2])
        self.printNodes()
    
    def printNodes(self):
        for nodeID in self.nodes:
            node = self.nodes[nodeID]
            print(nodeID, len(node.children), len(node.parents))

    def getSmallestWeight(self, nodes):
        weight= float("inf")
        node = None
        for id in nodes:
            _node = nodes[id]
            if _node.weight != None and _node.weight < weight:
                node = _node
                weight = _node.weight
        return node
    
    def _resetNodes(self):
        for id in self.nodes:
            self.nodes[id]._reset()

    def dijkstra(self, start, end):
        self._resetNodes()
        self.pathFinder.dijkstra(self.nodes, start, end)
    
    def belmanFord(self, start, end):
        self._resetNodes()
        self.pathFinder.belmanFord(self.nodes, self.edges, start, end)

