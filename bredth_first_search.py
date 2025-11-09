graph = {
    '5' = ['3','7']
    '3' = ['2','4']
    '7' = ['8']
    '2' = []
    '4' = ['8']
    '8' = []
}
visited = []
queue = []

def bfs(visited , graph ,node) # this function used for BFS , the node is initial with first node which is 5 in here
    visited.append(node)
    queue.append(node)
    
    while queue: # this part is for visiting each node , continue till it's have value
        m = queue.pop(0)
        print(m, end = " ")
        
        for neighbour in graph(m)
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
                
bfs( visited,graph ,'5')