class Array:

    # Using list becuase I doubt we are supposed to handle memory manually.. could be fun in C++ though.
    def __init__(self, values: list[int]):
        initialValues = values if values is not None else []
        self.size = len(initialValues)
        self.capacity = max(1, self.size)
        self.item = [0] * self.capacity

        for index, value in enumerate(initialValues):
            self.item[index] = value

    # might need length as well.
    def len(self) -> int:
        return self.size

    def __len__(self) -> int:
        return self.size

    # simple access by index, should be O(1) time.
    def access(self, index: int) -> int:
        self._check_element_index(index)
        return self.item[index]

    # insert a value at a specific index, shifting later values right.
    # O(n) time due to shifting elements, worst case when inserting at the beginning.
    def insert(self, index: int, value: int) -> None:
        self._check_insert_index(index)

        # ensure there is enough capacity for the new element
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        # otherwise, shift elements to make space for the new value
        for current in range(self.size, index, -1):
            self.item[current] = self.item[current - 1]

        self.item[index] = value
        self.size += 1

    # delete a value at a specific index, shifting later values left.
    # O(n) time due to shifting elements, worst case when deleting the first element.
    def delete(self, index: int) -> int:
        """Delete and return the value at index, shifting later values left."""
        self._check_element_index(index)
        removed = self.item[index]

        # if deleting the last element, just remove it
        if index == self.size - 1:
            self.size -= 1
            self.item[self.size] = 0
            return removed

        # similar to insertion.
        for current in range(index, self.size - 1):
            self.item[current] = self.item[current + 1]

        self.size -= 1
        self.item[self.size] = 0
        return removed

    # helper methods for index checking and resizing the array
    def _check_element_index(self, index: int) -> None:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("index must be an integer")
        if index < 0 or index >= self.size:
            raise IndexError("index must be between 0 and the last array position")

    def _check_insert_index(self, index: int) -> None:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("index must be an integer")
        if index < 0 or index > self.size:
            raise IndexError("index must be between 0 and the array length")

    # I could have just added capacity and block going over capacity for simplicity
    # but ended up implementing dynamic resizing to allow the array to grow as needed.
    def _resize(self, new_capacity: int) -> None:
        resizedItems = [0] * new_capacity
        for index in range(self.size):
            resizedItems[index] = self.item[index]
        self.item = resizedItems
        self.capacity = new_capacity

    def print(self) -> None:
        output = ""
        for index in range(self.size):
            output += str(self.item[index]) + ", "
        print(output)


# very simple with Array class.
class Stack:

    def __init__(self):
        self.item = Array([])

    def push(self, value: int) -> None:
        self.item.insert(self.item.len(), value)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.item.delete(self.item.len() - 1)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.item.access(self.item.len() - 1)

    def len(self) -> int:
        return self.item.len()

    def is_empty(self) -> bool:
        return self.item.len() == 0

    def print(self) -> None:
        self.item.print()


# Very similar to Stack.
class Queue:
    def __init__(self):
        self.item = Array([])

    def enqueue(self, value: int) -> None:
        self.item.insert(self.item.len(), value)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.item.delete(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.item.access(0)

    def front(self) -> int:
        return self.peek()

    def len(self) -> int:
        return self.item.len()
    
    def print(self) -> None:
        self.item.print()
    
    def is_empty(self) -> bool:
        return self.item.len() == 0
