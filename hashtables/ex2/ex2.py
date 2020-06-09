#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    # for each ticket
    # the cache[source] = destination
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    print(cache.items())

    #initialize empty route, first entry is our ticket with source[None]
    route = []
    route.append(cache['NONE'])
   
#    iterate through the tickets, checking in time against cache
    for ticket in tickets:

        # the next source is the last location in our route 
        _next = route[-1]
        # gets the source's destination 
        route.append(cache[_next])
        # if the last location is NONE, we are finished 
        if route[-1] == "NONE":
            return route
    

    return route
# solution runs in linear time , will always han