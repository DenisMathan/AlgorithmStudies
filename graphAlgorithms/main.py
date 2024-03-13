from graph import Graph

if __name__ == "__main__":
    graph = Graph([
        ("a", "b", 2),("a", "c", 4),("b", "c", 5),
        ("b", "d", 4),("b", "e", 9),("c", "e", 1),
        ("d", "e", 2),("c", "g", 2),("c", "h", 7),
        ("g", "h", 3),("g", "f", 1),("f", "i", 2),("i", "j", 6),
        ("g", "i", 6),
        ("h", "j", 5), ("g", "j", 8), ("j", "g", -9)
    ])
    # graph = Graph([
    #     ("a", "b", 5), ("a", "c", 1), ("b", "d", -3), ("c", "d", 2),
    #     ("a", "d", 3)
    # ])

    # graph.dijkstra('a', 'j')
    graph.belmanFord('a', 'j')