# write your bubble sort algorithm below
 
import random

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        swapped = False
        print(f"iteration: {i}")
        for j in range(len(lst) - 1):
            print(f"comparing {lst[j]}, {lst[j+1]}")
            if lst[j] > lst[j+1]:
                # tmp = lst[j]
                # lst[j] = lst[i]
                # lst[i] = tmp
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
                if not swapped:
                    return lst
    return lst

# l = [random.randrange(100) for x in range(10)]
l = [1, 5, 2, 6, 7]
print(l)

print(bubble_sort(l))
