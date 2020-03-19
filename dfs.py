# yo nibbas need to concentrate...

# DO NOT COPY ME YOU WON'T GRADUATE...

# Pehle Bredth Frst Search smjho..
# Depth First Search implemention
# graph imaagii attach ki ha wo zra dekh lo..

# dictionary create kr lo
graph = {'A': set(['B', 'C']),                         # single quote/double quote aik hi baat ha..
         'B': set(['A', 'D', 'E']),                    # vertex: edges--vertex
         'C': set(['A', 'F']),                               
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(graph)                                           # check kr lo dictionary bni ha k nhi

#dfs k sahi trh chlny ki umeed...
def dfs(graph, startingNode, visited = None):
    if visited is None:
        visited = set()
    visited.add(startingNode)
    neighbors = graph[startingNode]
    print(startingNode)                                # print ho rhi nodes,,,

    for nextNode in neighbors - visited:               # bohat khufnak dekhny wali cheez jo k ha nhi
        dfs(graph, nextNode, visited)                  # Recursive call ,, time complexity bachao jo k frq nhi prta, wrna is link pe jao "www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/"
    return visited                  

dfs(graph, 'A')                                        # {'A', 'C', 'F', 'E', 'B', 'D', 'B'}