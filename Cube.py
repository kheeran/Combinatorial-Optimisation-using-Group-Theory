import numpy as np
import time as time
import pickle

def move_up(config):
    return config[0:4] + config[7] + config[4:7] + config[8:16]

def move_front(config):
    x1 = (int(config[10]) + 2) % 3
    x2 = (int(config[14]) + 1) % 3
    x6 = (int(config[15]) + 2) % 3
    x7 = (int(config[9]) + 1) % 3
    return config[0] + config[2] + config [6] + config[3:6] + config[7] + config [1] + config[8] + str(x1) + str(x2) + config[11:14] + str(x6) + str(x7)

def move_right(config):
    x2 = (int(config[11]) + 2) % 3
    x3 = (int(config[13]) + 1) % 3
    x5 = (int(config[14]) + 2) % 3
    x6 = (int(config[10]) + 1) % 3
    return config[0:2] + config[3] + config[5] + config[4] + config[6] + config[2] + config[7:10] + str(x2) + str(x3) + config[12] + str(x5) + str(x6) + config[15]

def record(order, visited, explored, equivalence):
    config = order.pop(0)
    current = visited.pop(config)
    count = current[2]
    moves = {'U':move_up(config), 'F':move_front(config), 'R':move_right(config)}
    for move in moves:
        if visited.get(moves[move]) == None and explored.get(moves[move]) == None:
            visited[moves[move]] = (config, move, count+1)
            order.append(moves[move])
        else:
            equivalence.append((moves[move],(config, move, count+1)))
    explored[config] = current
    return count


def init_dict():
    return {'0123456700000000' : ("", "", 0)}, ['0123456700000000']

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 0)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

explored = {}
visited, order = init_dict()
equivalence = []
timings = []

n=0
start = time.time()

while len(order) > 0:
# while n < 100000:
    count = record(order, visited, explored, equivalence)

    if n % 367416 == 0:
        print (str((n//367416)*10) + "% complete")
        runtime = int(time.time() - start)
        timings.append(runtime)
        print ("Runtime: " + str(runtime) + " sec(s)" )
    n += 1

runtime = time.time() - start
timings.append(runtime)
print ("Diameter: " + str(count))
print ("Number of Configs: " + str(n))
print ("Total explored: " + str(len(explored)))
print ("Remaining no. of Configs: " + str(3674160 - n))
# print (equivalence)
print ("Timings:")
print (timings)
print ("Runtime: " + str(runtime))

save_obj(equivalence, "equivalence")
save_obj(timings, "timings")
save_obj(n, "number_of_configs")
save_obj(explored, "explored")
save_obj(visited, "visited")
