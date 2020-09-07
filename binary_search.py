# init sorted list
l = [2, 3, 5, 8, 11, 12, 18]

# set target value
target = 11

# define a sublist of 'l' by setting begin and end indexes
# init sublist equal to 'l'
slice_bgn = 0
slice_end = len(l) - 1

# set search status
found = False

# keep searching while sublist has items and target is not found
while slice_bgn <= slice_end and not found:
    
    # set sublist's midpoint
    slice_hlf = (slice_bgn + slice_end) // 2
    
    # if target is at midpoint
    if l[slice_hlf] == target:
        # stop searching
        found = True
    else:
        # if target is smaller than midpoint's value
        if target < l[slice_hlf]:
            # update sublist: ends before midpoint
            slice_end = slice_hlf - 1
        else:
            # target is greater than midpoint's value
            # update sublist: begins after midpoint
            slice_bgn = slice_hlf + 1

print(found)
print(slice_hlf)
