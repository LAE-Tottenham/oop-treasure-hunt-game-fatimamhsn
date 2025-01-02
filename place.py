class Place():
    def __init__(self, given_name, locked=False, key = False, items=None, enemies = None):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.locked = locked
        self.next_places = []
        self.items = []
        self.items = items if items else []
        self.enemies = enemies if enemies else []
        self.description = ''
        self.key = key
        # add more atributes as needed

    def describe(self, description):
        self.description = description

        if self.locked == True:
            if self.key == False:
                print('This place is locked. You need a key to enter. ')
            else:
                print(f'You are now in {self.name}. {self.description}')
        else:
            print(f'You are now in {self.name}. {self.description}')
    
    def add_enemies(self, enemies_instance):
        self.enemies_append(enemies_instance)


    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.items.append(item_instance)
        

    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            # remember that next_places is a list of Place instances hence why we can use place.name
            print(place.name)

    def showstats(self):
        print(f"Items here: {', '.join(self.items)}")

    # add more methods as needed


forest =  Place( 'Enchanted Forest', True, True)
forest.describe('this forest is very big and scary, there are many enemies')
forest.add_item(hammer.name)
forest.add_item(lock.name)
forest.showstats()