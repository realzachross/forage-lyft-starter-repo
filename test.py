from abc import abstractmethod, ABC


class Animal:
    def speak(self): print('sound')


class Dog(Animal):
    def __init__(self, words):
        self.words = words
        self.sound = "bark bark"

    """def speak(self):
        print(self.sound)
        print(self.words)"""


dog = Dog("hello, i'm marco")
dog.speak()
