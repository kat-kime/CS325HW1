import random
import time


def insertion_sort(int_array):
    """
    Sorts numbers using an insertion sort algorithm
    :param int_array: array of integers
    :return: numbers in sorted in descending order
    """
    # if array is less than 2, return
    if len(int_array) < 2:
        return int_array

    j = 1

    # iterate through array
    while j < len(int_array):
        key = int_array[j]

        i = j - 1

        # while a[i] less than key or i >= 0, move a[i] and iterate backwards
        while i >= 0 and int_array[i] < key:
            int_array[i + 1] = int_array[i]

            i -= 1

        # insert key
        int_array[i + 1] = key

        j += 1

    return int_array


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
        insertion_sort(array)

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