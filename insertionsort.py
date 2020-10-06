"""
Name:               Kat Kime
Date:               October 4, 2020
Description:        Takes a data file and sorts the numbers in descending order using an insertion sort algorithm.
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
    outfile = open("insert.out.txt", "w")

    for line in data:
        out = ""

        sorted_line = insertion_sort(line)
        print(sorted_line)

        for num in sorted_line:
            out += str(num) + " "

        outfile.write(out)
        outfile.write("\n")

    outfile.close()


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


if __name__ == "__main__":
    main()
