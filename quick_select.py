from randomized_quick_sort import RandomizedPartition

# QuickSelect algorithm using the randomized partition from randomized quicksort, which I already implemented in randomized_quick_sort.py.
def SelectKthSmallest(inputArray: list[int], k: int) -> int:

    # K must be within the valid range of the array length. If not, raise Error.
    if k < 1 or k > len(inputArray):
        raise ValueError("k must be between 1 and the number of values")

    items = list(inputArray)
    target = k - 1  # index of kth smallest element in sorted array.
    left = 0
    right = len(items) - 1

    # Quick select also partitions the array around a random pivot, like quick sort.
    # The random pivot helps avoid consistently poor partitions.
    while left <= right:
        # RandomizedPartition uses the same three-way partitioning as randomized quicksort.
        # It returns the bounds around the values equal to the pivot.
        left_end, right_start = RandomizedPartition(items, left, right)

        # Only continue on the partition that could contain the target element.
        if target <= left_end:
            right = left_end
        elif target >= right_start:
            left = right_start
        else:
            return items[target]

    return -1