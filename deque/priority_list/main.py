from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority=False) -> None:
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority
    def __str__(self) -> str:
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

class TaskList(object):
    def __init__(self) -> None:
        self.priorityList = deque()

    def adding(self, item:Task) -> None:
        if item.hasPriority:
            self.priorityList.appendleft(item)
        else:
            self.priorityList.append(item)

    def completing(self) -> None:
        return self.priorityList.popleft()

    def print(self) -> None:
        for task in self.priorityList:
            print(task.taskDesc)

def main():
    tasks = TaskList()
    tasks.adding(Task("cleaning"))
    tasks.adding(Task("cooking"))
    tasks.adding(Task("washing clothes"))
    tasks.print()
    tasks.adding(Task("work", True))
    tasks.adding(Task("take kids to school", True))
    tasks.adding(Task("pick up kids"))
    tasks.print()
    for i in range(3):
        task = tasks.completing()
        print("Completed task {0}".format(task.taskDesc))
    print("Remaining tasks")
    tasks.print()
    

if __name__ == "__main__":
    main()