"""E"""
from __future__ import annotations
from dataclasses import dataclass
from types import AsyncGeneratorType
from typing import Any, Iterable, Optional
import random
import copy
import datetime
    

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

<<<<<<< HEAD
    def __init__(self, email: str, password: str, name: str, events: list[dict], 
=======
    def init(self, email: str, password: str, name: str, events: list[dict], 
>>>>>>> dc5ee2a20cd52ab80b0d16da667b08825c09c5bb
                 hobbies: list[dict], want_to_learn: list[dict], sleep: int, wakeup: int):
                 # events, hobbies and want_to_learn are list[dict]. Each dictionary is an event
                 # where each key of the dictionary would represent a class instance of Event.
                 # e.g. {'title': "soccer", 'description': "...", ...}
        self.email = email
        self.password = password
        self.name = name
        self.events = self.sort_priority([Event(event['title'], event['description'], event['time'], event['priority'],
        event['estimated_length'], event['start'], event['end'], event['category']) for event in events])
        self.hobbies = self.sort_priority([Event(hobby['title'], hobby['description'], hobby['time'], hobby['priority'],
        hobby['estimated_length'], hobby['start'], hobby['end'], hobby['category']) for hobby in hobbies])
        self.want_to_learn = self.sort_priority([Event(skill['title'], skill['description'], skill['time'], skill['priority'],
        skill['estimated_length'], skill['start'], skill['end'], skill['category']) for skill in want_to_learn])
        self.sleep_time = sleep
        self.wakeup_time = wakeup
<<<<<<< HEAD
=======
        self.bad_habits = bad_habits
>>>>>>> dc5ee2a20cd52ab80b0d16da667b08825c09c5bb
    
    def _partition(self, lst: list, pivot: Any) -> tuple[list, list]:
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

    def find_priority(self):
        """
        """
        now = datetime.date.today()
        due_dates = {0: 10, 1: 7, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
        difficulties = {'easy': -1, 'med': 2, 'hard': 5}
        categories = {}

        for event in self.events:

            if event.category not in categories:
                categories[event.category] = [event]
            else:
                categories[event.category].append(event)

            if event.priority is None:
                event.priority = 0.0
                if event.category in self.want_to_learn:
                    event.priority += 1
                if event.category in self.goals:
                    event.priority += 2
                if event.category in self.bad_habits:
                    event.priority -= 1

                event.priority += difficulties[event.difficulty]
                event.priority += event.importance

                if event.due_date is not None:
                    delta = event.due_date - now
                    days = delta.days
                    if days < 7:
                        event.priority += due_dates[days]

            tie_breaker = (float(random.randrange(1, 100)))/100
            event.priority += tie_breaker

        for cat in categories:
            cur = categories[cat]
            by_priority = sorted(cur, key=lambda event: event.priority, reverse=True)
            for x in range(0, len(by_priority)):
                by_priority[x].priority -= 2 * x


class Day:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in the linked list, or None if the list is empty.
    _first: Optional[Node]

    def init(self, user: Any) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for event in user.events:
            self.append(event)
        
        temp = self._first
        self._first = Event('Wake up', 1, 'AWAKE', None, 0, 'life', user.wakeup_time, user.wakeup_time)
        self._first.next = temp
        self.append(Event('Sleep', 2, 'BEDTIME', None, 0, 'life', user.sleep_time, user.sleep_time))

        temp = self._first
        self._first = Node(Event('Wake up', 1, 'AWAKE', None, 0, 'life', user.wakeup_time, user.wakeup_time))
        self._first.next = temp
        self.append(Event('Sleep', 2, 'BEDTIME', None, 0, 'life', user.sleep_time, user.sleep_time))

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr)
            curr = curr.next

        return items_so_far

<<<<<<< HEAD

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
=======
    def check_hours(self) -> bool:
>>>>>>> dc5ee2a20cd52ab80b0d16da667b08825c09c5bb
        """Checks if the estimated time for all events is less than the time awake.
        """
        link_to_list = to_list()

        accumulator = sum([x.item.estimated_length for x in link_to_list])
        time_awake = user.sleep_time - user.wakeup_time
<<<<<<< HEAD
        accumulator = 0
        curr = self._first
        while curr is not None:
            accumulator += curr.item.estimated_length
        
        if accumulator <= time_awake:
            return True
        else:
            return False
=======

        return accumulator <= time_awake:
>>>>>>> dc5ee2a20cd52ab80b0d16da667b08825c09c5bb

    def pick_time(self, event: Any) -> int:
        """Picks a time for an event to occur in (for asynchronous events)
        """
        length = event.estimate_length
        curr = self._first.next
        prev = self._first
        while curr is not None:
            if (curr.item.start - prev.item.end) > length:
                return random.randint(prev.item.end, curr.item.start)
            else:
                prev, curr = curr, curr.next
<<<<<<< HEAD

=======
>>>>>>> dc5ee2a20cd52ab80b0d16da667b08825c09c5bb

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
                    time = self.pick_time(curr.item)
                    curr.item.start = time
                    curr = curr.next
                else:
                    curr = curr.next

    def recreation_check(self, recreation: Any) -> bool:
        """Checks if a certain recreational event is already in the day (helper function for insert_recreation)
        """
        curr = self._first
        while curr is not None:
            if curr.item.title == recreation.title:
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
        self.sort_day()
        curr = self._first
        prev = None
        while curr is not None and prev is not None:
            if (curr.item.start - prev.item.end) > 1:
                self.insert_recreation(random.choice(user.hobbies), user, prev.item, curr.item)
                prev, curr = curr, curr.next
            else:
                prev, curr = curr, curr.next

    def sort_day(self):
        """
        Sorts linked list in terms of time.
        """
        link_to_list = self.to_list()
        link_to_list.sort(key=lambda e, e.item.start)

        self._first = Node(link_to_list[0])
        curr = self._first
        for node in link_to_list[1:]:
            curr.next = node
            curr = node

        return self._first
    
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

