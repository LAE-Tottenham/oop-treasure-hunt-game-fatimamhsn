class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.rucksack_max_weight = 50
        self.rucksack = []
        # add more atributes as needed

    def calculate_rucksack_size(self):
        size = len(self.rucksack)
        vacancies = 50-size
        print(f'You have {size} items in your rucksack and {vacancies} spaces left')

    def add_item(self, item_instance):
        if self.calculate_rucksack_size() > self.rucksack_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your rucksack is full...")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        # add more code here

    # add more methods as needed
