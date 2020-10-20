#file to store all of the trainers using imported Trainer class

#imoport pokemon from pokemon
import pokemon
import moves



#class for opponent trainers that inherits trainer class
class Trainer():
    #constructor method that takes in list of opponent trainer's pokemon, name, potions, active
    def __init__(self, pokemon, name, potions):
        self.pokemon = pokemon
        self.name = name
        self.potions = potions
        self.active_pokemon = self.pokemon[0]
        self.battle_status = True


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def use_potion(self, potion_idx):
        #intake user input for potion selction
        potion = self.potions[potion_idx]
        print('{0} used {1} on {2} and gained {3}hp.'.format(self.name, potion.name, self.active_pokemon.name, potion.effect))
        self.active_pokemon.gain_health(potion.effect)
        self.potions.pop(potion_idx)
    

    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def attack_opp_trainer(self, opponent_trainer, selected_attack_idx):
        selected_attack = self.active_pokemon.available_moves[selected_attack_idx]
        print('{0} told {1} to use {2}.'.format(self.name, self.active_pokemon.name, selected_attack.name))
        self.active_pokemon.attack(selected_attack, opponent_trainer.active_pokemon)


    #method for changing active pokemon with one of available six pokemon
    def change_pokemon(self, diff_pokemon):
        print('{0} made {1} their active pokemon.'.format(self.name, diff_pokemon.name))
        self.active_pokemon = diff_pokemon

    #method for adding pokemon to available pokemon
    def add_pokemon(self, new_pokemon):
        if len(self.pokemon) < 6:
            print("{new_pokemon} has been added to {trainer_name}'s available Pokemon.".format(new_pokemon = new_pokemon.name, trainer_name = self.name))
            return self.pokemon.append(new_pokemon)
        else:
            print('{trainer_name} has too many Pokemon and needs to drop one before adding {new_pokemon}.'.format(trainer_name = self.name, new_pokemon = new_pokemon))


    #method for dropping pokemon from available pokemon
    def drop_pokemon(self, drop_pokemon):
        if drop_pokemon in self.pokemon:
            drop_index = self.pokemon.index(drop_pokemon)
            self.pokemon.pop(drop_index)
            print('{trainer_name} dropped {drop_pokemon} from their available Pokemon.'.format(trainer_name = self.name, drop_pokemon = drop_pokemon.name))
        else:
            print('{trainer_name} is not carrying {drop_pokemon} and cannot be dropped from available Pokemon.'.format(trainer_name = self.name, drop_pokemon = drop_pokemon.name))
    

#class for pokemon trainers
class User_Trainer(Trainer): 
    
    #constructor method for trainer attributes of list of available pokemon, name of the trainer, dictionary of their potions, and the active pokemon
    def __init__(self, pokemon, name, potions = []):
        self.pokemon = pokemon
        self.name = name
        self.potions = potions
        self.active_pokemon = self.pokemon[0]
        self.battle_status = True


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def select_potion(self):
        #intake user input for potion selction
        potion_idx = int(input('Select the number of the potion you would like to use:\n{0}'.format(self.print_potions()))) - 1
        if potion_idx < len(self.potions) and potion_idx >= 0:
            self.use_potion(potion_idx)


    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def selected_attack(self, opponent_trainer):
            selected_attack_idx = int(input('''What move should {0} use next?\n{1}'''.format(self.active_pokemon.name, self.active_pokemon.print_avail_moves()))) - 1
            if selected_attack_idx in range(3):
                self.attack_opp_trainer(opponent_trainer, selected_attack_idx)
            else: 
                self.selected_attack(opponent_trainer)


    #select pokemon to activate for battle
    def select_pokemon(self):
        selected_pokemon_idx = int(input('Select the number of the Pokemon would you like to battle with:\n{0}'.format(self.print_pokemon()))) - 1
        if selected_pokemon_idx < len(self.pokemon) and selected_pokemon_idx >= 0:
            selected_pokemon = self.pokemon[selected_pokemon_idx]
            if selected_pokemon.ko == False:
                self.change_pokemon(selected_pokemon)
            else:
                print('{0} is knocked out and unable to battle.'.format(selected_pokemon.name))
                self.select_pokemon()
        else:
            self.select_pokemon()


    #method to check if the trainer still has pokemon to battle
    def check_battle_status(self):
        self.battle_status = False
        for poke in self.pokemon:
            if poke.ko == False:
                self.battle_status = True
                return self.battle_status


    #method for selecting action during battling 
    def battle_turn(self, opponent_trainer):
        if self.active_pokemon.ko == False:
            move = input('Select the number of what you would like to do next:\n1: Attack\n2: Use item\n3: Switch pokemon\n')
            if move == '1':
                self.selected_attack(opponent_trainer)
            if move == '2':
                self.select_potion()
            if move == '3':
                self.select_pokemon()
        else:
            print('{0} is knocked out and unable to attack.'.format(self.active_pokemon.name))
            self.check_battle_status()
            if self.battle_status == True:
                self.select_pokemon()
                self.battle_turn(opponent_trainer)
            else:
                print('All of {0}\'s Pokemon are knocked out. {0} lost the battle.'.format(self.name))


    #method for reordering pokemon to first position
    def reorder_pokemon(self):
        new_top_poke_idx = int(input('Select the number of the Pokemon you would like to start battles:\n{0}'.format(self.print_pokemon()))) - 1
        print('{0} was moved to the top Pokemon and will start your battles'.format(self.pokemon[new_top_poke_idx].name))
        self.pokemon[0], self.pokemon[new_top_poke_idx] = self.pokemon[new_top_poke_idx], self.pokemon[0]


    #method for adding pokemon to available pokemon
    def add_pokemon(self, new_pokemon, storage = False):
        if len(self.pokemon) < 6:
            print("{0} has been added to {1}'s available Pokemon.".format(new_pokemon.name, self.name))
            return self.pokemon.append(new_pokemon)
        else:
            if storage == True:
                print('{0} has too many Pokemon and needs to drop one before adding {1} or it will be sent to storage.'.format(self.name, new_pokemon.name))
                drop_y_n = input('Would you like to drop a Pokemon to make room for {0}\nY: Yes\nN: No\n'.format(new_pokemon.name))
                if drop_y_n == 'Y':
                    self.drop_pokemon(storage)
                    self.add_pokemon(new_pokemon)
            else:
                print('{0} is carrying too many Pokemon and {1} was sent to storage.'.format(self.name, new_pokemon.name))
                storage.append(new_pokemon)        

   
    #method for dropping pokemon from available pokemon
    def drop_pokemon(self, storage):
        poke_to_drop_idx = int(input('Select the number of the Pokemon that you would like to drop:\n{0}'.format(self.print_pokemon()))) - 1
        if poke_to_drop_idx < len(self.pokemon) and poke_to_drop_idx >= 0:
            check = input('Are you sure that you would like to drop {0}?\nY: Yes\nN: No\n'.format(self.pokemon[poke_to_drop_idx].name))
            if check == 'Y':
                print('{0} dropped {1} from their available Pokemon and was put into storage.'.format(self.name, self.pokemon[poke_to_drop_idx].name))
                poke_to_drop = self.pokemon.pop(poke_to_drop_idx)
                storage.append(poke_to_drop)


    #helper method to print the potions that the user has
    def print_potions(self):
        list = ''
        for i, potion in enumerate(self.potions, 1):
            list += '{0}: {1} ({2} hp)\n'.format(i, potion.name, potion.effect)
        return list


    #helper method to print the pokemon that the user has
    def print_pokemon(self):
        list = ''
        for i, poke in enumerate(self.pokemon, 1):
            list += '{0}: {1}\n'.format(i, poke.name)
        return list






