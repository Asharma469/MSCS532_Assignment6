from randomized_quick_sort import Partition, RandomizedPartition, RandomizedQuickSort

# QuickSelect algorithm using the randomized partition from randomized quicksort, which I already implemented in randomized_quick_sort.py.
def SelectKthSmallest(inputArray: list[int], k: int) -> int:

    # K must be within the valid range of the array length. If not, raise Error.
    if k < 1 or k > len(inputArray):
        raise ValueError("k must be between 1 and the number of values")

    items = list(inputArray)
    target = k - 1  # index of kth smallest element in sorted array.
    return _SelectKthSmallestRecursive(items, 0, len(items) - 1, target)


def _SelectKthSmallestRecursive(items: list[int], left: int, right: int, target: int) -> int:
    if left == right:
        return items[left]

    # Quick select also partitions the array around a random pivot, like quick sort.
    # The random pivot helps avoid consistently poor partitions.
    # RandomizedPartition returns the bounds around values equal to the pivot.
    left_end, right_start = RandomizedPartition(items, left, right)

    # Recurse only into the partition that could contain the target element.
    if target <= left_end:
        return _SelectKthSmallestRecursive(items, left, left_end, target)
    if target >= right_start:
        return _SelectKthSmallestRecursive(items, right_start, right, target)
    return items[target]


# Deterministic QuickSelect using the Median of Medians pivot.
def SelectKthSmallestMedianOfMedians(inputArray: list[int], k: int) -> int:

    # K must be within the valid range of the array length. If not, raise Error.
    if k < 1 or k > len(inputArray):
        raise ValueError("k must be between 1 and the number of values")

    items = list(inputArray)
    target = k - 1  # index of kth smallest element in sorted array.
    return _SelectWithMedianOfMedians(items, 0, len(items) - 1, target)


def _SelectWithMedianOfMedians(items: list[int], low: int, high: int, target: int) -> int:
    if low == high:
        return items[low]

    left_end, right_start = MedianPartition(items, low, high)

    # Only continue on the partition that could contain the target element.
    if target <= left_end:
        return _SelectWithMedianOfMedians(items, low, left_end, target)
    if target >= right_start:
        return _SelectWithMedianOfMedians(items, right_start, high, target)
    return items[target]


def MedianPartition(items: list[int], low: int, high: int) -> tuple[int, int]:
    # Find a deterministic pivot using the Median of Medians.
    pivot = _MedianOfMedians(items, low, high)
    pivot_index = next(index for index in range(low, high + 1) if items[index] == pivot)

    # Partition into values smaller than, equal to, and greater than the pivot.
    return Partition(items, low, high, pivot_index)


def _MedianOfMedians(items: list[int], low: int, high: int) -> int:
    # Sort groups of at most five and collect each group's median.
    medians = []
    for start in range(low, high + 1, 5):
        group = items[start:min(start + 5, high + 1)]
        # Using Randomized QuickSort to sort the group of at most five elements.
        RandomizedQuickSort(group, 0, len(group) - 1)
        # The median of the sorted group is the middle element.
        medians.append(group[len(group) // 2])

    # A small range's median is its deterministic pivot.
    if len(medians) == 1:
        return medians[0]

    # Select the median of the medians using the same deterministic method.
    median_target = len(medians) // 2
    # This step recursively selects the median of the medians to determine the pivot.
    # for longer arrays, this recursive step ensures that the pivot is a good approximation of the true median.
    return _SelectWithMedianOfMedians(
        medians, 0, len(medians) - 1, median_target
    )