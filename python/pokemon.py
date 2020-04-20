#Project Goals: In this project, you will be using Python Classes to create a game system similar to the popular game series Pokémon. If you’re unfamiliar with Pokémon, it is a game where creatures (Pokémon) battle against each other. Every Pokémon has statistics associated with it like health, level, type, and a name. In this project we’ll make several classes that interact with each other so you can create your own Pokémon battles!

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


    #method for health gained from potion, with health maxed out at the max health
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



#pokemon objects
charmander = Pokemon('Charmander', 30, 0, 'fire', 130, 130, False, {'fire breath': 10, 'scratch': 7, 'flamethrower': 15})

squirtle = Pokemon('Squirtle', 69, 0, 'water', 140, 140, False, {'water hose': 10, 'tackle': 7, 'hydroblast': 15})

bulbassaur = Pokemon('Bulbassaur', 25, 0, 'grass', 150, 150, False, {'vine whip': 10, 'tackle': 7, 'power whip': 15})


#trainer objects
beth = Trainer([squirtle, charmander, bulbassaur], "Beth", {'elixir': 50, 'healing water': 25}, squirtle)

tim = Trainer([squirtle, charmander, bulbassaur], "Tim", {'elixir': 50, 'healing water': 25}, charmander)


#method tests
beth.attack_opp_trainer('water hose', tim)

tim.attack_opp_trainer('fire breath', beth)

beth.attack_opp_trainer('tackle', tim)

beth.attack_opp_trainer('tackle', tim)

beth.attack_opp_trainer('tackle', tim)

beth.attack_opp_trainer('tackle', tim)

tim.attack_opp_trainer('scratch', beth)

tim.change_pokemon(bulbassaur)

print(tim.active_pokemon.current_health)

tim.use_potion('elixir')

tim.drop_pokemon(charmander)

tim.drop_pokemon(charmander)

tim.add_pokemon(charmander)

print(tim.potions)

print(tim.active_pokemon.current_health)

tim.change_pokemon(charmander)


#Opportunity for increased functionality of the game
# • Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
# • Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
# • Let your Pokémon evolve once they hit a certain level.
# • Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.