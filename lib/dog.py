#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Example usage:

# Creating a Dog instance with only name
my_dog = Dog("Buddy")
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Mutt

# Creating a Dog instance with name and breed
other_dog = Dog("Max", "Labrador")
print(other_dog.name)   # Output: Max
print(other_dog.breed)  # Output: Labrador

