#Project Goals: In this project, you will be using Python Classes to create a game system similar to the popular game series Pokémon. If you’re unfamiliar with Pokémon, it is a game where creatures (Pokémon) battle against each other. Every Pokémon has statistics associated with it like health, level, type, and a name. In this project we’ll make several classes that interact with each other so you can create your own Pokémon battles!



import trainers, pokemon, moves

#function for selecting the first pokemon upon profile creation
def select_first_pokemon():
    first_pokemon_idx = int(input('Type in the number of the Pokemon that you would like to chose:\n{0}'.format(pokemon.print_starting_pokemon()))) - 1
    if first_pokemon_idx < len(pokemon.starting_pokemon) and first_pokemon_idx >= 0:
        first_pokemon = pokemon.starting_pokemon[first_pokemon_idx]
        check = input('Are you sure that you would like to select {0} as your first Pokemon?\nY: Yes\nN: No\n'.format(first_pokemon.name))
        if check == 'Y':
            print('Aweseome! You chose {0} as your first Pokemon!'.format(first_pokemon.name))
            return first_pokemon
    select_first_pokemon()


#helper method to print out the items in a store
def print_store_items(store):
    list = ''
    for i, item in enumerate(store, 1):
        list += '{0}: {1} - ${2}\n'.format(i, item.name, item.price)
    return list


#function to buy potion
def buy_potion(store):
    selected_potion_idx = int(input('Select the number of the potion that you would like to buy\n{0}'.format(print_store_items(store))))
    check = input('Are you sure that you would like to buy {0}?\nY: Yes\nN: No\n'.format(store[selected_potion_idx].name))
    if check == 'Y':
        return 



#helper method to print out the trainers
def print_opp_trainers(opponent_trainers):
    list = ''
    for i, trainer in enumerate(opponent_trainers, 1):
        list += '{0}: {1}\n'.format(i, trainer.name)
    return list


#method to select opponent trainer to battle. Should this go onto script file?
def select_opp_trainer(opponent_trainers):
    opponent_trainer_idx = input('What trainer would you like to battle:\n{0}'.format(print_opp_trainers(opponent_trainers))) - 1
    opponent_trainer = opponent_trainers[opponent_trainer_idx]
    check = input('Are you sure that you would like to battle {0}?\nY: Yes\nN: No\n'.format(opponent_trainer.name))
    if check == 'Y':
        return 


#function for battling another trainer that 
def pokemon_battle(name):
    pass

        

#stores

starting_store = [moves.potion, moves.super_potion]




#greeting and profile creation
print('Hello! Welcome to Pokemon Battle!\n\nLet\'s start by making a profile.\n')

#profile name
profile_name = input('First, what is your name?\n')

#create user profile
profile = trainers.User_Trainer([0], profile_name)


#select first pokemon
print('Nice to meet you {0}!\n\nNext let\'s choose our first Pokemon.\n'.format(profile_name))
user_first_pokemon = select_first_pokemon()
profile.add_pokemon(user_first_pokemon)


#select any potions
print('Wow, your grandpa put ${0} in your wallet!'.format(profile.wallet))
check = input('Next, would you like to go to the store to buy any potions\nY: Yes\nN: No\n')
if check == 'Y':
    profile.buy_item(starting_store)





#method tests


#Opportunity for increased functionality of the game
# • Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
# • Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
# • Let your Pokémon evolve once they hit a certain level.
# • Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.

print_store_items(starting_store)