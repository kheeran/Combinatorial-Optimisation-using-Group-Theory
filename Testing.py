import itertools
import pickle
import numpy as np

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 0)

def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list


orientations = [ '0' + str(p[0]) + str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5]) + str(-sum(p)%3) for p in itertools.product([0, 1, 2], repeat=6)]

permutations = ['0' + p for p in permute_string('1234567')]

visited = load_obj("visited")
missing_list = []

for permutation in permutations:
    for orientation in orientations:
        config = permutation + orientation
        if visited.get(config) == None:
            missing_list.append(config)

# first2pairs = {k: visited[k] for k in list(visited)[:2]}
# print (first2pairs)

print (missing_list[0:100])
print (len(missing_list))
print (len(visited))
print (len(missing_list) + len(visited))

save_obj(missing_list, "missing_list")

# print (test_list)
# print (len(permutations))
# print (len(orientations))
# print (len(permutations)*len(orientations))
# print (len(test_list))