#class for opponent trainers that inherits trainer class
class Opponent_Trainer(Trainer):
    #constructor method that takes in list of opponent trainer's pokemon, name, potions, active
    def __init__(self, pokemon, name, potions, move_sequence = [[]]):
        self.pokemon = pokemon
        self.name = name
        self.potions = potions
        self.active_pokemon = self.pokemon[0]
        self.move_sequence = move_sequence


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def use_potion(self, potion):
        potion_hp = self.potions[potion]
        print('{0} used {1} on {2} and gained {3}hp.'.format(self.name, potion, self.active_pokemon.name, potion_hp))
        self.active_pokemon.gain_health(potion_hp)
        self.potions.pop(potion)
    

    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def attack_opp_trainer(self, opponent_trainer, selected_attack_idx):
        if self.active_pokemon.ko == False:
            selected_attack = self.active_pokemon.available_moves[selected_attack_idx]
            print('{0} told {1} to use {2}.'.format(self.name, self.active_pokemon.name, selected_attack.name))
            self.active_pokemon.attack(selected_attack, opponent_trainer.active_pokemon)
        else:
            print('{0} is knocked out and unable to attack.'.format(self.active_pokemon.name))


    #method for changing active pokemon with one of available six pokemon
    def change_pokemon(self, diff_pokemon):
        if diff_pokemon in self.pokemon and diff_pokemon.ko == False:
            print('{trainer_name} made {pokemon_name} their active pokemon.'.format(trainer_name = self.name, pokemon_name = diff_pokemon.name))
            self.active_pokemon = diff_pokemon
        else:
            print('{pokemon_name} is not available.'.format(pokemon_name = diff_pokemon.name))


    #method for adding pokemon to available pokemon
    def add_pokemon(self, new_pokemon):
        if len(self.pokemon) < 6:
            print("{new_pokemon} has been added to {trainer_name}'s available Pokemon.".format(new_pokemon = new_pokemon.name, trainer_name = self.name))
            return self.pokemon.append(new_pokemon)
        else:
            print('{trainer_name} has too many Pokemon and needs to drop one before adding {new_pokemon}.'.format(trainer_name = self.name, new_pokemon = new_pokemon))


    #method for dropping pokemon from available pokemon
    def drop_pokemon(self, drop_pokemon):
        if drop_pokemon in self.pokemon:
            drop_index = self.pokemon.index(drop_pokemon)
            self.pokemon.pop(drop_index)
            print('{trainer_name} dropped {drop_pokemon} from their available Pokemon.'.format(trainer_name = self.name, drop_pokemon = drop_pokemon.name))
        else:
            print('{trainer_name} is not carrying {drop_pokemon} and cannot be dropped from available Pokemon.'.format(trainer_name = self.name, drop_pokemon = drop_pokemon.name))
    




###TESTS###


test_pikachu = pokemon.Pikachu(40)
test_bulb = pokemon.Bulbasaur(1)

#default trainer objects
ash = User_Trainer([test_pikachu, test_bulb], "Ash", [moves.potion, moves.super_potion, moves.hyper_potion, moves.max_potion])


opp_trainers = []

beth = Opponent_Trainer([test_bulb, test_pikachu], "Beth", [moves.potion, moves.max_potion])

storage_1 = [[]]

ash.add_pokemon(test_bulb)
ash.add_pokemon(test_bulb)
ash.add_pokemon(test_bulb)
ash.add_pokemon(test_bulb)
ash.add_pokemon(test_bulb, storage_1)

print(ash.active_pokemon.name)

ash.select_pokemon()

print(ash.active_pokemon.name)

ash.battle_status = True

ash.battle_turn(beth)
