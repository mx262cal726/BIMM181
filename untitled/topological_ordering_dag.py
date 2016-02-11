def topological_ordering(graph):
    '''Returns a topological ordering for the given graph.'''
    # Initialize and covert variables appropriately.
    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    # Get the topological ordering.
    while len(candidates) != 0:
        # Add the next candidate to the ordering.
        ordering.append(candidates[0])

        # Remove outgoing edges and store outgoing nodes.
        temp_nodes = []
        for edge in filter(lambda e: e[0] == candidates[0], graph):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        # Add outgoing nodes to candidates list if it has no other incoming edges.
        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        # Remove the current candidate.
        candidates = candidates[1:]

    return ordering



def toposort2(data):
    """Dependencies are expressed as a dictionary whose keys are items
and whose values are a set of dependent items. Output is a list of
sets in topological order. The first set consists of items with no
dependences, each subsequent set consists of items that depend upon
items in the preceeding sets.

>>> print '\\n'.join(repr(sorted(x)) for x in toposort2({
...     2: set([11]),
...     9: set([11,8]),
...     10: set([11,3]),
...     11: set([7,5]),
...     8: set([7,3]),
...     }) )
[3, 5, 7]
[8, 11]
[2, 9, 10]

"""

    from functools import reduce

    # Ignore self dependencies.
    for k, v in data.items():
        v.discard(k)
    # Find all items that don't depend on anything.
    extra_items_in_deps = reduce(set.union, data.itervalues()) - set(data.iterkeys())
    # Add empty dependences where needed
    data.update({item:set() for item in extra_items_in_deps})
    while True:
        ordered = set(item for item, dep in data.iteritems() if not dep)
        if not ordered:
            break
        yield ordered
        data = {item: (dep - ordered)
                for item, dep in data.iteritems()
                    if item not in ordered}
    assert not data, "Cyclic dependencies exist among these items:\n%s" % '\n'.join(repr(x) for x in data.iteritems())
from collections import defaultdict
from itertools import takewhile, count

def sort_topologically_stackless(graph):
    levels_by_name = {}
    names_by_level = defaultdict(set)

    def add_level_to_name(name, level):
        levels_by_name[name] = level
        names_by_level[level].add(name)


    def walk_depth_first(name):
        stack = [name]
        while(stack):
            name = stack.pop()
            if name in levels_by_name:
                continue

            if name not in graph or not graph[name]:
                level = 0
                add_level_to_name(name, level)
                continue

            children = graph[name]

            children_not_calculated = [child for child in children if child not in levels_by_name]
            if children_not_calculated:
                stack.append(name)
                stack.extend(children_not_calculated)
                continue

            level = 1 + max(levels_by_name[lname] for lname in children)
            add_level_to_name(name, level)

    for name in graph:
        walk_depth_first(name)



    return list(takewhile(lambda x: x is not None, (names_by_level.get(i, None) for i in count())))


graph = {
        1: [2, 3],
        2: [4, 5, 6],
        3: [4,6],
        4: [5,6],
        5: [6],
        6: []
    }

print(sort_topologically_stackless(graph))

if __name__ == '__main__':
    text = open("input.txt")
    lines = text.read().split("\n")
    edges, weights = {}, {}


    size = 0
    for i in range(0, len(lines)):
        line = lines[i].replace(' ',"").split('->')
        for j in range(0, len(line[1])):
            size += 1
    print size
    matrix = [0 for _ in range(size)]
    for i in range(0, len(lines)):
        line = lines[i].replace(' ',"").split('->')
        print "line",i,line
        index = int(line[0].strip(" "))
        if len(lines[i]) < 1:
            break
        edge = line[1].strip(" ").split(',')

        edges = list()
        for j in range(0, len(edge)):
            edges.append(edge[j])
        matrix[index] = edges
    print topological_ordering(matrix)


