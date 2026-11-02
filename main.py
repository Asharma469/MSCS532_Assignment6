import random
from typing import List
from data_structures import Array, Stack, Queue
from linked_list import LinkedList
from quick_select import SelectKthSmallest, SelectKthSmallestMedianOfMedians
from analysis import FunctionAnalyzer

# helper functions
def GetRandomArray(size: int) -> List[int]:
    return [random.randint(1, size) for _ in range(size)]

# generate an array with duplicate values randomly placed in the array
def GenShuffledDuplicateArray(size: int, values: int) -> List[int]:
    return [random.randint(1, values) for _ in range(size)]


ARRAY_SIZES = {
    "small": 100,
    "medium": 300,
    "large": 1000,
}
REPEATS = 30
ALGORITHMS = (
    ("Randomized QuickSelect", SelectKthSmallest),
    ("Median of Medians QuickSelect", SelectKthSmallestMedianOfMedians),
)


random.seed(42)
datasets = {"random": [], "sorted": [], "reversed": [], "duplicates": []}

for length in ARRAY_SIZES.values():
    random_values = GetRandomArray(length)
    datasets["random"].append(random_values)
    datasets["sorted"].append(sorted(random_values))
    datasets["reversed"].append(sorted(random_values, reverse=True))
    datasets["duplicates"].append(GenShuffledDuplicateArray(length, 3))

""" Un-comment this section to test simple quickselect results.
#just testing here for now.
print("enter the value of k")
k = 9
#k = int(input())
print("k is", k)
if(k < 1 or k > len(datasets["sorted"][0])):
    raise ValueError("k must be between 1 and the number of values")
print("(k-1)th element in the sorted array: ", sorted(datasets["sorted"][0].copy())[k-1])
print("quickselect", SelectKthSmallest(datasets["sorted"][0], k))
print("quickselect_median_of_medians", SelectKthSmallestMedianOfMedians(datasets["sorted"][0], k))
"""

# Analyzer runs both QuickSelects with all 4 different arrays for k as 1, (length + 1) // 2, and length, with multiple repetitions.
# Fastest execution time from the repetitions is recorded in the analysis results.
def RunAnalysis():
    for test_name, test_arrays in datasets.items():
        for function_name, selection_function in ALGORITHMS:
            analyzer = FunctionAnalyzer(REPEATS, test_arrays, test_name)
            analyzer.StartTest(selection_function, function_name)
            analyzer.PrintResult()


if __name__ == "__main__":
    RunAnalysis()


print("_____________________________")
print("_____________________________")

print("Array:")
testArr = Array([1, 2, 3, 4, 5])
print("Created array with values [1, 2, 3, 4, 5]:")
testArr.print()
print("Insert 10 at index 2:")
testArr.insert(2, 10)
testArr.print()
print(f"Delete value at index 2 (removed {testArr.delete(2)}):")
testArr.print()

print("_____________________________")

print("Stack:")
testStack = Stack()
print("Push 1, 2, and 3:")
testStack.push(1)
testStack.push(2)
testStack.push(3)
testStack.print()
print(f"Pop top value (removed {testStack.pop()}):")
testStack.print()
print(f"Pop top value (removed {testStack.pop()}):")
testStack.print()

print("_____________________________")

print("Queue:")
testQueue = Queue()
print("Enqueue 1, 2, and 3:")
testQueue.enqueue(1)
testQueue.enqueue(2)
testQueue.enqueue(3)
testQueue.print()
print(f"Dequeue front value (removed {testQueue.dequeue()}):")
testQueue.print()
print(f"Dequeue front value (removed {testQueue.dequeue()}):")
testQueue.print()

print("_____________________________")

print("Linked List:")
testLinkedList = LinkedList()
print("Insert 1, 2, and 3 at the end:")
testLinkedList.insert(0, 1)
testLinkedList.insert(1, 2)
testLinkedList.insert(2, 3)
testLinkedList.print()
print(f"Delete value at index 1 (removed {testLinkedList.delete(1)}):")
testLinkedList.print()
print("_____________________________")