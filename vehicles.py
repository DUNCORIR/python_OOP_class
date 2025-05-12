#!/usr/bin/python3
"""Vehicle movement demo showing polymorphism."""


class Vehicle:
    """Base class for all vehicles."""

    def move(self):
        """Placeholder method to be overridden."""
        return "Moving..."


class Car(Vehicle):
    def move(self):
        return " Driving"


class Plane(Vehicle):
    def move(self):
        return " Flying"


class Boat(Vehicle):
    def move(self):
        return " Sailing"


def vehicle_demo():
    """Demonstrate polymorphism with different vehicles."""
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(v.move())


if __name__ == "__main__":
    vehicle_demo()
