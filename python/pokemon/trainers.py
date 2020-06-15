#file to store all of the trainers using imported Trainer class

#class for pokemon trainers
class Trainer: 
    
    #constructor method for trainer attributes of list of available pokemon, name of the trainer, dictionary of their potions, and the active pokemon
    def __init__(self, pokemon, name, potions, active_pokemon):
        self.pokemon = pokemon
        self.name = name
        self.potions = potions
        self.active_pokemon = active_pokemon


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def use_potion(self, potion):
        potion_hp = self.potions.pop(potion)
        print('{trainer_name} used {potion} on {active_pokemon} and gained {potion_hp}hp.'.format(trainer_name = self.name, potion = potion, active_pokemon = self.active_pokemon.name, potion_hp = potion_hp))
        self.active_pokemon.gain_health(potion_hp)
        
    

    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def attack_opp_trainer(self, selected_attack, opponent_trainer):
        if self.active_pokemon.ko == False:
            print('{trainer_name} told {pokemon_name} to use {selected_attack}.'.format(trainer_name = self.name, pokemon_name = self.active_pokemon.name, selected_attack = selected_attack))
            attack_hp = self.active_pokemon.attacks[selected_attack]
            opponent_pokemon = opponent_trainer.active_pokemon
            self.active_pokemon.attack(attack_hp, opponent_pokemon)
        else:
            print('{pokemon_name} is knocked out and unable to attack.'.format(pokemon_name = self.active_pokemon.name))



    #method for changing active pokemon with one of available six pokemon
    def change_pokemon(self, diff_pokemon):
        if diff_pokemon in self.pokemon and diff_pokemon.ko == False:
            print('{trainer_name} made {pokemon_name} his active pokemon.'.format(trainer_name = self.name, pokemon_name = diff_pokemon.name))
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
            print('{trainer_name} dropped {drop_pokemon} from his available Pokemon.'.format(trainer_name = self.name, drop_pokemon = drop_pokemon.name))
        else:
            print('{trainer_name} is not carrying {drop_pokemon} and cannot be dropped from available Pokemon.'.format(trainer_name = self.name, drop_pokemon = drop_pokemon.name))



#imoport pokemon from pokemon
import pokemon

#trainer objects
beth = Trainer([pokemon.squirtle, pokemon.charmander, pokemon.bulbassaur], "Beth", {'elixir': 50, 'healing water': 25}, pokemon.squirtle)

tim = Trainer([pokemon.squirtle, pokemon.charmander, pokemon.bulbassaur], "Tim", {'elixir': 50, 'healing water': 25}, pokemon.charmander)
