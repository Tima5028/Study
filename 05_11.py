#
#
# class Dog:
#     species="Just a Dog"
#     legs_number=4
#     def __init__(self, name, breed, weight, hungry, age):
#         self.name=name
#         self.breed = breed
#         self.weight = weight
#         self.hungry = hungry
#         self.age=age
#
#
#     def say_hi (self, sound):
#         print(sound)
#
#
#     def feed(self, meal, meal_mass):
#         self.weight+=meal_mass
#         self.hungry="not hungry"
#
#     # def description(self):
#     #     return f"{self.name} is {self.age} years old"
#
#
#     # def __str__(self):
#     #     return f"{self.name} is {self.age} years old"
#
#     def __repr__(self):
#         return f"{self.name} is {self.age} years old"
#
#
# sharik = Dog("Sharik", "terier", 10, "hungry", 8)
# bobik = Dog("Bobik", "buldog", 15, "hungry", 7)
#
#
# sharik

# sharik.say_hi("wof!"*3)
# sharik.feed("Beef", 0.2)

# print(sharik.species)
# print(sharik.weight)
# print(bobik.breed)
# print(sharik.breed)
# print(f"thank you! {meal} was amazing!")


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.speak())
print(jim.speak("Wof!"))

print(isinstance(miles, Dachshund))
print(jim.age)

