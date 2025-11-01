from pakuri import *

class Pakudex:

    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.my_pakudex = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if len(self.my_pakudex) == 0:
            return None
        else:
            species_array = []
            for each_species in self.my_pakudex:
                species_array.append(each_species.get_species())
            return species_array

    def get_stats(self, species):
        for each_species in self.my_pakudex:
            if each_species.get_species() == species:
                return [each_species.get_attack(), each_species.get_defense(), each_species.get_speed()]
        return None

    def sort_pakuri(self):
        self.my_pakudex.sort()

    def add_pakuri(self, species):
        if self.size == self.capacity:
            return False

        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                return False

        self.my_pakudex.append(Pakuri(species))
        self.size += 1
        return True

    def evolve_species(self, species):
        for each_species in self.my_pakudex:
            if each_species.get_species() == species:
                each_species.evolve()
                return True
        return False

