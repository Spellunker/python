from datetime import datetime


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add(self, description):
        self.tasks.append(Task(description))

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        # Possível IndexError
        return [task for task in self.tasks
                if task.description == description][0]

    def __str__(self):
        return f"{self.name} ({len(self.pending())} pending task(s))"


class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.creation = datetime.now()

    def conclude(self):
        self.done = True

    def __str__(self):
        return self.description + ("(Done)" if self.done else "")


def main():
    house = Project("House work")
    house.add("Iron clothes")
    house.add("Do dishes")
    print(house)

    house.search("Do dishes").conclude()
    for task in house.tasks:
        print(f"- {task}")
    print(house)

    market = Project("Supermarket")
    market.add("Dry fruits")
    market.add("Meat")
    market.add("Tomato")
    print(market)

    buy_meat = market.search("Meat")
    buy_meat.conclude()
    for task in market.tasks:
        print(f"- {task}")
    print(market)


if __name__ == "__main__":
    main()
