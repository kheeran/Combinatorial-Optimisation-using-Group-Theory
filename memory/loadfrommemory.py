import pickle
import time as time

def load_obj(name):
    user_input = input("Do you want to load from\n" + "A)2_generator\n" + "B)symmetry\n" + "C)brute_force_relations\n" + "[A/B/C]?\n")
    folder = parseinput(user_input)
    with open(folder + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def parseinput(user_input):
    if user_input == "A":
        return "./2_generator/"
    elif user_input == "B":
        return "./symmetry/"
    elif user_input == "C":
        user_confirmation = input("Are you sure? [Y/N]?\n")
        if user_confirmation == "Y":
            return "./brute_force_relations/"
        else:
            raise Exception("You weren't sure!")
    else:
        raise Exception("User input invalid. The input was: " + user_input)


# MAIN FUNCTIONS
def find_initial_nodes():
    visited = load_obj("visited")

    print ("FINDING THE INITIAL NODES--\n")

    init_dict = {}
    init_array = []
    for k in visited.keys():
        init_dict[k] = ("", "", 0)
        init_array.append(k)


    print ("Initial dictionary:")
    print (init_dict)
    print()

    print ("Initial array:")
    print (init_array)

# MAIN
start = time.time()
equivalence = load_obj("visited")
print ("Time to load: " + str(time.time() - start))


print (len(equivalence))
keys = list(equivalence.keys())


for k in keys:
    if "01234567" in k:
        orient = k[8:16]
        count = 0
        for i in range (0,8):
            if orient[i] == "0":
                count += 1
        if count == 6:
            print (str(k) + "-> " + str(equivalence[k]))




# for k in keys:
#     if k = "0213456700000000":
#         print (equivalence[k])
#     if k == "0321456700000000":
#         print (equivalence[k])
#     if k == "0423156700000000":
#         print (equivalence[k])
#     if k == "0523416700000000":
#         print (equivalence[k])
#     if k == "0623451700000000":
#         print (equivalence[k])
#     if k == "0723456100000000":
#         print (equivalence[k])

# ('0612435700210210', 'RRRUUUFRFUUFURRURFR', 19)
# ('0362415700210210', 'RUUUFRFUUFURRURFRRR', 19)
# ('0562431700210210', 'RRFFRUUURURRFFRFR', 17)
# ('0723451602100021', 'RRRUFRRFFURFFFRFF', 17)
# ('0173452602100021', 'RRRFURUURFRRFUF', 15)
# ('0743152602100021', 'RURURRFFURRURFFFRFF', 19)
