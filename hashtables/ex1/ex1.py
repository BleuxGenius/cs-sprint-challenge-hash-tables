def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # creating new dictionary
    cache = {}

    if length < 2:
        return None
        # find the weight
        # create the hashtable of weights and positions
    for i in range(length):
        cache[weights[i]] = i
        # hash table dict is  complete, finds the potential pairs of the weights
        # assessing each weight's target weight and checking the hashtable for it.

        # The enumerate object yields pairs containing a count 
        # (from start, which defaults to zero) and a value yielded by the iterable argument.
        #  enumerate is useful for obtaining an indexed list:
    for index, weight in enumerate(weights):
        targeted_weight = limit - weight # computing the target weight

        if targeted_weight in cache:
            target_index = cache[targeted_weight] # check if such weight exists
            
            return (index, target_index) if index > target_index else (target_index, index)
    return None
