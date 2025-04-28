class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner musr be an instance of Owner class.")
        self.owner = owner

        Pet.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name
        pass

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    pass