import numpy as np
import time as time
import pickle

def _U(config):
    return config[0:4] + config[7] + config[4:7] + config[8:12] + config[15] + config[12:15]

def _D(config):
    return config[3] + config [0:3] + config[4:8] + config[11] + config[8:11] + config[12:16]

def _F(config):
    x1 = (int(config[10]) + 2) % 3
    x2 = (int(config[14]) + 1) % 3
    x6 = (int(config[15]) + 2) % 3
    x7 = (int(config[9]) + 1) % 3
    return config[0] + config[2] + config [6] + config[3:6] + config[7] + config [1] + config[8] + str(x1) + str(x2) + config[11:14] + str(x6) + str(x7)

def _B(config):
    x0 = (int(config[12]) + 1) % 3
    x3 = (int(config[8]) + 2) % 3
    x4 = (int(config[13]) + 2) % 3
    x5 = (int(config[11]) + 1) % 3
    return config[4] + config [1:3] + config[0] + config[5] + config[3] + config[6:8] + str(x0) + config[9:11] + str(x3) + str(x4) + str(x5) + config[14:16]

def _R(config):
    x2 = (int(config[11]) + 2) % 3
    x3 = (int(config[13]) + 1) % 3
    x5 = (int(config[14]) + 2) % 3
    x6 = (int(config[10]) + 1) % 3
    return config[0:2] + config[3] + config[5] + config[4] + config[6] + config[2] + config[7:10] + str(x2) + str(x3) + config[12] + str(x5) + str(x6) + config[15]

def _L(config):
    x0 = (int(config[9]) + 2) % 3
    x1 = (int(config[15]) + 1) % 3
    x4 = (int(config[8]) + 1) % 3
    x7 = (int(config[12]) + 2) % 3
    return config[1] + config[7] + config[2:4] + config[0] + config[5:7] + config[4] + str(x0) + str(x1) + config[10:12] + str(x4) + config[13:15] + str(x7)

def _Rx(config):
    return _R(_L(_L(_L(config))))

def _Ry(config):
    return _U(_D(_D(_D(config))))

def _Rz(config):
    return _F(_B(_B(_B(config))))

def neighbourhood_basic_moves(config):
    return {'U1' : _U(config), 'U2': _U(_U(config)), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config)))}

def neighbourhood_gen_2_moves(config):
    return {'U1' : _U(config), 'U2': _U(_U(config)), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config)))}

def neighbourhood_symmetry_moves(config):
    return {'Rx1' : _Rx(config), 'Ry1' : _Ry(config), 'Rz1' : _Rz(config)}

def record(unexplored, visited, equivalence, diameter_count):
    node = unexplored.pop(0)
    diameter = visited[node][2]
    diameter_count[int(diameter)] = diameter_count[int(diameter)] + 1
    neighbourhood = neighbourhood_symmetry_moves(node) # neighbourhood_basic_moves(node), neighbourhood_gen_2_moves(node), neighbourhood_symmetry_moves(node)
    for edge in neighbourhood:
        if visited.get(neighbourhood[edge]) == None:
            visited[neighbourhood[edge]] = (node, edge, diameter+1)
            unexplored.append(neighbourhood[edge])
        else:
            equivalence.append((neighbourhood[edge],(node, edge, diameter+1)))
    return diameter, diameter_count


def init_dict():
    return {'0123456700000000' : ("", "", 0)}, ['0123456700000000']

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 0)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# MAIN RUN

# explored = {}
visited, unexplored = init_dict()
# unexplored = ['0123456700000000', '0123745600000000', '0263457102100021', '0123745600000000', '0263457102100021']
equivalence = []
timings = []
diameter_count = np.zeros(20,  np.int32)

n=0
start = time.time()
# goal = 3674160 # G=<U,F,R>
# goal = 29160 # G=<U,F>
goal = 24 # G = Symmetry
checkpoint = goal/10

# while n < goal:
while len(unexplored) > 0:
    diameter, diameter_count = record(unexplored, visited, equivalence, diameter_count)

    if n % checkpoint == 0:
        print (str((n//checkpoint)*10) + "% complete")
        runtime = round(time.time() - start,2)
        timings.append(runtime)
        print ("Runtime: " + str(runtime) + " sec(s)" )
    n += 1

runtime = time.time() - start
timings.append(runtime)
print ("Diameter: " + str(diameter))
print (diameter_count)
print (sum(diameter_count))
print ("Number of Configs: " + str(n))
print ("Remaining no. of Configs: " + str(goal - n))
print ("Nodes visited: " + str(len(visited)))
print ("Total explored: " + str(len(visited) - len(unexplored)))
print ("Number of non-unique equivalence relations: " + str(len(equivalence)))
print ("Timings:")
print (timings)
print ("Runtime: " + str(runtime))

# save_obj(explored, "explored")
save_obj(diameter_count, "diameter_count")
save_obj(timings, "timings")
save_obj(equivalence, "equivalence")
save_obj(visited, "visited")




# TESTS
#
# config = "0124763501210200"
# if _U(config) == "0124576301210020":
#     print ("UP Correct")
# else:
#     print ("UP WRONG !!!!")
#
# config = "0123456700000000"
# if _F(config) == "0263457102100021":
#     print("FRONT Correct")
# else:
#     print("FRONT WRONG !!!!")
#
# config = "0263457102100021"
# if _R(config) == "0235476102210121":
#     print("RIGHT Correct")
# else:
#     print("RIGHT WRONG !!!!")
#
# config = "0263457102100021"
# if _D(config) == "3026457100210021":
#     print ("DOWN Correct")
# else:
#     print ("DOWN WRONG !!!!")
#
# config = "1360457200210021"
# if _B(config) == "4361507210222221":
#     print ("BACK Correct")
# else:
#     print ("BACK WRONG !!!!")
#
# config = "4361507210222221"
# if _L(config) == "3261407522222221":
#     print ("LEFT Correct")
# else:
#     print ("LEFT WRONG !!!!")
#     print (_L(config))
