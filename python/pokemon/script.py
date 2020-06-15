#Project Goals: In this project, you will be using Python Classes to create a game system similar to the popular game series Pokémon. If you’re unfamiliar with Pokémon, it is a game where creatures (Pokémon) battle against each other. Every Pokémon has statistics associated with it like health, level, type, and a name. In this project we’ll make several classes that interact with each other so you can create your own Pokémon battles!











import trainers, pokemon


#method tests
trainers.beth.attack_opp_trainer('water hose', trainers.tim)

trainers.tim.attack_opp_trainer('fire breath', trainers.beth)

trainers.beth.attack_opp_trainer('tackle', trainers.tim)

trainers.beth.attack_opp_trainer('tackle', trainers.tim)

trainers.beth.attack_opp_trainer('tackle', trainers.tim)

trainers.beth.attack_opp_trainer('tackle', trainers.tim)

trainers.tim.attack_opp_trainer('scratch', trainers.beth)

trainers.tim.change_pokemon(pokemon.bulbassaur)

print(trainers.tim.active_pokemon.current_health)

trainers.tim.use_potion('elixir')

trainers.tim.drop_pokemon(pokemon.charmander)

trainers.tim.drop_pokemon(pokemon.charmander)

trainers.tim.add_pokemon(pokemon.charmander)

print(trainers.tim.potions)

print(trainers.tim.active_pokemon.current_health)

trainers.tim.change_pokemon(pokemon.charmander)


#Opportunity for increased functionality of the game
# • Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
# • Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
# • Let your Pokémon evolve once they hit a certain level.
# • Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.