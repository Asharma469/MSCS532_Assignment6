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

    # simple access by index, should be O(1) time.
    def access(self, index: int) -> int:
        self._check_element_index(index)
        return self.item[index]

    # insert a value at a specific index, shifting later values right.
    # O(n) time due to shifting elements, worst case when inserting at the beginning.
    def insert(self, index: int, value: int) -> None:
        self._check_element_index(index)

        # if inserting at the end, just append the value
        if index == self.size:
            self.item.append(value)
            self.size += 1
            return

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