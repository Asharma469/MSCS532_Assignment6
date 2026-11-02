# Elementary Data Structures Report

## Overview

This project implements a dynamic array, a stack and queue built on that array,
and a singly linked list. This report gives a brief explanation of their
operation costs and where each structure is useful.

## Operations and Time Complexity

Let *n* be the number of stored values.

| Structure | Operation | Time | Explanation |
|---|---|---:|---|
| Array | Access by index | O(1) | The index directly identifies the stored position. |
| Array | Insert or delete | O(n) | Elements after the changed position may need to shift. |
| Array | Insert at end | O(1) amortized | Most insertions add at the end; occasionally the backing storage grows and copies values, taking O(n). |
| Stack | Push | O(1) amortized | Adds an item at the array end. |
| Stack | Pop or peek | O(1) | Removes or reads the last item. |
| Queue | Enqueue | O(1) amortized | Adds an item at the array end. |
| Queue | Dequeue | O(n) | Removes the first item and shifts the remaining items left. |
| Queue | Peek at front | O(1) | Reads the item at index zero. |
| Linked list | Insert or delete at head | O(1) | Updates the head reference and, for insertion, the new node's next reference. |
| Linked list | Insert or delete by index | O(n) | Must walk from the head to reach the position. |
| Linked list | Traverse | O(n) | Visits each node once. |

The array's insertion and deletion costs are worst-case costs for arbitrary
positions. Appending is O(1) amortized because the array grows its capacity
geometrically; a particular append that triggers a resize takes O(n). Stack
push and queue enqueue use that end-insertion operation. The current queue
uses the same array implementation directly, so dequeue is O(n), not O(1).

## Where Each Structure Shines

- **Array:** Choose it when fast indexed access is important, such as looking
  up an item by position. Its contiguous, indexable storage is straightforward
  to use. It is less suitable when many items must be inserted or removed near
  the beginning, because values have to shift.
- **Stack:** A stack is a natural fit when the most recently added item should
  be handled first (last in, first out). Examples include undo history,
  function-call tracking, and depth-first traversal. With this array-backed
  implementation, its core operations are constant time amortized.
- **Queue:** A queue is useful when items should be handled in arrival order
  (first in, first out), such as a simple work list or line of requests. This
  implementation is easy to understand, but removing from the front shifts
  all remaining items. For a workload with frequent dequeues or large queues,
  a circular buffer or linked queue would avoid that cost.
- **Singly linked list:** A linked list is useful when changing the head is
  common, or when an existing node reference is already available and links
  can be updated directly. It does not provide fast indexed access: reaching
  an arbitrary position requires walking through the nodes. Each node also
  stores a reference to the next node, adding per-item memory overhead
  compared with an array.

For indexed insertion and deletion, an array and this index-based linked list
both take O(n) time, but for different reasons: the array shifts values while
the list searches for the position. A linked-list insertion or deletion is
O(1) once the relevant node (or its predecessor) is already known. Arrays
often remain the simpler and more practical choice when fast indexing is
needed.

## Empirical Analysis

I did not write a separate empirical analysis for these data structures:
there was not enough time, and these basic operations are relatively
straightforward to analyze from their implementations. More importantly,
timing numbers on their own would not say much without a meaningful comparison
of alternative implementations under the same workloads—for example, this
array-backed queue versus a circular-buffer queue. The discussion above is
therefore based on operation structure and asymptotic complexity, not
benchmark results.