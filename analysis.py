import timeit
from typing import Callable, List, Optional, Tuple

SelectionFunction = Callable[[List[int], int], int]
AnalysisResult = Tuple[int, int, Optional[int], float, str]


class FunctionAnalyzer:
    def __init__(self, repeats: int, test_arrays: List[List[int]], test_name: str):
        self.repeats = repeats
        self.test_arrays = test_arrays
        self.test_name = test_name
        self.function_name = ""
        self.results: List[AnalysisResult] = []

    def StartTest(self, functionToBeBenchmarked: SelectionFunction, function_name: str):
        self.function_name = function_name
        self.results = []

        for input_values in self.test_arrays:
            if not input_values:
                raise ValueError("test arrays must not be empty")

            length = len(input_values)
            ks = sorted({1, (length + 1) // 2, length})
            expected_values = sorted(input_values)

            for k in ks:
                try:
                    result = functionToBeBenchmarked(input_values.copy(), k)
                except RecursionError:
                    self.results.append(
                        (length, k, None, -1, "RecursionError")
                    )
                    continue

                if result != expected_values[k - 1]:
                    raise AssertionError(
                        f"{function_name} returned an incorrect value for k={k}"
                    )

                timer = timeit.Timer(
                    stmt="select(values, k)",
                    setup="values = original.copy()",
                    globals={
                        "select": functionToBeBenchmarked,
                        "original": input_values,
                        "k": k,
                    },
                )
                try:
                    samples = timer.repeat(repeat=self.repeats, number=1)
                except RecursionError:
                    self.results.append(
                        (length, k, result, -1, "RecursionError")
                    )
                    continue

                self.results.append(
                    (length, k, result, min(samples), "ok")
                )

    def PrintResult(self):
        print(f"\n{self.function_name} on {self.test_name} arrays:")
        for length, k, value, elapsed, status in self.results:
            if elapsed == -1:
                print(f"  Length {length}, k={k}: {status}")
            else:
                print(
                    f"  Length {length}, k={k}: selected {value} "
                    f"in {elapsed * 1000:.6f} ms"
                )