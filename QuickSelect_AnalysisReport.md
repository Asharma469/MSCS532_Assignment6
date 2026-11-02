# QuickSelect Performance Analysis

## 1. Introduction

This report compares two implementations for finding the kth smallest value
in an array: Randomized QuickSelect and deterministic QuickSelect using the
Median of Medians pivot. Unlike a full sort, QuickSelect only partitions the
part of the array needed to find the requested order statistic. The benchmark
compares both algorithms across random, sorted, reverse-sorted, and
duplicate-heavy inputs.

The measurements show Randomized QuickSelect running faster in every tested
case. Median of Medians has higher constant overhead in this implementation,
but it provides a worst-case linear-time guarantee. These experiments are
small and limited to the tested inputs; they do not replace the theoretical
analysis.

## 2. Implementation Details

Both functions accept an input array and a one-based `k`, validate that k is
within the array's length, and return the value that would appear at position
k in sorted order. Each function copies its input, so it does not change the
caller's array.

Randomized QuickSelect chooses a random pivot, then uses a three-way partition
to group values smaller than, equal to, and greater than the pivot. It
continues only in the partition that can contain the target index. If the
target lies in the equal-to-pivot region, that value is returned immediately.
This also handles duplicate values without repeatedly selecting equal
elements.

The deterministic version chooses a pivot with Median of Medians. It sorts
groups of at most five values, collects their medians, and recursively finds
the median of those medians. It then uses the same three-way partition and
continues only in the relevant partition. Sorting each group is bounded work
because each group contains at most five elements.

## 3. Performance Analysis

Each partition scans its active range once, taking linear time in that
range. QuickSelect does not recursively process both outer partitions as
Quicksort does; it follows only the side containing the target.

| Algorithm | Best case | Expected case | Worst case |
|---|---|---|---|
| Randomized QuickSelect | O(n) | O(n) | O(n²) |
| Median of Medians QuickSelect | O(n) | O(n) | O(n) |

Randomized QuickSelect has expected O(n) time because random pivots usually
discard a substantial portion of the active range. A sequence of poor pivots
can instead leave almost the entire range for the next step, producing
O(n²) worst-case work.

Median of Medians selects a pivot that guarantees a constant fraction of
values can be discarded at each level. Its recurrence is
T(n) = T(n/5) + T(7n/10) + O(n), which yields O(n) worst-case time. The
algorithm performs extra grouping and recursive pivot-selection work, which
can make it slower in practice even though its worst-case bound is stronger.

Both implementations copy the input, requiring O(n) additional space. The
partition itself is in-place. Randomized QuickSelect's recursion stack is
O(log n) on expected balanced paths and O(n) in the worst case. Median of
Medians also allocates arrays of group medians; its additional memory remains
O(n), with recursion-stack use proportional to the shrinking selection
subproblems.

## 4. Empirical Analysis

The benchmark uses arrays of 100, 300, and 1,000 values. For each size, it
tests four distributions:

- **Random:** Values are independently selected from 1 through the array
  length.
- **Sorted:** The random input for that size, sorted in ascending order.
- **Reversed:** The same random input sorted in descending order.
- **Duplicates:** Values are independently selected from 1 through 3.

For each array, the analyzer tests k = 1, the middle position
`(length + 1) // 2`, and k equal to the array length. Thus, for lengths 100,
300, and 1,000, the middle k values are 50, 150, and 500 respectively. The
analyzer checks each result against the corresponding value in a sorted copy.
It times each algorithm 30 times per case and reports the minimum time. Times
below are in milliseconds. Each cell gives Randomized QuickSelect (R) first
and Median of Medians (M) second. The fastest time in each row is bolded.

### 4.1 Results: Arrays of 100 Elements

