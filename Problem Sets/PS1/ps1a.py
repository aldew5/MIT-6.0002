###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Alec Dewulf
# Collaborators: None
# Time: 3:00

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    file = open(filename, 'r')
    data = file.readlines()
    length = len(data)
    d = {}

    x = 0
    # split each line into a list of lenth two with name and weight
    while x < len(data):
        data[x] = data[x].split(',')
        x += 1

    x = 0
    # map name to weight getting rid of newline characters
    
    while x < length:
        dat = int(data[x][1].split()[0])
        d[data[x][0]] = dat

        x += 1

    return d
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #make a copy of the dictionary
    d = {}
    for k in cows:
        d[k] = cows[k]
    
    trips = []
    while len(d) != 0:
        trip, current_weight = [], 0
        # create one trip
        while current_weight < limit and len(d) > 0:
            # check for the lightest cow
            low_val, cow = None, None
            for c in d:
                if low_val == None or d[c] < low_val:
                    low_val = d[c]
                    cow = c
                    
            if current_weight + d[cow] <= limit:
                current_weight += d[cow]
                trip.append(cow)
                del d[cow]
            else:
                break
            
        # add the trip
        trips.append(trip)
        print(trip)
    return trips

cows = load_cows('ps1_cow_data.txt')
#print(greedy_cow_transport(cows,limit=10))


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    l, trips = [], []
    # create list of cows
    for k in cows:
        l.append(k)

    # still cows left to transport
    while len(l) > 0:
        # set variables
        highest_weight = 0
        t, l = [], l

        # loop through trips 
        for p in get_partitions(l):
            for trip in p:
                total_weight = 0
                for cow in trip:
                    total_weight += cows[cow]

                # more weight than the next best trip but less than the limit
                if total_weight > highest_weight and total_weight <= limit:
                    highest_weight = total_weight
                    # best trip with given cows
                    t = trip
                    
        # add the trip
        trips.append(t)

        # delete all trips using those cows
        x = 0
        while x < len(t):
            if t[x] in l:
                del l[l.index(t[x])]
            x += 1
        
    return trips

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    start = time.time()

    print("greedy trips")
    end = time.time()
    print("number of trips", len(greedy_cow_transport(cows, 10)))
    print("time", end-start)

    print("")
    start = time.time()

    print("brute force trips")
    print("number of trips", len(brute_force_cow_transport(cows, 10)))
    end = time.time()
    print("time", end-start)

compare_cow_transport_algorithms()

    
