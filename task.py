tasks = []

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.id = len(tasks) + 1

        tasks.append(self)

    def remove(self):
        found = False

        for task in tasks:
            if task.id == self.id:
                found = True
                continue

            if found:
                task.id -= 1

        tasks.remove(self)
        del self
