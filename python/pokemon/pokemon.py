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
bulbasaur = Pokemon('Bulbasaur', 1, 64, ['grass', 'poison'], 45, 45, False, {moves.tackle: 1, moves.vine_whip: 13, moves.razor_leaf: 27, moves.solar_beam: 48})

ivysaur = Pokemon('Ivysaur', 16, 142, ['grass', 'poison'], 60, 60, False, {moves.tackle: 1, moves.vine_whip: 13, moves.razor_leaf: 27, moves.solar_beam: 48})

ivysaur = Pokemon('Venusaur', 32, 236, ['grass', 'poison'], 80, 80, False, {moves.tackle: 1, moves.vine_whip: 13, moves.razor_leaf: 27, moves.solar_beam: 48})

charmander = Pokemon('Charmander', 1, 62, ['fire'], 39, 39, False, {moves.scratch: 1, moves.ember: 9, moves.rage: 22, moves.slash: 30, moves.flamethrower: 38, fire_spin: 46})

charmeleon = Pokemon('Charmeleon', 16, 142, ['fire'], 58, 58, False, {moves.scratch: 1, moves.ember: 9, moves.rage: 22, moves.slash: 30, moves.flamethrower: 38, fire_spin: 46})

charizard = Pokemon('Charizard', 36, 240, ['fire'], 78, 78, False, {moves.scratch: 1, moves.ember: 9, moves.rage: 22, moves.slash: 30, moves.flamethrower: 38, fire_spin: 46})

squirtle = Pokemon('Squirtle', 1, 63, ['water'], 44, 44, False, {moves.tackle: 1, moves.bubble: 8, moves.water_gun: 15, moves.bite: 22, moves.skull_bash: 35, hydro_pump: 42})

wartortle = Pokemon('Wartotle', 16, 142, ['water'], 59, 59, False, {moves.tackle: 1, moves.bubble: 8, moves.water_gun: 15, moves.bite: 22, moves.skull_bash: 35, hydro_pump: 42})

blastoise = Pokemon('Blastoise', 79, 239, ['water'], 79, 79, False, {moves.tackle: 1, moves.bubble: 8, moves.water_gun: 15, moves.bite: 22, moves.skull_bash: 35, hydro_pump: 42})

pikachu = Pokemon('Pikachu', 1, 112, ['electric'], 35, 35, False, {moves.thunder_shock: 1, moves.quick_attack: 16, moves.swift: 26, moves.thunder: 43})

raichu = Pokemon('Raichu', 1, 218, ['electric'], 60, 60, False, {moves.thunder_shock: 1, moves.quick_attack: 16, moves.swift: 26, moves.thunder: 43})

snorlax = Pokemon('Snorlax', 1, 189, ['normal'], 160, 160, False, {moves.headbutt: 1, moves.body_slam: 35, moves.double_edge: 48, moves.hyper_beam: 150})

magikarp = Pokemon('Magikarp', 1, 40, ['water'], 20, 20, False, {moves.splash: 1, moves.tackle: 15})

gyarados = Pokemon('Gyarados', 20, 95, ['water', 'flying'], 20, 20, False, {moves.bite: 1, moves.hydro_pump: 1, moves.bite: 60, moves.hyper_beam: 150})