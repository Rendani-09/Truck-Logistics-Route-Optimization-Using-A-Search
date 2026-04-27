import time
from A_star_search import path, visited_order, total_cost

# BUG FIX 1: 'time' was never imported — added import at the top
# BUG FIX 2: variable names inside the function were wrong:
#            visit_order  → visited_order
#            pat          → path
#            tot_cost     → total_cost
# BUG FIX 3: function call was misspelled: simulte_path → simulate_path
# BUG FIX 4: path/visited_order/total_cost were never imported from A_star_search

def simulate_path(path):
    print("\n Truck traveling...\n")
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\nDestination reached!")

    print("\nVisited Order:", visited_order)
    print("Optimal Path: ", path)
    print("Total Cost:   ", total_cost, "km")


simulate_path(path)