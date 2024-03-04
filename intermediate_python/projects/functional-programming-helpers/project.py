import csv
from functools import reduce


def count(predicate, iterable):
    """
    A functionn that returns the frequency of an element in an iterable.
    A special type of `filter()` function that returns the number of
    occurrences of an element instead of returning a Boolean value.

    :params:

    :predicate: evaluated to True, will allow a counter to increment by one
    :itr: the collections containing the element of interest.
    """

    count_filter = filter(predicate, iterable)
    count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)

    return count_reduce


def average(itr):
    """
    A function that computes the arithmetic mean of a collection.
    Executed recursively to adhere to functional programming principles.

    :params:

    :itr: the collectionn to be averaged.

    Returns the average of elemments in an iterable of numbers
    """

    iterable = iter(itr)

    return avg_helper(0, iterable, 0)


def avg_helper(curr_count, itr, curr_sum):
    """
    Function responsible for implementing a loop to compute an average.

    :params:

    :curr_count:  current count of elements
    :itr:  collection
    :curr_sum:  current running total of elements in the collection.
    """
    next_num = next(itr, "null")
    if next_num == "null":
        return curr_sum / curr_count
    curr_count += 1
    curr_sum += next_num

    return avg_helper(curr_count, itr, curr_sum)


try:
    with open("1kSalesRec.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        fields = next(reader)
        print(fields[1])
        belgiums = count(lambda x: x[1] == "Belgium", reader)
        print(belgiums)
        csvfile.seek(0)
        avg_portugal = average(
            map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader))
        )
        print(avg_portugal)

except FileNotFoundError:
    print("Error! File does not exist!")
