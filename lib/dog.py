class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name, breed="Mutt"):
        self._name = None
        self._breed = None  # Using None as a placeholder until setter validates the breed
        self.name = name  # Using the property setter for validation
        self.breed = breed  # Using the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            print("Breed must be in the list of approved breeds.")
        else:
            self._breed = value

# Example usage:
dog1 = Dog("Buddy", "Pug")
print(dog1.name)  # Output: Buddy
print(dog1.breed)  # Output: Pug

dog2 = Dog("Rex", "Labrador")  # Invalid breed, should print an error message
dog2.name = "Rex"  # Valid name, should set the name
dog2.breed = "Beagle"  # Valid breed, should set the breed
print(dog2.name)  # Output: Rex
print(dog2.breed)  # Output: Beagle
