import time as time
import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 0)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

start = time.time()
visited = load_obj("visited")
print ("Time to load: " + str(time.time() - start))

vertices = list(visited.keys())
edges = [(p,visited[p][0]) for p in vertices]

# Removing the initial node to itself
index = edges.index(('0123456700000000', ''))
edges.pop(index)


#Dynamic Approach Fail
# def find_move(node, visited, vertices, dict):
#     child = dict.get(node)
#     child_move = child[1]
#     parent = dict.get(visited[node])
#     parent_move = parent[1]
#     if list == None:
#         find_move(visited[node][0], visited, vertices, dict)
#     else:
#         dict.pop(node)


def find_move(node):
    if visited[node][2] == 0 :
        return ""
    return str(visited[node][1]) + find_move(visited[node][0])

n=0
start = time.time()
for v in vertices:
    # if visited[v][2] == 11:
        n += 1
        print (find_move(v))
        print (n)
print ("Time for search: " + str(time.time() - start))
