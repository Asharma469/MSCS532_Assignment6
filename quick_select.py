from randomized_quick_sort import Partition, RandomizedPartition

# QuickSelect algorithm using the randomized partition from randomized quicksort, which I already implemented in randomized_quick_sort.py.
def SelectKthSmallest(inputArray: list[int], k: int) -> int:

    # K must be within the valid range of the array length. If not, raise Error.
    if k < 1 or k > len(inputArray):
        raise ValueError("k must be between 1 and the number of values")

    items = list(inputArray)
    target = k - 1  # index of kth smallest element in sorted array.
    return _SelectKthSmallestRecursive(items, 0, len(items) - 1, target)


def _SelectKthSmallestRecursive(
    items: list[int], left: int, right: int, target: int
) -> int:
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