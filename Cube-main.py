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

def neighbourhoods(config, select):

    if select == "basic_moves_all":
        return {'U1' : _U(config), 'U2': _U(_U(config)), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config))), 'D1' : _D(config), 'D2': _D(_D(config)), 'D3': _D(_D(_D(config))), 'B1':_B(config), 'B2' : _B(_B(config)), 'B3' : _B(_B(_B(config))), 'L1' : _L(config), 'L2' : _L(_L(config)), 'L3' : _L(_L(_L(config))) }

    if select == "basic_moves" or select == "G0":
        return {'U1' : _U(config), 'U2': _U(_U(config)), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config)))}

    if select == "basic_moves_quarter":
        return {'U1' : _U(config), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R3' : _R(_R(_R(config)))}

    if select == "basic_moves_relations":
        return {'U' : _U(config), 'F':_F(config), 'R' : _R(config)}

    if select == "G1":
        return {'U2': _U(_U(config)), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config)))}

    if select == "G2":
        return {'U2': _U(_U(config)),'F2' : _F(_F(config)),'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config)))}

    if select == "G3":
        return {'U2': _U(_U(config)),'F2' : _F(_F(config)),'R2' : _R(_R(config))}

    if select == "gen_2_moves":
        return {'U1' : _U(config), 'U2': _U(_U(config)), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config)))}

    if select == "gen_2_moves_relations":
       return {'U' : _U(config), 'F':_F(config)}

    if select == "symmetry_moves":
        return {'X1' : _Rx(config),'X2' : _Rx(_Rx(config)), 'X3' : _Rx(_Rx(_Rx(config))), 'Y1' : _Ry(config), 'Y2' : _Ry(_Ry(config)), 'Y3' : _Ry(_Ry(_Ry(config))), 'Z1' : _Rz(config), 'Z2' : _Rz(_Rz(config)), 'Z3' : _Rz(_Rz(_Rz(config)))}

## INCLUDING ALL 6 BASIC MOVES WHICH NEVER RUNS!
#
# def neighbourhoods(config, select):
#
#     if select == "G0":
#         return {'U1' : _U(config), 'U2': _U(_U(config)), 'U3': _U(_U(_U(config))), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config))), 'D1' : _D(config), 'D2': _D(_D(config)), 'D3': _D(_D(_D(config))), 'B1':_B(config), 'B2' : _B(_B(config)), 'B3' : _B(_B(_B(config))), 'L1' : _L(config), 'L2' : _L(_L(config)), 'L3' : _L(_L(_L(config))) }
#
#     if select == "G1":
#         return {'U2': _U(_U(config)), 'F1':_F(config), 'F2' : _F(_F(config)), 'F3' : _F(_F(_F(config))), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config))), 'D2': _D(_D(config)), 'B1':_B(config), 'B2' : _B(_B(config)), 'B3' : _B(_B(_B(config))), 'L1' : _L(config), 'L2' : _L(_L(config)), 'L3' : _L(_L(_L(config))) }
#
#     if select == "G2":
#         return {'U2': _U(_U(config)), 'F2' : _F(_F(config)), 'R1' : _R(config), 'R2' : _R(_R(config)), 'R3' : _R(_R(_R(config))), 'D2': _D(_D(config)), 'B2' : _B(_B(config)), 'L1' : _L(config), 'L2' : _L(_L(config)), 'L3' : _L(_L(_L(config))) }
#
#     if select == "G3":
#         return {'U2': _U(_U(config)), 'F2' : _F(_F(config)), 'R2' : _R(_R(config)), 'D2': _D(_D(config)), 'B2' : _B(_B(config)), 'L2' : _L(_L(config))}


