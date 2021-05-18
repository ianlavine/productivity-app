"""event class"""


class Event:
    """event"""
    def __init__(self, title, desc="", time=None, pri=2, est=1, category='work', start=None, end=None) -> None:
        self.title = title
        self.description = desc
        self.time = time
        self.priority = pri
        self.estimated_length = est
        self.start = None
        self.end = None
        self.category = category

    def put_in_slot(self, time) -> None:
        """chooses sepcific time for an event to take place"""
        self.start = time
        self.end = self.estimated_length + self.start

    def display_task(self) -> None:
        """displays task"""
        print(self.title + ": from " + str(self.start) + " to " + str(self.end))
        # blank line


def create_task_bank() -> dict:
    """creates dict of reccomendable tasks sorted by their category"""
    pass
