def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

# empty array
    result = []
    #  creating hashtable dictionary
    cache = {}

# the array in the arrays 
    for array in arrays:
        # loop to find the specific array number in the array  
        for array_Num in array:
            # if the array number is not in the hash table
            if array_Num not in cache:
                #  the array number in the hash table is equivalent to 1 
                cache[array_Num] = 1 
            else: 
                # the array number in the hash table addes 1 to the arrayed number 
                cache[array_Num] += 1  

        # Returns a list containing the tuple for each key value pair 
        for key,value in cache.items():
            if value > 1:
                result.append(key)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
