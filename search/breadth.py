
class Node:

    def __init__(self, v, r, c, nw=None, n=None, w=None):
        self.value = v
        self.row = r
        self.col = c
        self.nw = nw
        self.n = n
        self.w = w
        self.e = None
        self.s = None
        self.se = None

    def children(self):
        o = []
        if self.nw is not None:
            o.append(self.nw)
        if self.n is not None:
            o.append(self.n)
        if self.w is not None:
            o.append(self.w)
        if self.e is not None:
            o.append(self.e)
        if self.s is not None:
            o.append(self.s)
        if self.se is not None:
            o.append(self.se)
        
        return o


def generate_graph():
    root = None
    row_count = 30
    graph = [x[:] for x in [[None] * row_count] * row_count]
    for r in range(1, row_count + 1):
        v = 1
        row = r - 1
        for c in range(1, r + 1):
            col = c - 1

            nw = graph[row-1][col-1] if row > 0 and col > 0 else None
            n = graph[row-1][col] if row > 0 else None
            w = graph[row][col-1] if col > 0 else None

            current = Node(v, r, c, nw, n, w)
            graph[row][col] = current
            if root is None:
                root = current

            if nw is not None:
                nw.se = current
            if n is not None:
                n.s = current
            if w is not None:
                w.e = current

            v = int(v * (r - c) / c)

    return [root, graph]


def breadth_first_search(root, value):
    # Explore siblings before children.
    to_do = [[root]]
    while to_do:
        # Current
        path = to_do.pop()
        node = path[-1]

        # Did we reach the goal?
        score = sum([p.value for p in path])
        if score == value:
            return path
        if score > value:
            continue

        # Queue the next steps
        for move in node.children():
            if move not in path:
                to_do.append(path + [move])

    return None


def show_visual_answer(path, graph):
    for r in graph:
        for c in r:
            if c is not None:
                print(c.value, end="<" if c in path else " ")
        print()

def compute(N):
    [root, graph] = generate_graph()

    path = breadth_first_search(root, N)
    if True:
        show_visual_answer(path, graph)
    else:
        for p in path:
            print(p.row, p.col)

compute(8888)
