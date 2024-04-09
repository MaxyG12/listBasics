print("Greeting generator")
print()
greetings = ["Hello", "Hi", "Hey", "Howdy", "Hola", "Bonjour"]
import random
greeting = random.choice(greetings)
name = input("What is your name? ")
print(f"{greeting}, {name}!")


