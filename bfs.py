def bfs(graph,start):
    visited=set()
    Queue=[start]
    while Queue:
        vertex=Queue.pop(0)
        if vertex not in visited:
            print(vertex,end="")
            visited.add(vertex)
        for n in graph[vertex]:
            if n not in visited:
                Queue.append(n)

graph={0:[1,2],1:[2,3],2:[0,1],3:[1,4],4:[2,3]}
bfs(graph,0)
