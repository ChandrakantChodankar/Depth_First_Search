# Goal Search
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
visited = []


def dfs(tree, start):
    if start not in visited:
        visited.append(start)
        print(start, end=" ")
    neighour = tree[start]
    for i in neighour:
        if goal in visited:
            break
        else:
            dfs(tree, i)


dfs(tree, start)
