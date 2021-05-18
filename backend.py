"""E"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass
class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node


class Day:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for item in items:
            self.append(item)

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def __len__(self) -> int:
        """Return the number of elements in this list.
        """
        curr = self._first
        len_so_far = 0
        while curr is not None:
            len_so_far += 1
            curr = curr.next

        return len_so_far

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.
        """
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True

            curr = curr.next
        return False


class User:
    """
    ...
    """
    email: str
    password: str
    name: str
    tasks: list  # A list of tuples containing the task and the amount of time allocated
    # sorted by priority.
    activities: list  # A list of tuples containing the activity and the amount of time allocated
    # sorted by priority.
    hobbies: list
    want_to_learn: list

    def __init__(self, email: str, password: str, name: str, tasks: list, activities: list,
                 hobbies: list, want_to_learn: list):
        ...


class Schedule:
    """
    ...
    """
    monday: dict
    tuesday: dict
    wednesday: dict
    thursday: dict
    friday: dict
    saturday: dict
    sunday: dict

