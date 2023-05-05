# Iterative depending DFS
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
maxdepth = int(input("Enter the max depth:"))
level = 0
path = list()


def idls(start, goal, tree, path, level, maxdepth):
    print("current level ", level)
    path.append(start)
    if start == goal:
        print("goal node found")
        return path
    print("Goal not found: ", goal)
    if level == maxdepth:
        return False
    neighour = tree[start]
    for i in neighour:
        if idls(i, goal, tree, path, level+1, maxdepth):
            return path
        print(path.pop())
    return False


for i in range(maxdepth+1):
    path = list()
    result = idls(start, goal, tree, path, level, maxdepth)

if result:
    print("level present")
    print("Path is ", path)
else:
    print("Goal node found in the max depth")