| k | Random | Sorted | Reversed | Duplicates |
|---:|---|---|---|---|
| 1 | R: 0.059300 ms<br>M: 0.835400 ms | R: 0.042000 ms<br>M: 0.519700 ms | R: 0.045200 ms<br>M: 0.665200 ms | R: **0.018400 ms**<br>M: 0.157000 ms |
| 50 | R: 0.095100 ms<br>M: 0.830600 ms | R: 0.044100 ms<br>M: 0.343400 ms | R: 0.071200 ms<br>M: 0.555900 ms | R: **0.018800 ms**<br>M: 0.127200 ms |
| 100 | R: 0.068600 ms<br>M: 0.795100 ms | R: 0.038000 ms<br>M: 0.316600 ms | R: 0.045000 ms<br>M: 0.520200 ms | R: **0.017100 ms**<br>M: 0.162700 ms |

### 4.2 Results: Arrays of 300 Elements

| k | Random | Sorted | Reversed | Duplicates |
|---:|---|---|---|---|
| 1 | R: 0.186000 ms<br>M: 2.772800 ms | R: 0.107800 ms<br>M: 1.076700 ms | R: 0.129500 ms<br>M: 1.973700 ms | R: **0.052300 ms**<br>M: 0.437400 ms |
| 150 | R: 0.321400 ms<br>M: 1.367900 ms | R: 0.149200 ms<br>M: 1.002600 ms | R: 0.209000 ms<br>M: 1.225300 ms | R: **0.053200 ms**<br>M: 0.365100 ms |
| 300 | R: 0.170900 ms<br>M: 2.987300 ms | R: 0.108100 ms<br>M: 1.053700 ms | R: 0.171800 ms<br>M: 1.871500 ms | R: **0.052500 ms**<br>M: 0.442500 ms |

### 4.3 Results: Arrays of 1,000 Elements

| k | Random | Sorted | Reversed | Duplicates |
|---:|---|---|---|---|
| 1 | R: 0.645500 ms<br>M: 8.228000 ms | R: 0.411000 ms<br>M: 3.719400 ms | R: 0.480400 ms<br>M: 6.341400 ms | R: **0.225700 ms**<br>M: 1.484400 ms |
| 500 | R: 1.102400 ms<br>M: 7.429600 ms | R: 0.846300 ms<br>M: 3.636800 ms | R: 0.742200 ms<br>M: 4.036700 ms | R: **0.202200 ms**<br>M: 1.452800 ms |
| 1000 | R: 0.597900 ms<br>M: 7.512900 ms | R: 0.357100 ms<br>M: 3.981100 ms | R: 0.404700 ms<br>M: 3.789500 ms | R: **0.195300 ms**<br>M: 1.607800 ms |

## 5. Discussion

Randomized QuickSelect was faster for every size, distribution, and k value
in these measurements. Median of Medians took roughly 3 to 18 times as long
in the displayed cases. Its grouping, small-group sorting, and recursive
selection of a pivot add substantial fixed work at these input sizes. This
timing difference does not mean it has a worse asymptotic worst case: it is
the algorithm with the O(n) worst-case guarantee.

For both methods, selecting an extreme order statistic can require scanning
large portions of the input. The random inputs and duplicate-heavy inputs
showed some variation with k, but there is no consistent trend that makes
one k value universally fastest. Three-way partitioning is useful with
duplicates because it groups all pivot-equal values at once; if the target
falls in that group, selection ends without processing those values again.

The results should be treated as measurements of these implementations on
these generated inputs, not as proof of the complexity bounds. The analyzer
reports the fastest of 30 samples, which reduces the effect of interruptions
but is not representative of a typical run. Randomized QuickSelect also
chooses new pivots across runs, so its minimum sample can reflect a favorable
sequence of choices. The benchmark does not record machine or Python
version, and the inputs are limited in size and variety.

## 6. Conclusion

The Analyzer results show that Randomized QuickSelect is faster in the
measured cases, while Median of Medians provides the stronger worst-case
guarantee. For ordinary inputs where expected performance is acceptable,
Randomized QuickSelect is an efficient choice in this implementation. When
an O(n) worst-case bound is required, Median of Medians offers that
guarantee at the cost of higher practical overhead in these tests.
