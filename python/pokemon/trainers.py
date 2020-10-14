#file to store all of the trainers using imported Trainer class

#imoport pokemon from pokemon
import pokemon
import moves

#class for pokemon trainers
class Trainer: 
    
    #constructor method for trainer attributes of list of available pokemon, name of the trainer, dictionary of their potions, and the active pokemon
    def __init__(self, pokemon, name, potions):
        self.pokemon = pokemon
        self.name = name
        self.potions = potions
        self.active_pokemon = self.pokemon[0]


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def use_potion(self):
        #intake user input for potion selction
        potion = int(input('What potion would you like to use:\n{0}'.format(self.print_potions))) - 1
        if potion in self.potions:
            potion_hp = self.potions[potion]
            print('{0} used {1} on {2} and gained {3}hp.'.format(self.name, potion, self.active_pokemon.name, potion_hp))
            self.active_pokemon.gain_health(potion_hp)
            self.potions.pop(potion)
        else:
            self.use_potion()


    #method to battle an opponent trainer. Should this go onto script file?
    def battle_opp_trainer(self):
        opponent_trainer_idx = input('What trainer would you like to battle:\n{0}'.format(self.print_opp_trainers())) - 1


    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def attack_opp_trainer(self, opponent_trainer):
        if self.active_pokemon.ko == False:
            selected_attack_idx = int(input('''What move should {0} use next?\n{1}'''.format(self.active_pokemon.name, self.active_pokemon.print_avail_moves()))) - 1
            if selected_attack_idx in range(3):
                selected_attack = self.active_pokemon.available_moves[selected_attack_idx]
                print('{0} told {1} to use {2}.'.format(self.name, self.active_pokemon.name, selected_attack.name))
                self.active_pokemon.attack(selected_attack, opponent_trainer.active_pokemon)
            else: 
                self.attack_opp_trainer(opponent_trainer)
        else:
            print('{0} is knocked out and unable to attack.'.format(self.active_pokemon.name))


    #method for changing active pokemon with one of available six pokemon
    def change_pokemon(self):
        diff_pokemon = input()
        if diff_pokemon in self.pokemon and diff_pokemon.ko == False:
            print('{0} made {1} their active pokemon.'.format(self.name, diff_pokemon.name))
            self.active_pokemon = diff_pokemon
        else:
            print('{0} is not available.'.format(diff_pokemon.name))


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


    #helper methods
    def print_potions(self):
        for i, potion in enumerate(self.potions, 1):
            print('{0}: {1}'.format(i, potion))

    def print_pokemon(self):
        for i, pokemon in enumerate(self.pokemon, 1):
            print('{0}: {1}'.format(i, pokemon))

    def print_opp_trainers(self):
        for i, trainer in enumerate(opp_trainers, 1):
            print('{0}: {1}'.format(i, trainer))


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
ash = Trainer([test_pikachu], "Ash", {'lorem': 50, 'ipsum': 25}, test_pikachu)


#tim = Trainer([pokemon.squirtle, pokemon.charmander, pokemon.bulbasaur], "Tim", {'lorem': 50, 'ipsum': 25}, pokemon.charmander)

#misty = Trainer([pokemon.squirtle], "Misty", {'lorem': 50, 'ipsum': 25}, pokemon.squirtle)


beth = Opponent_Trainer([test_bulb], "Beth", {'lorem': 50, 'ipsum': 25}, test_bulb)


ash.attack_opp_trainer(beth)

opp_trainers = []