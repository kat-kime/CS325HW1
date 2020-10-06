import random
import time


def merge_sort(int_array):
    """
    Sorts numbers using a merge sort algorithm
    :param int_array: integer array
    :return: numbers sorted in decreasing order
    """
    merge_sort_helper(int_array)
    return int_array


def merge_sort_helper(array):
    # if greater than 1, split
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            # sort left and right
            merge_sort_helper(left)
            merge_sort_helper(right)

            # merge
            merge(array, left, right)


def merge(array, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def create_array(num):
    temp = []
    for i in range(num):
        temp.append(random.randrange(10000))

    return temp


def get_times(random_arrays):
    # iterate through the arrays
    for array in random_arrays:
        # grab start time
        start = time.time()

        # perform insertion sort
        merge_sort(array)

        # grab total time
        end = time.time() - start

        # plot data
        print(len(array), end)


def main():
    # create random arrays up to 10,000
    nums = [750, 1000, 2500, 5000, 10000, 15000, 20000]
    random_arrays = []

    for num in nums:
        random_arrays.append(create_array(num))

    get_times(random_arrays)


if __name__ == "__main__":
    main()