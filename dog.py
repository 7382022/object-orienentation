class Dog:
    species = "Dog"

    def __init__(self,name,age):
        self.name = name
        self.age = age

Marsh = Dog("Marsh",5)
Chase = Dog ("Chase",7)


print("Marsh is a {}".format(Marsh.species))
print("Chase is a {}".format(Chase.species))

print("{} is {} years old".format(Marsh.name,Marsh.age))
print("{} is {} years old".format(Chase.name,Chase.age))