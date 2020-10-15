#Project Goals: In this project, you will be using Python Classes to create a game system similar to the popular game series Pokémon. If you’re unfamiliar with Pokémon, it is a game where creatures (Pokémon) battle against each other. Every Pokémon has statistics associated with it like health, level, type, and a name. In this project we’ll make several classes that interact with each other so you can create your own Pokémon battles!



import trainers, pokemon


def select_first_pokemon():
    first_pokemon_idx = int(input('Type in the number of the Pokemon that you would like to chose:\n{0}'.format(pokemon.print_starting_pokemon()))) - 1
    if first_pokemon_idx < len(pokemon.starting_pokemon) and first_pokemon_idx >= 0:
        first_pokemon = pokemon.starting_pokemon[first_pokemon_idx]
        check = input('Are you sure that you would like to select {0} as your first Pokemon?\nY: Yes\nN: No\n'.format(first_pokemon.name))
        if check == 'Y':
            return first_pokemon
    select_first_pokemon()


#greeting and profile creation
print('Hello! Welcome to Pokemon Battle!\n\nLet\'s start by making a profile.\n')

#profile name
profile_name = input('First, what is your name?\n')

print('Nice to meet you {0}!\n\nNext let\'s choose our first Pokemon.\n'.format(profile_name))

user_first_pokemon = select_first_pokemon()





profile = trainers.Trainer(user_first_pokemon, profile_name)




#method tests


#Opportunity for increased functionality of the game
# • Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
# • Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
# • Let your Pokémon evolve once they hit a certain level.
# • Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.