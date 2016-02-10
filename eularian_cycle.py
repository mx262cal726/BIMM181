__author__ = 'kyle'



def find_eulerian_tour(graph):

    def freqencies():
        my_list = [x for (x, y) in graph]
        result = [0 for i in range(max(my_list) + 1)]
        for i in my_list:
            result[i] += 1
        return result

    def find_node(tour):
        for i in tour:
            if freq[i] != 0:
                return i
        return -1

    def helper(tour, next):
        find_path(tour, next)
        u = find_node(tour)
        while sum(freq) != 0:
            sub = find_path([], u)
            tour = tour[:tour.index(u)] + sub + tour[tour.index(u) + 1:]
            u = find_node(tour)
        return tour

    def find_path(tour, next):
        for (x, y) in graph:
            if x == next:
                current = graph.pop(graph.index((x,y)))
                graph.pop(graph.index((current[1], current[0])))
                tour.append(current[0])
                freq[current[0]] -= 1
                freq[current[1]] -= 1
                return find_path(tour, current[1])
        tour.append(next)
        return tour

    graph += [(y, x) for (x, y) in graph]
    freq = freqencies()
    return helper([], graph[0][0])

find_eulerian_tour("graphs.txt")

