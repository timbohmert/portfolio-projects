#Project Goal (supplied by Codecademy): You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

#imported libraries: Games created by Tim Bohmert
import games

#user class
class User:

    def __init__(self):
        self.wallet = 0


    #user input to enter the games
    def play_a_game(self):
        
        #requests user input for game selection
        game = int(input("""\nSelect the number of the game you want to play:
        1)Coin Flip | 2)Cho-Han | 3)High Card | 4)Roulette: """))
        while game not in [1, 2, 3, 4]:
            game = int(input('\nPlease select 1 for Coin Flip, 2 for Cho-Han, 3 for High Card, or 4 for Roulette: '))
        #user selected coin-flip, will run program and return winnings/losings and update wallet
        if game == 1:
            result = games.coin_flip(self.wallet)
            self.wallet += result
            print('\nAfter the last game, you now have {0} in your account wallet.'.format(self.wallet))


        #user selected cho-han, will run program and return winnings/losings and update wallet
        if game == 2:
            result = games.cho_han(self.wallet)
            self.wallet += result
            print('\nAfter the last game, you now have {0} in your account wallet.\n'.format(self.wallet))

        #user selected high card, will run program and return winnings/losings and update wallet
        if game == 3:
            result = games.high_card(self.wallet)
            self.wallet += result
            print('\nAfter the last game, you now have {0} in your account wallet.\n'.format(self.wallet))

        #user selected roulette, will run program and return winnings/losings and update wallet
        if game == 4:
            result = games.roulette(self.wallet)
            self.wallet += result
            print('\nAfter the last game, you now have {0} in your account wallet.\n'.format(self.wallet))

    
    #deposit money into account
    def money_deposit(self):
        money = int(input('\nPlease enter the amount of money you would like to deposit into your account wallet: '))
        while type(money) != int:
            money = int(input('Please enter a number for the amount of money that you would like to enter into your account: '))
        self.wallet += money
        print('You now have {0} in your wallet.'.format(name.wallet))
                

print('\nWelcome to Tim\'s Roayle Casino!')

name = input('\nPlease enter your name: ')
while type(name) == None:
    name = int(input('\nPlease enter a valid name: '))
name = User()
print('\nBefore we can play some games, let\'s put some money into your account.')
name.money_deposit()

#while loop that allows user to play a game or deposit more money into their account
while True:
    while name.wallet > 0:
        option = int(input('''\nWhat would you like to do next?
        1) Play a game | 2) Deposit more money into your account: '''))
        while option not in [1, 2]:
            option = int(input('''Please select 1 to play a game or 2 to deposit more money into your account? '''))
        if option == 1:
            name.play_a_game()
        else:
            name.money_deposit()
    else:
        print('\nYou don\'t have any money in your acccount. Please make a deposit before you play a game.')
        name.money_deposit()
        

