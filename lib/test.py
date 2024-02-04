class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name
        self._age = 0
        pass

    def get_age(self):
        print("Retrieving age")
        return self._age
    

    def set_age(self, age):
        print(f"Setting age to { age }")
        self._age = age
    
    age = property(get_age, set_age)

guido = Human("Guido")
print(guido.age)
print(guido.species)

