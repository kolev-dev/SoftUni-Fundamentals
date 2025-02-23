class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name

        self.__animals = 0

        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self, species, name):
        if species == "mammals":
            self.mammals.append(name)

        elif species == "fish":
            self.fishes.append(name)

        elif species == "bird":
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species_type):

        if species_type == "mammals":

            return f"{self.mammals} in {self.zoo_name}: {", ".join(self.mammals)} Total animals: {self.__animals}"

        elif species_type == "fish":

            return f"{self.fishes} in {self.zoo_name}: {", ".join(self.fishes)} Total animals: {self.__animals}"

        elif species_type == "bird":

            return f"{self.birds} in {self.zoo_name}: {", ".join(self.birds)} Total animals: {self.__animals}"




name_of_zoo = input()
n = int(input())

zoo = Zoo(name_of_zoo)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)



show_species = input()
print(zoo.get_info(show_species))

