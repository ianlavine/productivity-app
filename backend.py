"""E"""
from __future__ import annotations
from dataclasses import dataclass
from types import AsyncGeneratorType
from typing import Any, Iterable, Optional
import random
import copy
    

@dataclass
class Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[Node] = None  # By default, this node does not link to any other node

class Event:
    """event"""
    title: str
    description: str
    time: int
    priority: int
    estimated_length: int
    start: int
    end: int
    category: str

    def __init__(self, title: str, priority: int, desc = "", time = None, est = 1, category='work', 
    start = None, end = None) -> None:
        self.title = title
        self.description = desc
        self.time = time
        self.priority = priority
        self.estimated_length = est
        self.start = start
        self.end = end
        self.category = category

class User:
    """
    ...
    """
    email: str
    password: str
    name: str
    events: list
    hobbies: list
    want_to_learn: list
    sleep_time: int
    wakeup_time: int

    def __init__(self, email: str, password: str, name: str, events: list[dict], 
                 hobbies: list[dict], want_to_learn: list[dict], sleep: int, wakeup: int):
                 # events, hobbies and want_to_learn are list[dict]. Each dictionary is an event
                 # where each key of the dictionary would represent a class instance of Event.
                 # e.g. {title: "soccer", description: "...", ...}
        self.email = email
        self.password = password
        self.name = name
        self.events = self.sort_priority([Event(...) for event in events])
        self.hobbies = self.sort_priority([Event(...) for hobby in hobbies])
        self.want_to_learn = self.sort_priority([Event(...) for skill in want_to_learn])
        self.sleep_time = sleep
        self.wakeup_time = wakeup
    
    def _partition(lst: list, pivot: Any) -> tuple[list, list]:
        smaller = []
        bigger = []

        for item in lst:
            if item.priority <= pivot.priority:
                smaller.append(item)
            else:
                bigger.append(item)

        return (smaller, bigger)
        
    def sort_priority(self) -> list:
        """ Returns a sorted list of the user's events by their priority.
        """
        lst = self.events
        if len(lst) < 2:
            return lst.copy()
        else:
            pivot = lst[0]
            smaller, bigger = self._partition(lst[1:], pivot)

            smaller_sorted = self.sort_priority(smaller)
            bigger_sorted = self.sort_priority(bigger)

            return smaller_sorted + [pivot] + bigger_sorted

    def find_priority(self) -> int:
        """
        """
        ...


class Day:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in the linked list, or None if the list is empty.
    _first: Optional[Node]

    def __init__(self, user: Any) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for event in user.events:
            self.append(event)

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

    def check_hours(self, user: Any) -> bool:
        """Checks if the estimated time for all events is less than the time awake.
        """
        time_awake = user.sleep_time - user.wakeup_time
        accumulator = 0
        curr = self._first
        while curr is not None:
            accumulator += curr.estimated_length
        
        if accumulator <= time_awake:
            return True
        else:
            return False

    def pick_time(self, event: Any) -> int:
        """Picks a time for an event to occur in (for asynchronous events)
        """
        length = event.estimate_length
        curr = self._first
        prev = None

    def create_day_onlyevents(self, user: Any) -> None:
        """Mutates nodes so that the linked list represents all tasks needed to complete in the day
         with start and end times for asynchronous events.  
        """
        if self.check_hours(user) is False:
            raise ValueError('The estimated time for all events is greater than the time awake.')
        else:
            curr = self._first
            while curr is not None:
                if curr.item.start is None:
                    ...
                    curr = curr.next
                else:
                    curr = curr.next

    def recreation_check(self, recreation: Any) -> bool:
        """Checks if a certain recreational event is already in the day (helper function for insert_recreation)
        """
        curr = self._first
        while curr is not None:
            if curr.title == recreation.title:
                return True
            else:
                curr = curr.next
        
        return False

    def insert_recreation(self, og_recreation: Any, user: Any, event1 = None, event2 = None) -> None:
        """Inserts a time slot for a recreational event. event 1 and event 2 can be put into the 
        function if wanting to insert in between two time slots. 
        """
        recreation = copy.deepcopy(og_recreation)
        if event1 is not None and event2 is not None:
            recreation.start = random.randint(event1.end, (event2.start - recreation.estimated_length))
        elif event1 is not None and event2 is None:
            recreation.start = random.randint(event1.end, (user.sleep_time - recreation.estimated_length))
        elif event1 is None and event2 is not None:
            recreation.start = random.randint(user.wakeup_time, (event2.start - recreation.estimated_length))
        else:
            recreation.start = random.randint(user.wakeup_time, (user.sleep_time - recreation.estimated_length))
        
        recreation.end = recreation.start + recreation.estimated_length
        self.append(recreation)

    def create_day(self, user: Any) -> None:
        """ Creates whole day
        """
        self.create_day_onlyevents(user)
        self.sort_day
        curr = self._first
        prev = None
        while curr is not None and prev is not None:
            if (curr.start - prev.end) > 1:
                self.insert_recreation(random.choice(user.hobbies), user, prev, curr)
                prev, curr = curr, curr.next
            else:
                prev, curr = curr, curr.next
            

    def sort_day(self):
        """Sorts linked list in terms of time.
        """
        if self._first.next is None: 
            return self._first
        else:
            mid = self.getMid(self._first)
            left = self.sort_day(self._first)
            right = self.sort_day(mid)
            return self.merge(left, right)
    
    def getMid(self, head):
        """Helper function for sort_day
        """
        prev, curr = head, head
        while curr.next and curr.next.next:
            prev = prev.next
            curr = curr.next.next
        mid = prev.next
        prev.next = None
        return mid
    
    def merge(self, head1, head2):
        """2nd helper function for sort_day
        """
        dummy = tail = Day(None)
        while head1 and head2:
            if head1.item.start < head2.item.start:
                tail.next, head1 = head1, head1.next
            else:
                tail.next, head2 = head2, head2.next

        tail.next = head1 or head2
        return dummy.next
    
    def check_overlap(self) -> list[tuple]:
        """Returns a list of events that have overlapping times
        """
        lst = []
        curr = self._first
        prev = None

        while curr is not None:
            if prev is not None :
                if range(...):
                    lst.append((curr, prev))
            else:
                prev = curr
                curr = curr.next


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

