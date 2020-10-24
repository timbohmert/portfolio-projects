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
        if self.pokemon:
            self.active_pokemon = self.pokemon[0]
        self.battle_status = False
        self.storage = []


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def use_potion(self, potion_idx):
        #intake user input for potion selction
        if self.active_pokemon.ko == False:
            potion = self.potions[potion_idx]
            print('{0} used {1} on {2} and gained {3}hp.'.format(self.name, potion.name, self.active_pokemon.name, potion.effect))
            self.active_pokemon.gain_health(potion.effect)
            self.potions.pop(potion_idx)
        else:
            print('{0} is knocked out and needs to be revived.')
    

    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def attack_opp_trainer(self, opponent_trainer, selected_attack_idx):
        selected_attack = self.active_pokemon.available_moves[selected_attack_idx]
        print('{0} told {1} to use {2}.'.format(self.name, self.active_pokemon.name, selected_attack.name))
        self.active_pokemon.attack(selected_attack, opponent_trainer.active_pokemon)


    #method for changing active pokemon with one of available six pokemon
    def change_pokemon(self, diff_pokemon):
        print('{0} made {1} their active pokemon.'.format(self.name, diff_pokemon.name))
        self.active_pokemon = diff_pokemon


    #method to check if the trainer still has pokemon to battle
    def check_battle_status(self):
        self.battle_status = False
        for poke in self.pokemon:
            if poke.ko == False:
                self.battle_status = True
                return self.battle_status
        print('{0} doesn\'t have any Pokemon available to battle.'.format(self.name))


    #holder method that will be writtn over in inherited classes
    def battle_turn(self, opponent_trainer):
        pass


    #function for battling another trainer that 
    def pokemon_battle(self, opp_trainer):
        self.check_battle_status()
        if self.battle_status == True:
            
            #resets active pokemon to 0 index pokemon, and notifies user of opponent's active pokemon 
            self.active_pokemon = self.pokemon[0]
            print('Let\'s battle!')
            print('{0} sent out {1} as their first Pokemon to battle!'.format(self.name, self.active_pokemon.name))
            print('{0} sent out {1} as their first Pokemon to battle!'.format(opp_trainer.name, opp_trainer.active_pokemon.name))
            
            #determines which trainer will go first
            if self.active_pokemon.speed >= opp_trainer.active_pokemon.speed:
                first = self
                second = opp_trainer
            
            #alternates battle turns
            turn_count = 0
            while self.battle_status == True and opp_trainer.battle_status == True:
                if turn_count % 2 == 0:
                    first.battle_turn(second)
                    turn_count += 1
                else:
                    second.battle_turn(first)
                    turn_count += 1

            #print statement acknowledging winner and ending battle
            winner = first if turn_count % 2 == 0 else second 
            print('{0} won the battle!'.format(winner.name))

        #print statement when trainer is not able to battle     
        else:
            print('Please revive some Pokemon before battling.')


    #method for adding pokemon to available pokemon
    def add_pokemon(self, new_pokemon):
        if len(self.pokemon) < 6:
            print("{new_pokemon} has been added to {trainer_name}'s available Pokemon.".format(new_pokemon = new_pokemon.name, trainer_name = self.name))
            return self.pokemon.append(new_pokemon)
        else:
            print('{trainer_name} has too many Pokemon and needs to drop one before adding {new_pokemon}.'.format(trainer_name = self.name, new_pokemon = new_pokemon))


    #method for dropping pokemon from available pokemon
    def drop_pokemon(self, poke_to_drop_idx):
        print('{0} dropped {1} from their available Pokemon and was put into storage.'.format(self.name, self.pokemon[poke_to_drop_idx].name))
        poke_to_drop = self.pokemon.pop(poke_to_drop_idx)
        self.storage.append(poke_to_drop)
    