def init_dict(select):
    if select == "all":
        return {'0123456700000000': ('', '', 0), '4035762121211212': ('', '', 0), '7456123000000000': ('', '', 0), '1762035421211212': ('', '', 0), '1230745600000000': ('', '', 0), '2301674500000000': ('', '', 0), '3012567400000000': ('', '', 0), '3265047112122121': ('', '', 0), '5674301200000000': ('', '', 0), '4710532612122121': ('', '', 0), '0354176212122121': ('', '', 0), '3540217621211212': ('', '', 0), '5403621712122121': ('', '', 0), '5326471021211212': ('', '', 0), '6217540321211212': ('', '', 0), '7104653221211212': ('', '', 0), '4567012300000000': ('', '', 0), '6745230100000000': ('', '', 0), '6532710412122121': ('', '', 0), '1047265312122121': ('', '', 0), '7621403512122121': ('', '', 0), '2176354012122121': ('', '', 0), '2653104721211212': ('', '', 0), '0471326521211212': ('', '', 0)}, ['0123456700000000', '4035762121211212', '7456123000000000', '1762035421211212', '1230745600000000', '2301674500000000', '3012567400000000', '3265047112122121', '5674301200000000', '4710532612122121', '0354176212122121', '3540217621211212', '5403621712122121', '5326471021211212', '6217540321211212', '7104653221211212', '4567012300000000', '6745230100000000', '6532710412122121', '1047265312122121', '7621403512122121', '2176354012122121', '2653104721211212', '0471326521211212']
    else:
        return {'0123456700000000': ('', '', 0)}, ['0123456700000000']

def init_dict_visited(visited):
    unexplored = list(visited.keys())
    new_visited = {}
    for k in unexplored:
        new_visited[k] = ('', '', 0)
    return new_visited, unexplored


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 0)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

# SIMPLIFYING THE DEFINING RELATIONS ALGO

def equivalence_relations(moves_set, visited, equivalence, neighbourhood, node, edge):

    if "relations" in moves_set:
        jump = 1
    else:
        jump = 2

    m_1 = visited[neighbourhood[edge]][1]
    m_2 = visited[node][1] + edge

    n = 0
    for j in range(0,len(m_1), jump):
        if m_1[j:j+jump] == m_2[j:j+jump]:
            n += jump
        else:
            break
    if equivalence.get(m_1[n:]) == None:
        equivalence[m_1[n:]] = [m_2[n:]]
    else:
        equivalence[m_1[n:]].append(m_2[n:])


# MAIN SEARCH ALGO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def record(unexplored, visited, equivalence, diameter_count, loop_iter, select):
    node = unexplored.pop(0)
    diameter = visited[node][2]
    diameter_count[int(diameter)] = diameter_count[int(diameter)] + 1
    neighbourhood = neighbourhoods(node, select)
    for edge in neighbourhood:
        loop_iter += 1
        if visited.get(neighbourhood[edge]) == None:
            visited[neighbourhood[edge]] = (node, visited[node][1] + edge, diameter+1)
            unexplored.append(neighbourhood[edge])
        else:
            equivalence_relations(moves_set, visited, equivalence, neighbourhood, node, edge)

    return diameter, diameter_count, loop_iter

