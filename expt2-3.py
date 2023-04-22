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
goal = input("Enter the goal state: ")


def dfs_sp(tree):
    visited = []
    stack = [[start]]
    if start == goal:
        print("start is the goal node")
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.append(node)
        neighour = tree[node]
        for i in neighour:
            new_path = list(path)
            new_path.append(i)
            stack.append(new_path)
            if i == goal:
                return new_path


print("path is ", dfs_sp(tree))
