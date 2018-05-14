#   Ryan Vinyard
#   Python 3.6.5
#   The Tech Academy, python sorting drill

# While researching sorting methods I came across quick sort. It looked
# interesting to me. It essentially takes an element from a list and
# makes it a "pivot." Everything higher than the pivot goes into another
# list that goes above the pivot, and everything lower goes in a list
# lower than it. These two lists are then sorted, then joined by the
# pivot. I spent some time learning how this worked. I attempted to
# reproduce this below. The main difference between this algorithm and
# sample ones is that most sample code I found had the line:
# pivot = arr[0]
# This makes the pivot the first entry in the list. This seems inefficient
# to me, so I had it simply start near the middle by having it divide the
# length of the list by 2. This seems to work, and  I assume it would be
# a little more efficient, though I'm not sure.

def custom_sort(alist):
# First, define the lower and upper lists, as well as one for the pivot
    lowerlist = []
    higherlist = []
    pivotlist = []

# Now add a statement that if a list has nothing or just one number in it
# It must be sorted

    if len(alist) <= 1:
        return alist
    
# The pivot starts about halfway through the list at index len/2

    else:        
        pivotnum = int(len(alist)/2)
        if pivotnum < 0:
            pivotnum = 0
        pivot = alist[pivotnum]
        
# Go through each number and add them to lowerlist or higherlist
# If any number is the same as the pivot it goes into the pivotlist

        for i in alist:
            if i < pivot:
                lowerlist.append(i)
            elif i > pivot:
                higherlist.append(i)
            else:
                pivotlist.append(i)
                
# This process repeats until the lists are sorted

    lowerlist = custom_sort(lowerlist)
    higherlist = custom_sort(higherlist)
    return lowerlist + pivotlist + higherlist
    
 
alist = [67, 45, 2, 13, 1, 998]
alist = custom_sort(alist)
print (alist)

alist = [89, 23, 33, 45, 10, 12, 45, 45, 45]
alist = custom_sort(alist)
print (alist)

