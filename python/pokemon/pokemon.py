#file to store all of the pokemon using imported Pokemon class

#imported moves library
import moves, random

#class for individual pokemon and their characteristics
class Pokemon:
    #constructor for pokemon attributes
    def __init__(self, name, poke_type, max_health, attack_power, defense_power, speed, exp_yield, all_moves, evolve_poke, level = 1):
        self.name = name
        self.poke_type = poke_type
        self.ko = False
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.speed = speed
        self.exp_yield = exp_yield
        self.all_moves = all_moves
        self.evolve_poke = evolve_poke
        self.level = level
        self.max_health = int(max_health * (1 + (self.level-1)//50))
        self.total_exp = level ** 3
        self.available_moves = []
        for key, value in self.all_moves.items():
            if self.level >= key:
                self.available_moves.append(value)

    #lists available moves
    def print_avail_moves(self):
        string = ''
        for i, move in enumerate(self.available_moves, 1):
            string += str(i) + ': ' + move.name + '\n'
        return string


    #method for health lost from attack, with health bottomed out at 0 hp
    def lose_health(self, damage):
        if 0 <= self.current_health - damage:
            self.current_health -= damage
            print('{0} now has {1}hp.'.format(self.name, self.current_health))
        else:
            self.current_health = 0
            self.ko_status()


    #method for health gained from potion, with health max````ed out at the max health
    def gain_health(self, potion_hp):
        if potion_hp == 'full' or self.max_health < self.current_health + potion_hp:
            gain = self.max_health - self.current_health
            self.current_health = self.max_health
        else:
            gain = potion_hp
            self.current_health += potion_hp
        print('{0} gained {1} hp and now has {2} hp.'.format(self.name, gain, self.current_health))


    #method for ko status
    def ko_status(self):
        if self.current_health == 0:
            self.ko = True
            print("{0} is knocked out and can no longer battle.".format(self.name))
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
                attack_multiplier = self.type_multiplier(opponent_pokemon)
                damage = int(((self.level * 2/5 + 2) * attack_power//50 + 2) * attack_multiplier)
                print("{0}'s attack did {1} damage to {2}.".format(self.name, damage, opponent_pokemon.name))
                return opponent_pokemon.lose_health(damage)
            else:
                print("{0}'s attack missed!".format(self.name))


    #method to add move to available_moves if space, otherwise remove move existing to add move or don't add move
    def add_move(self):
        if self.level in self.all_moves:
            added_move = self.all_moves[self.level]
            
            #automatically adds the new move to the available moves if there is space
            if len(self.available_moves) < 4:
                self.available_moves.append(added_move)
                print('{0} learned the move {1}!'.format(self.name, added_move.name))
            
            #if there is not enough space, asks user if they want to remove move to add the added_move
            else:
                remove_to_add = input('\nThere is not enough space in {0}\'s available moves. Would you like to remove one of your current moves to make room for {1}?\nYes [y] or No [n]: '.format(self.name, added_move.name)) 
                while remove_to_add not in ['y', 'n']:
                    remove_to_add = input('Would you like to remove one of your current moves to make room for {1}?\nYes [y] or No [n]: '.format(added_move.name))
                
                #removes one move from available moves and adds the added_move
                if remove_to_add == 'y':
                    removed_move_idx = int(input('What move would you like to remove?\n{0}: '.format(self.print_avail_moves()))) - 1
                    while removed_move_idx not in range(3):
                        removed_move_idx = int(input('What move would you like to remove?\n{0}: '.format(self.print_avail_moves))) - 1
                    print('{0} forgot the move {1} and learned the move {2}.'.format(self.name, self.available_moves[removed_move_idx].name, added_move.name))
                    self.available_moves[removed_move_idx] = added_move
                
                #does not add the move to the pokemon's available moves
                else:
                    print('{0} was not added to {1}\'s available moves.'.format(added_move.name, self.name))


    #method for gaining exp after opponent pokemon faints
    def gain_exp(self, opponent_pokemon):
        #experience gained equation
        gained_exp = opponent_pokemon.level * opponent_pokemon.exp
        self.total_exp += gained_exp
        print('{0} justed gained {1} experience points.'.format(self.name, gained_exp))
        
        #run level up method to check if pokemon gained enough experience to level up
        self.level_up()


    #method for leveling up
    def level_up(self):
        if self.total_exp > (self.level + 1) ** 3:
            self.level = self.total_exp ** 1/3
            print('{0} justed leved up to level {1}!'.format(self.name, self.level))
            
            #run evole method to check if pokemon evolved
            self.evolve()
            
            #run add_move method to check if pokemon can learn a new move
            self.add_move()


    #method to evolve pokemon at appropriate level
    def evolve(self):
        if self.level >= self.evolve_poke[0]['level']:
            evolved_poke = self.evolve_poke[0]
            input_to_evolve = input('{0} is trying to evolve into {1}! Do you want {0} to evolve?\nYes [y] or No [n]: '.format(self.name, evolved_poke['name']))
            if input_to_evolve == 'y':
                print('{0} is evolving into {1}!'.format(self.name, evolved_poke['name']))
                self.name = evolved_poke['name']
                self.max_health = evolved_poke['max_health']
                self.attack_power = evolved_poke['attack_power']
                self.defense_power = evolved_poke['defense_power']
                self.exp_yield = evolved_poke['exp_yield']
                self.evolve_poke.pop(0)
            elif input_to_evolve == 'n':
                print('{0} didn\'t evolve.'.format(self.name))
            else:
                self.evolve()
            

    #helper method for type multiplier during attack
    def type_multiplier(self, opponent_pokemon):
        multiplier = 1
        for type_self in self.poke_type:
            for type_opp in opponent_pokemon.poke_type:
                multiplier *= attack_multiple[type_self][type_opp]
        return multiplier






#bulbasaur class that 
class Bulbasaur(Pokemon):
    def __init__(self, level):
        super().__init__('Bulbasaur', ['grass', 'poison'], 45, 49, 49, 45, 64, {1: moves.tackle, 13: moves.vine_whip, 27: moves.razor_leaf, 48: moves.solar_beam}, [{'name': 'Ivysaur', 'level': 16, 'max_health': 60, 'attack_power': 62, 'defense_power': 63, 'speed': 60, 'exp_yield': 142}, {'name': 'Venusaur', 'level': 32, 'max_health': 80, 'attack_power': 82, 'defense_power': 83, 'speed': 80, 'exp_yield': 236}], level)


        self.level = level
        self.current_health = self.max_health
        self.ko = False


#charmander class that 
class Charmander(Pokemon):
    def __init__(self, level):
        super().__init__('Charmander', ['fire'], 39, 52, 43, 65, 62, {1: moves.scratch, 9: moves.ember, 22: moves.rage, 30: moves.slash, 38: moves.flamethrower, 46: moves.fire_spin}, [{'name': 'Charmeleon', 'level': 16, 'max_health': 58, 'attack_power': 64, 'defense_power': 58, 'speed': 80, 'exp_yield': 142}, {'name': 'Charizard', 'level': 36, 'max_health': 78, 'attack_power': 84, 'defense_power': 78, 'speed': 100,'exp_yield': 240}], level)
        
        self.level = level
        self.current_health = self.max_health
        self.ko = False


#squirtle class that 
class Squirtle(Pokemon):
    def __init__(self, level):
        super().__init__('Squitle', ['water'], 44, 48, 65, 43, 63, {1: moves.tackle, 8: moves.bubble, 15: moves.water_gun, 22: moves.bite, 35: moves.skull_bash, 42: moves.hydro_pump}, [{'name': 'Wartortle', 'level': 16, 'max_health': 59, 'attack_power': 63, 'defense_power': 80, 'speed': 58, 'exp_yield': 142}, {'name': 'Blastoise', 'level': 36, 'max_health': 79, 'attack_power': 83, 'defense_power': 100, 'speed': 78,'exp_yield': 239}], level)
        
        self.level = level
        self.current_health = self.max_health
        self.ko = False


#pikachu class that 
class Pikachu(Pokemon):
    def __init__(self, level):
        super().__init__('Pikachu', ['electric'], 35, 55, 40, 90, 112, {1: moves.thunder_shock, 16: moves.quick_attack, 26: moves.swift, 43: moves.thunder}, [{'name': 'Raichu', 'level': 32, 'max_health': 60, 'attack_power': 90, 'defense_power': 55, 'speed': 110, 'exp_yield': 218}], level)
        
        self.level = level
        self.current_health = self.max_health
        self.ko = False


#snorlax class that 
class Snorlax(Pokemon):
    def __init__(self, level):
        super().__init__('Snorlax', ['normal'], 160, 110, 65, 30, 189, {1: moves.headbutt, 35: moves.body_slam, 48: moves.double_edge, 56: moves.hyper_beam}, [], level)
        
        self.level = level
        self.current_health = self.max_health
        self.ko = False


#magikarp class that 
class Magikarp(Pokemon):
    def __init__(self, level):
        super().__init__('Magikarp', ['water'], 20, 10, 55, 80, 40, {1: moves.splash, 15: moves.tackle, 20: moves.bite, 41: moves.hydro_pump, 52: moves.hyper_beam}, [{'name': 'gyrados', 'level': 20, 'max_health': 95, 'attack_power': 125, 'defense_power': 79, 'speed': 81, 'exp_yield': 189, }], level)
        
        self.level = level
        self.current_health = self.max_health
        self.ko = False




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


#objects of starting pokemon that a new user can chose from
start_bulbasaur = Bulbasaur(1)
start_charmander = Charmander(1)
start_squirtle = Squirtle(1)

starting_pokemon = [start_bulbasaur, start_charmander, start_squirtle]

def print_starting_pokemon():
    list = ''
    for i, pokemon in enumerate(starting_pokemon, 1):
        list += '{0}: {1}\n'.format(i, pokemon.name)
    return list





#test_bulb = Bulbasaur(23)

#test_char = Charmander(40)

#test_char.attack(moves.scratch, test_bulb)
#test_bulb.attack(moves.tackle, test_char)

#test_char.print_avail_moves()