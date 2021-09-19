class Animal:
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        print('woof')

class Cat(Animal):
    def voice(self):
        print('meow')

class Fox(Animal):
    def voice(self):
        print('?????')

dog = Dog()
dog.voice()

cat = Cat()
cat.voice()

fox = Fox()
fox.voice()