# FULL SEARCH EXEC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def full_search(select, visited, unexplored, equivalence, timings, diameter_count, loop_iter, n, start):

    checkpoint = goal/10

    # while n < goal:
    while len(unexplored) > 0:
        diameter, diameter_count, loop_iter = record(unexplored, visited, equivalence, diameter_count, loop_iter, select)

        # PROGRESS BAR

        if n % checkpoint == 0:
            # print ("Equivalence not saving")
            print (str((n//checkpoint)*10) + "% complete")
            runtime = round(time.time() - start,2)
            timings.append(runtime)
            print ("Runtime: " + str(runtime) + " sec(s)\n" )
        n += 1


    runtime = time.time() - start
    timings.append(runtime)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Diameter: " + str(diameter))
    print (diameter_count)
    print (sum(diameter_count))
    print ("Number of Configs: " + str(n))
    print ("Remaining no. of Configs: " + str(goal - n))
    print ("Nodes visited: " + str(len(visited)))
    print ("Total explored: " + str(len(visited) - len(unexplored)))
    print ("Number of shortest moves with equivalence relations: " + str(len(equivalence)))
    print ("Timings:")
    print (timings)
    print ("Runtime: " + str(runtime))
    print ("No. of main loop iteration ratio check (number of basic moves): " + str(loop_iter/(n)))
    # print ("Unexplored nodes: " + str(len(unexplored)))
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    return timings, diameter_count, n


# MAIN THISTLEWAITE ALGO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def thistlewaite_algo(goal, save, root):
    visited, unexplored = init_dict(root)
    equivalence = {}
    timings = []
    diameter_count = np.zeros(50,  np.int32)
    loop_iter = 0
    n=0
    start = time.time()

    timings, diameter_count, n = full_search("G3", visited, unexplored, equivalence, timings, diameter_count, loop_iter, n, start)

    # visited_G3 = visited
    # diameter_count_G3 = diameter_count
    visited, unexplored = init_dict_visited(visited)
    diameter_count = np.zeros(52,  np.int32)
    loop_iter = 0
    n=0

    timings, diameter_count, n = full_search("G2", visited, unexplored, equivalence, timings, diameter_count, loop_iter, n, start)

    # visited_G2 = visited
    # diameter_count_G2 = diameter_count
    visited, unexplored = init_dict_visited(visited)
    diameter_count = np.zeros(52,  np.int32)
    loop_iter = 0
    n=0

    timings, diameter_count, n = full_search("G1", visited, unexplored, equivalence, timings, diameter_count, loop_iter, n, start)

    if sum(diameter_count) < goal:
        # visited_G1 = visited
        # diameter_count_G1 = diameter_count
        visited, unexplored = init_dict_visited(visited)
        diameter_count = np.zeros(52,  np.int32)
        loop_iter = 0
        n=0
        
        timings, diameter_count, n = full_search("G0", visited, unexplored, equivalence, timings, diameter_count, loop_iter, n, start)

    # Saving Objects
    if save:
        save_obj(visited, "visited")
        # save_obj(diameter_count, "diameter_count")
        save_obj(timings, "timings")

    print ("COMPLETE!")

# MAIN BRUTE FORCE ALGO with EQUIVALENCE RELATIONS

def brute_force_relations(goal, save, root, moves_set):

    visited, unexplored = init_dict(root)
    equivalence = {}
    timings = []
    diameter_count = np.zeros(50,  np.int32)
    loop_iter = 0
    n=0
    start = time.time()

    timings, diameter_count, n = full_search(moves_set, visited, unexplored, equivalence, timings, diameter_count, loop_iter, n, start)

    keys = list(equivalence.keys())
    unique_relations = 0
    for k in keys:
        equivalence[k] = set(equivalence[k])
        unique_relations += len(equivalence[k])
        # print(k + "~" + str(equivalence[k]))

    print ("|R| = " + str(unique_relations))

    # Saving Objects
    if save:
        save_obj(visited, "visited")
        save_obj(equivalence, "equivalence")
        save_obj(diameter_count, "diameter_count")
        save_obj(timings, "timings")

    print ("COMPLETE!")


# MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# G=<U,D,F,B,R,L>
# moves_set = "basic_moves_all"
# goal = 3674160*24
# root = "all"

# G=<U,F,R>
# moves_set = "basic_moves_relations"
# goal = 3674160
# root = ""

# G=<U,F,R>
moves_set = "basic_moves"
goal = 3674160
root = ""


# moves_set = "basic_moves"
# goal = 88179840
# root = "all"

# G=<U,F,R>
# moves_set = "basic_moves_quarter"
# goal = 3674160
# root = ""

# # G = <U,F>
# moves_set = "gen_2_moves_relations"
# goal = 29160
# root = ""

# # G=Symmetry
# moves_set = "symmetry_moves"
# goal = 24
# root = ""

# Save objects for re-use?
save = False

thistlewaite_algo(goal, save, root)

# brute_force_relations(goal, save, root, moves_set)






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
