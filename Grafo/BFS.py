from collections import deque

def bfs(graph, v):
    visited = set()
    f = deque()

    visited.add(v)
    f.append(v)

    while f:
        u = f.popleft()

        print(u)

        for w in graph[u]:
            if w not in visited:
                visited.add(w)
                f.append(w)
    
    return visited

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }

    result = bfs(graph, 'A')
    print(result)

main()
