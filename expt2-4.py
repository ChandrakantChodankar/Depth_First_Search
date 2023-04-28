# depth limited Search
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
path = []


def dls(start, goal, path, level, maxdepth):
    print("current level", level)
    path.append(start)
    if start == goal:
        print("goal node found")
        return path
    if level == maxdepth:
        return False
    print("expanding current node", start)
    neighour = tree[start]
    for i in neighour:
        if dls(i, goal, path, level+1, maxdepth):
            return path
        print(path.pop())
    return False


result = dls(start, goal, path, level, maxdepth)
if result:
    print("level present")
    print(path)
else:
    print("total node found in the max depth")
