import time as time
import pickle

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

start = time.time()
visited = load_obj("visited")
timings = load_obj("timings")
equivalence = load_obj("equivalence")
diameter_count = load_obj("diameter_count")
print ("Time to load: " + str(time.time() - start))

print(visited)
print(timings)
print (diameter_count)
print(len(equivalence))
