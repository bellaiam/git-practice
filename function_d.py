def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    sorted_list = numbers.sort()
    largest_number = sorted_list[-1]
    return largest_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
