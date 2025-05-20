class Carro:
    def __init__(self, max_speed=200):
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, delta=5):
        if self.current_speed <= (self.max_speed - delta):
            self.current_speed += delta
        else:
            self.current_speed = self.max_speed
        return self.current_speed

    def brake(self, delta=5):
        if self.current_speed >= (0 + delta):
            self.current_speed -= delta
        else:
            self.current_speed = 0
        return self.current_speed


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        # 178 + 8 = 180
        print(c1.accelerate(8))

    for _ in range(10):
        # 3 - 20 = 0
        print(c1.brake(delta=20))
