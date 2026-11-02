import random
from typing import List
from quick_select import SelectKthSmallest

# helper functions
def GetRandomArray(size: int) -> List[int]:
    return [random.randint(1, size) for _ in range(size)]

# generate an array with duplicate values randomly placed in the array
def GenShuffledDuplicateArray(size: int, values: int) -> List[int]:
    return [random.randint(1, values) for _ in range(size)]


ARRAY_SIZES = {
    "small": 10,
    "medium": 20,
    "large": 30,
}
REPEATS = 30
ALGORITHMS = (
    "quickselect",
    "quickselect_with_quick_sort_partition"
)

random.seed(42)
datasets = {"random": [], "sorted": [], "reversed": [], "duplicates": []}

for length in ARRAY_SIZES.values():
    random_values = GetRandomArray(length)
    datasets["random"].append(random_values)
    datasets["sorted"].append(sorted(random_values))
    datasets["reversed"].append(sorted(random_values, reverse=True))
    datasets["duplicates"].append(GenShuffledDuplicateArray(length, 3))

#just testing here for now. Need to implement analysis class.
print(datasets["sorted"][0])
print("quickselect", SelectKthSmallest(datasets["sorted"][0], 4))