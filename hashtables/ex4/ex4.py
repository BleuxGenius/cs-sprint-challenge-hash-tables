def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # creating hashtable dict
    cache = {}
    # array to return matches
    result =[]
   

    for index in a:
        # if the number is multiplied by -1 not in the dict
        if index * -1 not in cache:
            # the dict number is equal to the number that was multiplied by -1
            cache[index] = index
        else:
            # append the absolute value to the array , and return it 
            result.append(abs(index))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
