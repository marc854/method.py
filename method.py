# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power        # Protected attribute
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")

    def use_power(self):
        print(f"{self.name} uses their power: {self._power}!")

# Subclass with overridden method
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the skies at {self.flight_speed} mph using {self._power}!")

# Creating objects
hero1 = Superhero("Shadow Knight", "Invisibility", "Gotham")
hero2 = FlyingSuperhero("Sky Blaze", "Flame Wings", "Metropolis", 500)

# Test them
hero1.introduce()
hero1.use_power()
hero2.introduce()
hero2.use_power()
