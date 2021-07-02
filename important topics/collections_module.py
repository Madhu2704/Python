import collections as CEO
from icecream import ic

ic.configureOutput(includeContext=True)


def noOfOccurancesOfEachItem(items_list: list) -> dict:
    # This will create a sorted order key value pair with
    # item: no of times it is present in the container
    return CEO.Counter(items_list)


if __name__ == '__main__':
    items_container = [1, 1, 2, 2, 5, 6, 8, 6, 5, 5, 5, 8, 5,
                       6, 8, 5, 6, 9, 4, 6, 3, 6, 9, 9, 6, 6, 333, 5, 3, 3, ]
    ic(noOfOccurancesOfEachItem(items_container))
