class Pathfinder:

    def belmanFord(self, nodes, edges, start, end):
        nodes[start].weight = 0
        for i in range(len(nodes)):
            for edge in edges:
                parentWeight = nodes[edge.parent[0]].weight
                childWeight = nodes[edge.child[0]].weight
                if parentWeight != None:
                    oldWeight = childWeight
                    newWeight = parentWeight + edge.weight
                    path = nodes[edge.parent[0]].path + [nodes[edge.child[0]].name]
                    if oldWeight == None or oldWeight > newWeight:
                        nodes[edge.child[0]].weight = newWeight
                        nodes[edge.child[0]].path = path

        for edge in edges:
                parentWeight = nodes[edge.parent[0]].weight
                childWeight = nodes[edge.child[0]].weight
                if(parentWeight + edge.weight < childWeight):
                    print("negative Circle!")
                    return
        print(nodes[end].path)
    
     

    def dijkstra(self, nodes, start, end):
        nodes = nodes.copy()
        nodes[start].weight = 0
        _nodes = {}
        #print(nodes)
        while len(nodes) > 0:
            startNode = self.getSmallestWeight(nodes) 
            for node in startNode.children + startNode.parents:
                if node.weight == None:
                    node.weight = startNode.weight + node.weights[startNode.name]
                    node.path = startNode.path + [node.name]
                elif node.weight > startNode.weight + node.weights[startNode.name]:
                    node.weight = startNode.weight +  node.weights[startNode.name]
                    node.path = startNode.path + [node.name]
                _nodes[node.name] = node
            nodes.pop(startNode.name)
        print(_nodes[end].path)
            

    def getSmallestWeight(self, nodes):
        weight= float("inf")
        node = None
        for id in nodes:
            _node = nodes[id]
            if _node.weight != None and _node.weight < weight:
                node = _node
                weight = _node.weight
        return node
    