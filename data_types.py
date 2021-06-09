""" Ideal Day - data_types.py
Contains classes and data structures for events in schedule
"""
# Constants
PRIORITIES = {"!", "!!", "!!!"}

class Event:
    """Python class representing an event/activity for a specific day
    
    Instance Attributes:
    - title: name of event
    - description: further details about the event
    - priority: how important this event for the day

    Representation invariants:
    - self.priority in PRIORITIES
    """
    title: str
    description: str
    priority: str

    def init(self) -> None:
        """initilize an event instance"""

print('moose')

