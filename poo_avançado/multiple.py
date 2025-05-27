class Animal:
    @property
    def capacities(self):
        return ("sleep", "eat", "drink")


class Man(Animal):
    @property
    def capacities(self):
        return super().capacities + ("love", "talk", "study")


class Spider(Animal):
    @property
    def capacities(self):
        return super().capacities + ("web making", "wall walking")


class SpiderMan(Spider, Man):
    @property
    def capacities(self):
        return super().capacities + \
            ("Beat up bad guys", "shoot web inbetween buildings")


if __name__ == "__main__":
    john = Man()
    print(f"John: {john.capacities}")

    spider = Spider()
    print(f"Spider: {spider.capacities}")

    peter = SpiderMan()
    print(f"Peter: {peter.capacities}")
