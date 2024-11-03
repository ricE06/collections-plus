"""
Implements the Linked List data structure. 

In a linked list, each node stores both a value and a reference
to the next node in the array. The first node is called the head.
The list ends when the final nodes points to None. This final node
is called the tail.

This implementation keeps track of both the length and the tail node.

Space complexity: O(n), with O(n) extra space
Time complexity:
    Arbitrary indexing or mutating: O(n)
    Known indexing or mutating: O(1)
"""

from typing import Any, Optional, Iterable

class LinkedListNode():
    """
    An individual node of a linked list.

    Attributes:
        value: the value to be stored in this node
        next: the next linked list node
    """

    def __init__(self, value: Any, next: Optional["LinkedListNode"] = None) -> None:
        self.value = value
        self.next = next

class LinkedList():
    """
    A linked list.

    Attributes:
        length: how many nodes are contained in the list
        head: the first LinkedListNode in the list
        tail: the last LinkedListNode in the list.
    """

    def __init__(self, *values: Optional[Iterable[Any]] = tuple()) -> None:
        self._head = LinkedListNode(None) # sentinel node
        self._tail = self._head
        self._length = 0
        prev_node = self._head
        for val in values:
            node = LinkedListNode(val)
            prev_node.next = node
            prev_node = node
            self._length += 1
        # prev_node.next = self._tail
        self._tail = prev_node

    @staticmethod
    def index_into(func):
        """
        Decorator to call the function once we have
        reached the proper index node.
        Range of indices allowed is (-len) to (+len-1), inclusive.
        """
        def wrapper(self, index: int, *args, **kwargs) -> None:
            if not isinstance(index, int):
                raise TypeError("Index into LinkedList must be an integer.")
            if not -self._length <= index < self._length:
                raise IndexError("LinkedList index out of range.")
            if index < 0: index += self._length

            prev_node = self._head
            node = self._head.next
            for _ in range(index):
                prev_node = node
                node = node.next
            return func(prev_node, node, *args, **kwargs)

        return wrapper

    def __repr__(self):
        out = "LinkedList("
        node = self._head.next
        for idx in range(self._length):
            out += str(node)
            if idx < self._length - 1: out += ", "
        out += ")"
        return out

    @index_into
    def __getitem__(self, prev_node: LinkedListNode, node: LinkedListNode) -> Any:
        """
        Returns the value at the specified node.
        """
        return node.value

    @index_into
    def __setitem__(self, prev_node: LinkedListNode, node: LinkedListNode, val: Any) -> None:
        """
        Sets the value at the specified node to `val`.
        """
        node.value = val

    @index_into
    def __delitem__(self, prev_node: LinkedListNode, node: LinkedListNode) -> None:
        next_node = node.next
        prev_node.next = next_node
        self._length -= 1
        del node

    def __len__(self) -> int:
        return self._length

    def __length_hint__(self):
        return NotImplemented

    def __iter__(self):
        """
        Returns a generator to iterate over the LinkedList.
        """
        node = self._head.next
        for _ in range(self._length):
            yield node.value
            node = node.next

    def __eq__(self, other: "LinkedList") -> bool:
        """
        Checks for equality. Equality is defined as the value in each
        node for both Linked Lists being equal.
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Can only compare LinkedLists to a LinkedList")
        if len(self) != len(other):
            return False
        for self_val, other_val in zip(self, other):
            if self_val != other_val:
                return False
        return True

    # todo: the other ordering methods. 

    def __lt__(self, other: "LinkedList") -> bool:
        raise NotImplementedError

    def __le__(self, other: "LinkedList") -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

    @index_into
    def pop(self, prev_node: LinkedListNode, node: LinkedListNode) -> Any: 
        raise NotImplementedError

    def append(self, value: Any) -> None:
        raise NotImplementedError

    def extend(self, other: "LinkedList") -> None:
        raise NotImplementedError

    def count(self, value: Any) -> int:
        raise NotImplementedError

    def index(self, value: Any) -> int:
        raise NotImplementedError

    @index_into
    def insert(self, prev_node: LinkedListNode, node: LinkedListNode, value: Any) -> None:
        raise NotImplementedError

    def remove(self, value: Any) -> None:
        raise NotImplementedError

    def copy(self) -> "LinkedList":
        raise NotImplementedError

    def __add__(self, other: "LinkedList") -> "LinkedList":
        raise NotImplementedError

    def __mul__(self, times: int) -> "LinkedList":
        raise NotImplementedError



