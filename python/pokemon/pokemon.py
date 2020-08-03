#file to store all of the pokemon using imported Pokemon class

#imported moves library
import moves, random

#class for individual pokemon and their characteristics
class Pokemon:
    #constructor for pokemon attributes
    def __init__(self, name, level, base_xp, poke_type, max_health, current_health, ko, all_moves):
        self.name = name
        self.level = level
        self.base_xp = base_xp
        self.poke_type = poke_type
        self.max_health = int(max_health * (1 + (self.level-1)//50))
        self.current_health = current_health
        self.ko = ko
        self.all_moves = all_moves
        self.available_moves = []
        if isinstance(self.all_moves[1], list):
            self.available_moves += self.all_moves[1]
        else:
            self.available_moves = [self.all_moves[1]]


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


    #method for damage based on attack selection, type multiplier, and accuracy and this is delivered to opponent pokemon with attack
    def attack(self, selected_attack, opponent_pokemon):
        #check if the selected attack is in pokemon's available moves
        if selected_attack in self.available_moves:
            #use move accuracy to determine if the pokemon landed the attack
            rand_number = random.randint(0, 99)
            if selected_attack.accuracy > rand_number:
                attack_power = selected_attack.power
                attack_multiplier = self.attack_type(opponent_pokemon)
                damage = (attack_power * (1 + (self.level - 1)//50) * attack_multiplier)//1
                print("{pokemon_name}'s attack did {damage} damage to {opponent_pokemon}.".format(pokemon_name = self.name, damage = damage, opponent_pokemon = opponent_pokemon.name))
                return opponent_pokemon.lose_health(damage)
            else:
                print("{pokemon_name}'s attack missed!".format(pokemon_name = self.name))



    #method to add move to available_moves if space, otherwise remove move existing to add move or don't add move
    def add_move(self):
        if self.level in self.all_moves.keys():
            added_move = self.all_moves[self.level]
            #automatically adds the new move to the available moves if there is space
            if len(self.available_moves) < 4:
                self.available_moves.append(added_move)
                print('{0} was added to {1}\'s available moves.'.format(added_move.name, self.name))
            #if there is not enough space, asks user if they want to remove move to add the added_move
            else:
                remove_to_add = input('\nThere is not enough space in {0}\'s available moves. Would you like to remove one of your current moves to make room for {1}?\nYes [y] or No [n]: '.format(self.name, added_move.name)) 
                while remove_to_add not in ['y', 'n']:
                    remove_to_add = input('Would you like to remove one of your current moves to make room for {1}?\nYes [y] or No [n]: '.format(added_move.name))
                #removes one move from available moves and adds the added_move
                if remove_to_add == 'y':
                    removed_move = int(input('What move would you like to remove?\n{0} [1], {1} [2], {2} [3], {3} [4]: '.format(self.available_moves[0], self.available_moves[1], self.available_moves[2], self.available_moves[3])))
                    while removed_move not in [0, 1, 2, 3]:
                        removed_move = int(input('What move would you like to remove?\n{0} [1], {1} [2], {2} [3], {3} [4]: '.format(self.available_moves[0], self.available_moves[1], self.available_moves[2], self.available_moves[3])))
                    print('You removed {0} and added {1} to {2}\'s available moves.'.format(self.available_moves[removed_move].name, added_move.name, self.name))
                    self.available_moves[removed_move] = added_move
                #does not add the move to the pokemon's available moves
                else:
                    print('{0} was not added to {1}\'s available moves.'.format(added_move.name, self.name))


    #helper method for determining best type to attack with
    def attack_type(self, opponent_pokemon):
        max_multiplier = 0
        for type_self in self.poke_type:
            for type_opp in opponent_pokemon.poke_type:
                multiple = attack_multiple[type_self][type_opp]
                if multiple > max_multiplier:
                    max_multiplier = multiple
                else:
                    continue
        return max_multiplier



#dictionary of the attack multiplier for each of the pokemon types.
attack_multiple = {
    'grass': {'grass': 0.5, 'poison': 2.0, 'fire': 0.5, 'water': 2.0, 'electric': 0.5, 'normal': 1.0, 'flying': 0.5}, 
    'poison': {'grass': 2.0, 'poison': 0.5, 'fire': 1.0, 'water': 1.0, 'electric': 1.0, 'normal': 1.0, 'flying': 1.0}, 
    'fire': {'grass': 2.0, 'poison': 1.0, 'fire': 0.5, 'water': 0.5, 'electric': 1.0, 'normal': 1.0, 'flying': 1.0}, 
    'water': {'grass': 0.5, 'poison': 1.0, 'fire': 2.0, 'water': 0.5, 'electric': 1.0, 'normal': 1.0, 'flying': 1.0}, 
    'electric': {'grass': 0.5, 'poison': 1.0, 'fire': 1.0, 'water': 2.0, 'electric': 0.5, 'normal': 1.0, 'flying': 2.0}, 
    'normal': {'grass': 1.0, 'poison': 1.0, 'fire': 1.0, 'water': 1.0, 'electric': 1.0, 'normal': 1.0, 'flying': 1.0}, 
    'flying': {'grass': 2.0, 'poison': 1.0, 'fire': 1.0, 'water': 1.0, 'electric': 0.5, 'normal': 1.0, 'flying': 1.0}
    }

        
#list of default pokemon
bulbasaur = Pokemon('Bulbasaur', 1, 64, ['grass', 'poison'], 45, 45, False, {1: moves.tackle, 13: moves.vine_whip, 27: moves.razor_leaf, 48: moves.solar_beam})

ivysaur = Pokemon('Ivysaur', 16, 142, ['grass', 'poison'], 60, 60, False, {1: moves.tackle, 13: moves.vine_whip, 27: moves.razor_leaf, 48: moves.solar_beam})

venusaur = Pokemon('Venusaur', 32, 236, ['grass', 'poison'], 80, 80, False, {1: moves.tackle, 13: moves.vine_whip, 27: moves.razor_leaf, 48: moves.solar_beam})

charmander = Pokemon('Charmander', 1, 62, ['fire'], 39, 39, False, {1: moves.scratch, 9: moves.ember, 22: moves.rage, 30: moves.slash, 38: moves.flamethrower, 46: moves.fire_spin})

charmeleon = Pokemon('Charmeleon', 16, 142, ['fire'], 58, 58, False, {1: moves.scratch, 9: moves.ember, 22: moves.rage, 30: moves.slash, 38: moves.flamethrower, 46: moves.fire_spin})

charizard = Pokemon('Charizard', 36, 240, ['fire'], 78, 78, False, {1: moves.scratch, 9: moves.ember, 22: moves.rage, 30: moves.slash, 38: moves.flamethrower, 46: moves.fire_spin})

squirtle = Pokemon('Squirtle', 1, 63, ['water'], 44, 44, False, {1: moves.tackle, 8: moves.bubble, 15: moves.water_gun, 22: moves.bite, 35: moves.skull_bash, 42: moves.hydro_pump})

wartortle = Pokemon('Wartotle', 16, 142, ['water'], 59, 59, False, {1: moves.tackle, 8: moves.bubble, 15: moves.water_gun, 22: moves.bite, 35: moves.skull_bash, 42: moves.hydro_pump})

blastoise = Pokemon('Blastoise', 79, 239, ['water'], 79, 79, False, {1: moves.tackle, 8: moves.bubble, 15: moves.water_gun, 22: moves.bite, 35: moves.skull_bash, 42: moves.hydro_pump})

pikachu = Pokemon('Pikachu', 1, 112, ['electric'], 35, 35, False, {1: moves.thunder_shock, 16: moves.quick_attack, 26: moves.swift, 43: moves.thunder})

raichu = Pokemon('Raichu', 1, 218, ['electric'], 60, 60, False, {1: moves.thunder_shock, 16: moves.quick_attack, 26: moves.swift, 43: moves.thunder})

snorlax = Pokemon('Snorlax', 1, 189, ['normal'], 160, 160, False, {1: moves.headbutt, 35: moves.body_slam, 48: moves.double_edge, 56: moves.hyper_beam})

magikarp = Pokemon('Magikarp', 1, 40, ['water'], 20, 20, False, {1: moves.splash, 15: moves.tackle})

gyarados = Pokemon('Gyarados', 20, 95, ['water', 'flying'], 20, 20, False, {1: [moves.bite, moves.hydro_pump], 52: moves.hyper_beam})




charizard.attack(moves.scratch, pikachu)