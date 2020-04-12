
class Node:

    def __init__(self, v):
        self.value = v

    def children(self):
        return []


def generate_graph():
    value = 1
    root = Node(value)
    return root


def breadth_first_search(root, goal):
    # Explore siblings before children.
    to_do = [[root]]
    while to_do:
        path = to_do.pop()
        node = path[-1]
        if node.value == goal:
            return path

        for move in node.children():
            if move not in path:
                to_do.append(path + [move])

    return None


root = generate_graph()
path = breadth_first_search(root, goal=100)
