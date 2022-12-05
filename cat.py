from models.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def to_string(self):
        return {"name": self.name,
                "age": self.age,
                "leg_count": self.leg_count
                }

    @classmethod
    def communicate(cls):
        return "I am cat, so I can meow"

    @staticmethod
    def can_fly():
        return False
