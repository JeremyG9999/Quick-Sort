def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        print(arr)
        return quick_sort(less) + [pivot] + quick_sort(greater)
my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_list = quick_sort(my_list)
print(sorted_list)
#pick a pivot point
#reorder the array so all elements less than the pivot point are before it
#and all elements greater than it come after it
#after the partition, the pivot is in its final spot
#then apply this to elements of smaller and larger values to the pivot