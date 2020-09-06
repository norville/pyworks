# init unsorted list
l = [5, 8, 1, 3, 2]

# init sorting status indicator: list not sorted
is_sorted = False

while not is_sorted:
    
    # list sorted (exit on next iteration)
    is_sorted = True
    
    # iterate list's items
    for i in range(len(l) - 1):
        
        # if current item is gt the next
        if l[i] > l[i + 1]:
            
            # sort current item and the next
            l[i], l[i + 1] = l[i + 1], l[i]
            
            # list not sorted
            is_sorted = False

print(l)
