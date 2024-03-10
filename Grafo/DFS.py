def dfs(graph):
    visited = set()

    def dfs_recursive(vertex):
        visited.add(vertex)
        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex not in visited:
                dfs_recursive(adjacent_vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs_recursive(vertex)

    return visited

def main():
    # Exemplo de uso
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }

    result = dfs(graph)
    print(result)
    
main()