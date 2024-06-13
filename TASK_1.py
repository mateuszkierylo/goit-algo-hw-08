import heapq

def minimum_cost_to_connect_cables(cables):
    if not cables:
        return 0

    # Create a min-heap from the list of cables
    heapq.heapify(cables)
    
    total_cost = 0

    # While there is more than one cable in the heap
    while len(cables) > 1:
        # Extract the two smallest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # The cost to connect these two cables
        cost = first + second
        
        # Add the new cable back into the heap
        heapq.heappush(cables, cost)
        
        # Accumulate the total cost
        total_cost += cost

    return total_cost

# Example usage:
cables = [4, 3, 2, 6, 10, 15]
print(minimum_cost_to_connect_cables(cables)) 
