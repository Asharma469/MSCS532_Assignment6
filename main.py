import random
from typing import List
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
