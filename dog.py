from models.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def to_string(self):
        return {"name": self.name,
                "age": self.age,
                "leg_count": self.leg_count
                }

    @classmethod
    def communicate(cls):
        return "I am dog, so I can bark"

    @staticmethod
    def can_fly():
        return False