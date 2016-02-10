__author__ = 'kyle'


def topological_ordering(graph):

    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})
    while len(candidates) != 0:

        ordering.append(candidates[0])
        temp_nodes = []
        for edge in filter(lambda e: e[0] == candidates[0], graph):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        candidates = candidates[1:]
    return ordering


def longest_path_in_dag(graph, edges, source, sink):

    top_order = topological_ordering(graph.keys())
    top_order = top_order[top_order.index(source)+1:top_order.index(sink)+1]
    graph_out = {node:-100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
    graph_out[source] = 0
    backtrack = {node:None for node in top_order}

    for node in top_order:
        try:
            graph_out[node], backtrack[node] = max(map(lambda e: [graph_out[e[0]] + graph[e], e[0]], filter(lambda e: e[1] == node, graph.keys())), key=lambda p:p[0])
        except ValueError:
            pass

    path = [sink]
    while path[0] != source:
        path = [backtrack[path[0]]] + path
    return graph_out[sink], path


def setup_longest_path(text):
    in_file = open(text)
    lines = in_file.read().split("\n")
    source = int(lines[0])
    sink = int(lines[1])
    edge_set = {}
    edge_container = {}
    for pairs in [lines[line].strip().split('->') for line in range(2, len(lines))]:
        node = int(pairs[0])
        edges = int(pairs[1].split(':')[0])
        edge_weight = int(pairs[1].split(':')[1])
        if node in edge_set:
            edge_set[node].append(edges)
        else:
            edge_set[node] = [edges]
        edge_container[node, edges] = edge_weight

    length, path = longest_path_in_dag(edge_container, edge_set, source, sink)
    path = '->'.join(map(str, path))
    output = '\n'.join([str(length), path])
    return output


print setup_longest_path("input")