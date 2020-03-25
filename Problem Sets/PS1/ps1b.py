###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Alec Dewulf
# Collaborators: None
# Time: 4: 00
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight

    I used the memo to add the amount of eggs required for an already computed sum to the new level.
    I thought of this problem as a tree with the roots being the egg weights and the following levels being their possible sums.
    The first time a sum is found that is equal to the target weight that will be returned
    """
    # first call
    if len(memo) == 0:
        #add inital weights - create first row
        for egg in egg_weights:
            memo[egg] = 1
            
    # create a list of the egg_weights
    eggs = []
    for e in egg_weights:
        eggs.append(e)

    # new dictionary for level n where n in number of eggs
    level = {}
    for key in memo:
        for e in eggs:
            # new sum that is under target - builds a new level
            if (key + e) not in memo.keys() and (key + e) <= target_weight:
                # add it to the dictionary
                level[key + e] = memo[key] + 1

                # found the correct combo
                if key + e == target_weight:
                    # return the number of eggs
                    return level[key + e]

    # didn't find solution
    if len(level) == 0:
        # no possible solutions - all nums greater than target
        return None
    else:
        for k in level:
            # add the new level to the memo
            memo[k] = level[k]

    # call the function again with updated memo so a new level can be added
    return dp_make_weight(egg_weights, target_weight, memo)    
        


    

 #EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
