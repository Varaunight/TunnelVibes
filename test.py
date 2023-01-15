class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("John", 30), Person("Jane", 25), Person("Bob", 35)]

# Use filter to find the Person object with the name "John"
result = next(filter(lambda x: x.name == "John", people), None)
print(result)
