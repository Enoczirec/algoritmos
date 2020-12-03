# Algoritmos Kruskal para AGM
# Brandon Alain Cruz Ruiz
# 198573
#
# Mini proyecto 2

res = dict()
result = []
final_result = {}
  
def make_set(v):
    res[v] = {
      'parent': v,
      'size': 1,
      'childs': []
    }

def find_set(v):
    return res[v]['parent']

def union(u, v):
    parent_u, parent_v = get_sets(u, v)
    if parent_u != parent_v:
        if res[parent_u]['size'] > res[parent_v]['size']:
            temp = [parent_u]
            res[parent_v]['size'] += res[parent_u]['size']
            res[parent_u]['size'] = res[parent_v]['size']
            res[parent_v]['childs'] = temp + res[parent_u]['childs']
            for vertex in res[parent_v]['childs']:
                res[vertex]['parent'] = parent_v
        else:
            temp = [parent_v]
            res[parent_u]['size'] += res[parent_v]['size']
            res[parent_v]['size'] = res[parent_u]['size']
            res[parent_u]['childs'] = temp + res[parent_v]['childs']
            for vertex in res[parent_u]['childs']:
                res[vertex]['parent'] = parent_u


def get_sets(u, v):
    return find_set(u), find_set(v)

def kruskal(graph):
    print_adjacencies(graph, 'GRAFO')
    for key in graph['vertices']:
        make_set(key)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, u, v = edge
        set_u, set_v = get_sets(u, v)
        if set_u != set_v:
            union(u, v)
            result.append(edge)
    final_result = {
      'vertices': graph['vertices'],
      'edges': result
    }
    print_adjacencies(final_result)
    return final_result

def print_adjacencies(graph, title = 'AGM'):
    n = len(graph['vertices'])
    adjacencies = [([0]*n) for i in range(n + 1)]
    vertices = graph['vertices']
    for edge in graph['edges']:
        w, u, v = edge
        u_index = vertices.index(u)
        v_index = vertices.index(v)
        adjacencies[u_index][v_index] = w
        adjacencies[v_index][u_index] = w
    print(f'\nMATRIZ DE ADYACENCIAS DEL {title}\n')
    print('   '+'  '.join(vertices))
    for i in range(n):
        print(f'{vertices[i]} {adjacencies[i]}')


def main():
    filename = input("Ingresa el nombre del archivo: ")
    file = open(filename, 'r')
    lines = file.readlines()
    vertex = set()
    edges = []
    for x in lines:
        edge = x.strip('\n')
        w, u, v = edge.split(',')
        edges.append([int(w),u,v])
        vertex = vertex.union(u)
        vertex = vertex.union(v)
    file.close()
    graph = {
      "edges": edges,
      "vertices": list(vertex)
    }
    kruskal(graph)

if __name__ == "__main__":
    main()

