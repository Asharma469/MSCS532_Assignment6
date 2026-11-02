# linked list will need a node class. Not giving it a type, maybe any type is acceptable? not sure.
class Node:
    def __init__(self, value):
        # value and a reference to the next node is all it needs.
        self.value = value
        self.next: Node | None = None


# linked list class that manages a sequence of nodes.
# Keeps track of the first node basically, and updates each node to connect them together.
class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def insert(self, index: int, value: int) -> None:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("index must be an integer")
        if index < 0 or index > self.size:
            raise IndexError("index must be between 0 and the list length")
        
        node = Node(value)

        # if inserting at the head, update the head to the new node.
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            # else we find the node just before the insertion point.
            previous = self.nodeAt(index - 1)
            node.next = previous.next
            previous.next = node

        # keeping track of size.
        self.size += 1

    def delete(self, index: int) -> int:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("index must be an integer")
        if index < 0 or index >= self.size:
            raise IndexError("index must be between 0 and the last list position")

        # If it's head, then update head.
        if index == 0:
            removed = self.head
            if removed is None:
                raise ValueError("head is None")
            self.head = removed.next
        else:
            # else we take the removed node
            previous = self.nodeAt(index - 1)
            removed = previous.next
            if removed is None:
                raise ValueError("node to remove is None")
            previous.next = removed.next

        self.size -= 1
        return removed.value

    # learnt to make iterator in C, but for now returning a list that simulates the linked list traversal with each node.
    # would not be a good idea to analyze this, since it's adding extra overhead by creating a list of nodes.
    def traverse(self) -> list[Node]:
        values = []
        current = self.head
        while current is not None:
            values.append(current)
            # keep updating current to the next node until there's no more nodes.
            current = current.next
        return values

    # keeping track of Size to avoid having to traverse to count length.
    def len(self) -> int:
        return self.size

    # get the node at a specific index.
    def nodeAt(self, index: int) -> Node:
        current = self.head
        for _ in range(index):
            assert current is not None
            current = current.next
        assert current is not None
        return current

    def print(self) -> None:
        # print the linked list by traversing through all nodes.
        output = ""
        for node in self.traverse():
            output += f"{node.value} -> "
        output += "None"
        print(output)