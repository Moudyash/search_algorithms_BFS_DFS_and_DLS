from collections import deque


def breadth_first_search(graph, start, goal):
    found = False
    fringe = deque([start])
    visited = set([start])
    came_from = {start: None}

    while not found and fringe:
        current = fringe.pop()
        if current == goal:
            found = True
            break

        # print(current, end = " ")

        for node in neighbors(current):
            if node not in visited:
                visited.add(node)
                fringe.appendleft(node)
                came_from[node] = current

    if found:
        print('Path:', end=' ')
        print_path(came_from, goal)
    # print(); return came_from
    else:
        print('No path from {} to {}'.format(start, goal))


def neighbors(node):
    try:
        return graph[node]
    except KeyError:
        return []


def print_path(came_from, goal):
    parent = came_from[goal]
    if parent:
        print_path(came_from, parent)
    else:
        print(goal, end='');return
    print(' =>', goal, end='')


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '4': ['8']
}

start, goal = '5', '8'
print(f"""
breadth first search:
graph:{graph}

""")
breadth_first_search(graph, start, goal)


def depth_first_search(graph, start, goal):
    found = False
    fringe = deque([start])
    visited = set()
    came_from = {start: None}

    while not found and len(fringe):
        current = fringe.pop()

        # print(current, end = " ")

        if current not in visited:
            visited.add(current)
            fringe.extend(reversed(neighbors(current)))

        if current == goal:
            found = True
            break

        for node in neighbors(current):
            came_from[node] = current

    if found:
        print('Path:', end=' ')
        print_path(came_from, goal)
    else:
        print('No path from {} to {}'.format(start, goal))


def neighbors(node):
    try:
        return graph[node]
    except KeyError:
        return []


def print_path(came_from, goal):
    parent = came_from[goal]
    if parent:
        print_path(came_from, parent)
    else:
        print(goal, end='');return
    print(' =>', goal, end='')


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '4': ['8']
}

start, goal = '5', '8'
print("\ndepth first search:")
depth_first_search(graph, start, goal)


def depth_limited_search(graph, start, goal, limit=-1):
    found = False
    fringe = deque([(0, start)])
    visited = set([start])
    came_from = {start: None}

    while not found and fringe:
        depth, current = fringe.pop()
        if current == goal:
            found = True
            break

        # print(current, end = " ")
        if limit == -1 or depth < limit:
            for node in neighbors(current):
                if node not in visited:
                    visited.add(node)
                    fringe.append((depth + 1, node))
                    came_from[node] = current

    if found:
        print('Path:', end=' ')
        print_path(came_from, goal)
    # print(); return came_from
    else:
        print('No path from {} to {}'.format(start, goal))


def neighbors(node):
    try:
        return graph[node]
    except KeyError:
        return []


def print_path(came_from, goal):
    parent = came_from[goal]
    if parent:
        print_path(came_from, parent)
    else:
        print(goal, end='');return
    print(' =>', goal, end='')


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '4': ['8']
}

start, goal, l = '5', '8', 2
print("\ndepth limited search:")
depth_limited_search(graph, start, goal, l)