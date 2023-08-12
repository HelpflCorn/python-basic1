# Task 2

# Implement 2 classes, the first one is the Boss and the second one is the Worker.

# Worker has a property 'boss', and its value must be an instance of Boss.

# You can reassign this value, but you should check whether the new value is Boss. 
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. 
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
# use getters and setters instead!

import sys
from random import randint


class Boss:
    def __init__(self, name: str, company: str):
        self.id = randint(1, sys.maxsize)
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)

    def get_workers(self):
        return self._workers

class Worker:
    def __init__(self, name: str, company: str, boss: Boss):
        self.id = randint(1, sys.maxsize)
        self.name = name
        self.company = company
        self._boss = None 
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss is not None:
                self._boss._workers.remove(self) 
            self._boss = new_boss
            new_boss.add_worker(self)


boss1 = Boss("Petro", "RzyshivDynamics")
boss2 = Boss("Vasyl", "MicroZmerynka")
worker1 = Worker("Mykhailo", "RzyshivDynamics", boss1)
worker2 = Worker("MrFedir", "MicroZmerynka", boss2)

print("Initial workers for Boss 1:", [worker.name for worker in boss1.get_workers()])
print("Initial workers for Boss 2:", [worker.name for worker in boss2.get_workers()])
print(worker1.id)
print(worker2.id)

worker1.boss = boss2

print("Updated workers for Boss 1:", [worker.name for worker in boss1.get_workers()])
print("Updated workers for Boss 2:", [worker.name for worker in boss2.get_workers()])
