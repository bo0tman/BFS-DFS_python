# yo niggas need to concentrate...

# DO NOT COPY ME YOU WON'T GRADUATE...

# Breath First Search impletamention
# graph imaagii attach ki ha wo bhi dekh lo..

# dictionary create kr lo
graph = {'A': set(['B', 'C']),                         # single quote/double quote aik hi baat ha..
         'B': set(['A', 'D', 'E']),                    # vertex: edges--vertex
         'C': set(['A', 'F']),                               
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(graph)                                           # check kr lo dictionary bni ha k nhi

#bfs k sahi trh chlny ki umeed...
def bfs(graph, startingNode):
    visited, queue = set(), [startingNode]             # mutilple assignment ha, ghabrana nhi ha...
    while queue:
        vertex = queue.pop(0)                          # vertex/node aik hi baat ha..   
        neighbors = graph[vertex]
        print(vertex)                                  # sath sath print krwai jao jis vertex pe ho
        
        for nextNode in neighbors:                 # thora sa dimagh lgao smj a jae ga
                if nextNode not in visited:
                    visited.add(nextNode)
                    queue.extend(nextNode)
    return visited                                                

bfs(graph, 'A')                                        # {'A', 'B', 'C', 'D', 'E', 'A', 'F'}