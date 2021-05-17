"""day class"""
import block
import random

task_bank = block.create_task_bank()


class Day:
    """represents a day of tasks"""
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.hard_tasks = []
        self.soft_tasks = []
        self.tasks = []
        self.task_slots = []
        self.open_time = self.end - self.start
        self.used_time_slots = {}
        self.goals = []

    def add_task(self, task) -> None:
        """adds task to self.tasks"""
        if task.time is None:
            self.soft_tasks.append(task)
        else:
            self.hard_tasks.append(task)
        self.tasks.append(task)

    def add_goal(self, goal) -> None:
        """adds goal to self.goals"""
        self.goals.append(goal)

    def put_in_slot(self, task, time) -> None:
        """chooses sepcific time for an event to take place"""
        self.task_slots.append((task, time))
        task.put_in_slot(time)

    def order_day(self) -> None:
        """order tasks in day"""
        self.soft_tasks.sort(key=lambda x: x.priority, reverse=True)

        for task in self.hard_tasks:
            self.put_in_slot(task, task.time)

        time = self.start
        for task in self.soft_tasks:
            self.put_in_slot(task, time)
            time += task.estimated_length

    def assess_day(self) -> None:
        """make sure there all goals in self.goals have a task in self.tasks
         with that category. If not, adds a task from task_bank in that category.
        """
        for goal in self.goals:
            if not [x for x in self.tasks if x.category == goal]:
                task_options = task_bank[goal]
                this_task = random.choice(task_options)
                self.add_task(this_task)

    def check_overlap(self) -> bool:
        """check if new task slot overlaps with a previous one"""
        pass

    def display_day(self) -> None:
        """displays day"""
        for task in self.tasks:
            task.display_task()
