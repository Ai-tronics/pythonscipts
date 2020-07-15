import items

class Player:
    
    def __init__(self):
        self.inventory = [items.Rock(),items.Dagger(),'Gold(5)','Crusty Bread']

    def print_inventory(self):
        print("Inventory:")
        for items in self.inventory:
            print('* ' + str(items))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))
        
    
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for weapons in self.inventory:
          try:
             if weapons.damage > max_damage:
               best_weapon = weapons
               max_damage = weapons.damage
          except AttributeError:
                pass 
        return best_weapon
