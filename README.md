# Graphs 



Test 

Minimum Spanning Tree with Prim's algorithm (prim_algorithm.py) 

    g  = Graph(5) 
    g.graph = [ [0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]]

    g.primMST();


Maximum Spanning Tree with inverse Prim's algorithm (invprim.py)

    g = Graph(5)
    g.graph = [ [0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]]

    g.primMST2();


Ford–Fulkerson Algorithm (FordFulkerson.py)

    graph = [[0, 16, 13, 0,  0,  0],
            [0, 0,  10, 12, 0,  0],
            [0, 4,  0,  0,  14, 0],
            [0, 0,  9,  0,  0, 20],
            [0, 0,  0,  7,  0,  4],
            [0, 0,  0,  0,  0, 0 ]]

    g = Graph(graph)

    source = 0; sink = 5

    print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))



Prüfer Sequence to Labeled Tree (prufer2.py)

    g.build_tree([3, 3, 3, 4])

