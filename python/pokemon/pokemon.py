#file to store all of the pokemon using imported Pokemon class

#class for individual pokemon and their characteristics
class Pokemon:
    #constructor for pokemon attributes
    def __init__(self, name, level, xp, poke_type, max_health, current_health, ko, attacks):
        self.name = name
        self.level = level
        self.xp = xp
        self.poke_type = poke_type
        self.max_health = int(max_health * (1 + (self.level-1)//50))
        self.current_health = current_health
        self.ko = ko
        self.attacks = attacks


    #method for health lost from attack, with health bottomed out at 0 hp
    def lose_health(self, damage):
        if 0 <= self.current_health - damage:
            self.current_health = self.current_health - damage
            print('{name} now has {current_health}hp.'.format(name = self.name, current_health = self.current_health))
        else:
            self.current_health = 0
            self.ko_status()


    #method for health gained from potion, with health max````ed out at the max health
    def gain_health(self, potion_hp):
        if self.max_health >= self.current_health + potion_hp:
            self.current_health = self.current_health + potion_hp
        else:
            self.current_health = self.max_health
        print('{name} now has {current_health}hp.'.format(name = self.name, current_health = self.current_health))


    #method for ko status
    def ko_status(self):
        if self.current_health == 0:
            self.ko = True
            print("{name} is knocked out and can no longer battle.".format(name = self.name))
        else: 
            self.ko = False


    #method for damage delivered to opponent with attack
    def attack(self, attack_hp, opponent_pokemon):
        damage = (attack_hp * (1 + (self.level - 1)//50) * attack_multiple[self.poke_type][opponent_pokemon.poke_type])//1
        print("{pokemon_name}'s attack did {damage} damage to {opponent_pokemon}.".format(pokemon_name = self.name, damage = damage, opponent_pokemon = opponent_pokemon.name))
        return opponent_pokemon.lose_health(damage)

        
#dictionary of the attack multiplier for each of the pokemon types.
attack_multiple = {'fire': {'water': 0.5, 'grass': 2}, 'water': {'fire': 2, 'grass': 0.5}, 'grass': {'water': 2, 'fire': 0.5}}


#pokemon objects that include
charmander = Pokemon('Charmander', 30, 0, 'fire', 130, 130, False, {'fire breath': 10, 'scratch': 7, 'flamethrower': 15})

squirtle = Pokemon('Squirtle', 69, 0, 'water', 140, 140, False, {'water hose': 10, 'tackle': 7, 'hydroblast': 15})

bulbassaur = Pokemon('Bulbassaur', 25, 0, 'grass', 150, 150, False, {'vine whip': 10, 'tackle': 7, 'power whip': 15})

pikachu = Pokemon('Pikachu', 10, 10, 'electric', 100, 80, False, {'lightning bolt'})