#class for pokemon trainers
class User_Trainer(Trainer): 
    
    #constructor method for trainer attributes of list of available pokemon, name of the trainer, dictionary of their potions, and the active pokemon
    def __init__(self, name):
        super().__init__([], name, [])
        self.wallet = 500


    #method for using a potion on the active pokemon. Prints out name of potion used and the hp it will give with the active pokemon
    def select_potion(self):
        #intake user input for potion selction
        potion_idx = int(input('Select the number of the potion you would like to use:\n{0}'.format(self.print_potions()))) - 1
        if potion_idx < len(self.potions) and potion_idx >= 0:
            self.use_potion(potion_idx)


    #method for attacking opponent trainer's active pokemon with trainer's active pokemon. Prints out name of attach
    def selected_attack(self, opponent_trainer):
            selected_attack_idx = int(input('''What move would you like to use next?\n{0}'''.format(self.active_pokemon.print_avail_moves()))) - 1
            if selected_attack_idx in range(3):
                self.attack_opp_trainer(opponent_trainer, selected_attack_idx)
            else: 
                self.selected_attack(opponent_trainer)


    #select pokemon to activate for battle
    def select_pokemon(self):
        selected_pokemon_idx = int(input('Select the number of the Pokemon you would like to battle with:\n{0}'.format(self.print_pokemon()))) - 1
        if selected_pokemon_idx < len(self.pokemon) and selected_pokemon_idx >= 0:
            selected_pokemon = self.pokemon[selected_pokemon_idx]
            if selected_pokemon.ko == False:
                self.change_pokemon(selected_pokemon)
            else:
                print('{0} is knocked out and unable to battle.'.format(selected_pokemon.name))
                self.select_pokemon()
        else:
            self.select_pokemon()


    #helper method to select opponent trainer to battle. Should this go onto script file?
    def select_battle_opp(self, opponent_trainers):
        opponent_trainer_idx = int(input('First, what trainer would you like to battle:\n{0}'.format(self.print_opp_trainers(opponent_trainers)))) - 1
        opponent_trainer = opponent_trainers[opponent_trainer_idx]
        check = input('Are you sure that you would like to battle {0}?\nY: Yes\nN: No\n'.format(opponent_trainer.name))
        if check == 'Y':
            self.pokemon_battle(opponent_trainer)


    #method for selecting action during battling 
    def battle_turn(self, opponent_trainer):
        if self.active_pokemon.ko == False:
            move = int(input('Select the number of what you would like to do next:\n1: Attack\n2: Use item\n3: Switch pokemon\n'))
            if move not in range(1, 4):
                self.battle_turn(opponent_trainer)
            if move == 1:
                self.selected_attack(opponent_trainer)
            if move == 2:
                self.select_potion()
            if move == 3:
                self.select_pokemon()
        else:
            print('{0} is knocked out and unable to attack.'.format(self.active_pokemon.name))
            self.check_battle_status()
            if self.battle_status == True:
                self.select_pokemon()
                self.battle_turn(opponent_trainer)
            else:
                print('All of your Pokemon are knocked out.')


    #method for reordering pokemon to first position
    def reorder_pokemon(self):
        new_top_poke_idx = int(input('Select the number of the Pokemon you would like to start battles:\n{0}'.format(self.print_pokemon()))) - 1
        print('{0} was moved to the top Pokemon and will start your battles'.format(self.pokemon[new_top_poke_idx].name))
        self.pokemon[0], self.pokemon[new_top_poke_idx] = self.pokemon[new_top_poke_idx], self.pokemon[0]


    #method for adding pokemon to available pokemon
    def add_pokemon(self, new_pokemon, avail_storage = False):
        if len(self.pokemon) < 6:
            print("{0} has been added to {1}'s available Pokemon.".format(new_pokemon.name, self.name))
            return self.pokemon.append(new_pokemon)
        else:
            if avail_storage == True:
                print('{0} has too many Pokemon and needs to drop one before adding {1} or it will be sent to storage.'.format(self.name, new_pokemon.name))
                drop_y_n = input('Would you like to drop a Pokemon to make room for {0}\nY: Yes\nN: No\n'.format(new_pokemon.name))
                if drop_y_n == 'Y':
                    self.select_drop_pokemon()
                    self.add_pokemon(new_pokemon)
            else:
                print('{0} is carrying too many Pokemon and {1} was sent to storage.'.format(self.name, new_pokemon.name))
                self.storage.append(new_pokemon)        

   
    #method for dropping pokemon from available pokemon
    def select_drop_pokemon(self):
        poke_to_drop_idx = int(input('Select the number of the Pokemon that you would like to drop:\n{0}'.format(self.print_pokemon()))) - 1
        if poke_to_drop_idx < len(self.pokemon) and poke_to_drop_idx >= 0:
            check = input('Are you sure that you would like to drop {0}?\nY: Yes\nN: No\n'.format(self.pokemon[poke_to_drop_idx].name))
            if check == 'Y':
                self.drop_pokemon(poke_to_drop_idx)


    #function to buy potion
    def buy_item(self, store):
        selected_potion_idx = int(input('Select the number of the item that you would like to buy\n{0}'.format(self.print_store_items(store)))) - 1
        selected_potion =store[selected_potion_idx]
        if selected_potion.price <= self.wallet:
            check = input('Are you sure that you would like to buy {0}?\nY: Yes\nN: No\n'.format(selected_potion.name))
            if check == 'Y':
                print('You just added {0} to your items!'.format(selected_potion.name))
                self.potions.append(selected_potion)
                self.wallet -= selected_potion.price
                print('You now have ${0} in your wallet.'.format(self.wallet))
                check = input('Would you like to buy a different item?\nY: Yes\nN: No\n')
                if check == 'Y':
                    self.buy_item(store)
        else:
            print('You don\'t have enough money for {0}'.format(selected_potion.name))
            check = input('Would you like to buy a different item?\nY: Yes\nN: No\n')
            if check == 'Y':
                self.buy_item(store)


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


    #helper method to print out the items in a store
    def print_store_items(self, store):
        list = ''
        for i, item in enumerate(store, 1):
            list += '{0}: {1} - ${2}\n'.format(i, item.name, item.price)
        return list


    #helper method to print out the trainers
    def print_opp_trainers(self, opponent_trainers):
        list = ''
        for i, trainer in enumerate(opponent_trainers, 1):
            list += '{0}: {1}\n'.format(i, trainer.name)
        return list



