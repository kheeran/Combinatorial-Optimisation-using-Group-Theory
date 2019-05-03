import pickle
import time as time

def load_obj(name):
    user_input = input("Do you want to load from\n" + "A)2_generator\n" + "B)symmetry\n" + "C)brute_force\n" + "[A/B/C]?\n")
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
            return "./brute_force/"
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

equivalence = load_obj("equivalence")

len(equivalence)
