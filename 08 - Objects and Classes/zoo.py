class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name

        self.__animals = 0

        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)

        elif species == "fish":
            self.fishes.append(name)

        elif species == "bird":
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species_type):

        if species_type == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n Total animals: {self.__animals}"

        elif species_type == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n Total animals: {self.__animals}"

        elif species_type == "bird":

            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n Total animals: {self.__animals}"




name_of_zoo = input()
n = int(input())

zoo = Zoo(name_of_zoo)

for _ in range(n):
    command = input().split()
    zoo.add_animal(command[0], command[1])



show_species = input()
print(zoo.get_info(show_species))

