from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, description, deadline=None):
        self.tasks.append(Task(description, deadline))

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        # Possível IndexError
        return [task for task in self.tasks
                if task.description == description][0]

    def __str__(self):
        return f"{self.name} ({len(self.pending())} pending task(s))"


class Task:
    def __init__(self, description, deadline=None):
        self.description = description
        self.done = False
        self.creation = datetime.now()
        self.deadline = deadline

    def conclude(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append("(Done)")
        elif self.deadline:
            if datetime.now() > self.deadline:
                status.append("(Late)")
            else:
                days = (self.deadline - datetime.now()).days
                status.append(f"(Late in {days} days)")

        return f"{self.description} " + " ".join(status)


def main():
    house = Project("House work")
    house.add("Iron clothes", datetime.now())
    house.add("Do dishes")
    print(house)

    house.search("Do dishes").conclude()
    for task in house:
        print(f"- {task}")
    print(house)

    market = Project("Supermarket")
    market.add("Dry fruits")
    market.add("Meat")
    market.add("Tomato", datetime.now() + timedelta(days=3, seconds=1))
    print(market)

    buy_meat = market.search("Meat")
    buy_meat.conclude()
    for task in market:
        print(f"- {task}")
    print(market)


if __name__ == "__main__":
    main()
