# traversal
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = input("Enter the start state: ")


def dfs_travel(tree):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        neighour = tree[node]
        for i in neighour:
            stack.append(i)
    return visited


print("DFS traversal is: ", dfs_travel(tree))

goal = input("Enter the goal state: ")


def dfs_path(tree):
    visited = []
    stack = [start]
    if start == goal:
        print("Start node is goal node")
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        neighour = tree[node]
        for i in neighour:
            if i not in visited:
                visited.append(i)
                stack.append(i)
                if i == goal:
                    return visited


print("Path is: ", dfs_path(tree))
