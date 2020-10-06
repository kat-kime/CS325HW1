"""
Name:               Kat Kime
Date:               October 4, 2020
Description:        Takes a data file and sorts the numbers in descending order using a merge sort algorithm.
"""


def main():
    process_file("data.txt")


def process_file(data_file):
    """
    Takes a data file and processes each line while writing the output to a file.
    :param data_file: user-defined file
    """
    # read file
    infile = open(data_file, "r")

    data = []

    for line in infile.readlines():
        line = line.strip()
        line = line.split(' ')

        i = 0
        while i < len(line):
            line[i] = int(line[i])

            i += 1

        data.append(line)

    infile.close()

    # process file
    outfile = open("merge.out.txt", "w")

    for line in data:
        out = ""

        sorted_line = merge_sort(line)
        print(sorted_line)

        for num in sorted_line:
            out += str(num) + " "

        outfile.write(out)
        outfile.write("\n")

    outfile.close()


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


if __name__ == "__main__":
    main()