#class for opponent trainers that inherits trainer class
class Opponent_Trainer(Trainer):
    #constructor method that takes in list of opponent trainer's pokemon, name, potions, active
    def __init__(self, pokemon, name, potions, move_sequence):
        super().__init__(pokemon, name, potions)
        self.move_sequence = move_sequence
        self.battle_status = True


####Need to create structure for the move_sequence. Thinking to create dictionaries for each pokemon, and then dictionary for each turn with key:value for attack, potion, or change pokemon. Need to think about how to create smart selection of when to use potion with a lot of damage, or when to change to different pokemon if the multiplier is not good. Should we use unique data structure for finding the right move?
    #method to select move from move_sequence
    def select_move(self):
        return 1 


    #method for selecting action during battling 
    def battle_turn(self, opponent_trainer):
        if self.active_pokemon.ko == False:
            move = self.select_move()
            if move == 1:
                self.attack_opp_trainer(opponent_trainer, 0)
            if move == 2:
                self.use_potion(moves.super_potion)
            if move == 3:
                self.change_pokemon(self.active_pokemon)
        else:
            print('{0} is knocked out and unable to attack.'.format(self.active_pokemon.name))
            self.check_battle_status()
            if self.battle_status == True:
                self.change_pokemon(self.active_pokemon)
                self.battle_turn(opponent_trainer)
            else:
                print('All of {0}\'s Pokemon are knocked out.'.format(self.name))





###TESTS###


test_pikachu = pokemon.Pikachu(40)
test_bulb = pokemon.Bulbasaur(1)
test_char = pokemon.Charmander(1)
test_squir = pokemon.Squirtle(1)
test_karp = pokemon.Magikarp(1)
test_snor = pokemon.Snorlax(1)
test_bulb2 = pokemon.Bulbasaur(1)

#default trainer objects
ash = User_Trainer("Ash")

ash.potions = [moves.potion, moves.super_potion, moves.hyper_potion, moves.max_potion]

beth = Opponent_Trainer([test_bulb], "Beth", [moves.potion, moves.max_potion], [])
tim = Opponent_Trainer([test_bulb2], "Tim", [moves.potion, moves.max_potion], [])

#ash.add_pokemon(test_pikachu)
ash.add_pokemon(test_bulb)
#ash.add_pokemon(test_char)
#ash.add_pokemon(test_karp)
#ash.add_pokemon(test_snor)
#ash.add_pokemon(test_squir)
#ash.add_pokemon(test_bulb2)



#ash.select_pokemon()

#print(ash.active_pokemon.name)

#ash.battle_status = True

#ash.battle_turn(beth)

beth.pokemon_battle(tim)
beth.pokemon_battle(tim)