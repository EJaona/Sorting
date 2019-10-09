# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements # Creates an array with the length of both arrA & arrB 
    # TO-DO
    side_a = 0
    side_b = 0

    for i in range(elements):
        if side_a >= len(arrA):

            merged_arr[i] = arrB[side_b]
            side_b += 1

        elif side_b >= len(arrB):

            merged_arr[i] = arrA[side_a]
            side_a += 1

        elif arrA[side_a] < arrB[side_b]:

            merged_arr[i] = arrA[side_a]
            side_a += 1

        else:

            merged_arr[i] = arrB[side_b]
            side_b += 1
            
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        left_half = arr[ : len(arr) // 2 ]
        right_half = arr[ len(arr) // 2 : ]

        sorted_left = merge_sort(left_half)
        sorted_right = merge_sort(right_half)

        return merge( sorted_left, sorted_right )
    


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
