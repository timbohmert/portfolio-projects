#Project Goal (supplied by Codecademy): You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

#imported libraries: Games created by Tim Bohmert
import games

#user class
class User:

    def __init__(self, wallet):
        self.wallet = wallet


#user input to enter the games

    def play_a_game(self):
        
        #requests user input for game selection
        game = int(input("""Select the number of the game you want to play:
        1)Coin Flip | 2)Cho-Han | 3)High Card | 4)Roulette: """))
        while game not in [1, 2, 3, 4]:
            game = int(input('Please select 1 for Coin Flip, 2 for Cho-Han, 3 for High Card, or 4 for Roulette: '))
        #user selected coin-flip, will run program and return winnings/losings and update wallet
        if game == 1:
            result = games.coin_flip()
            self.wallet += result
            print('After the last game, you now have {0} in your account wallet.'.format(self.wallet))


        #user selected cho-han, will run program and return winnings/losings and update wallet
        if game == 2:
            result = games.cho_han()
            self.wallet += result
            print('After the last game, you now have {0} in your account wallet.'.format(self.wallet))

        #user selected high card, will run program and return winnings/losings and update wallet
        if game == 3:
            result = games.high_card()
            self.wallet += result
            print('After the last game, you now have {0} in your account wallet.'.format(self.wallet))

        #user selected roulette, will run program and return winnings/losings and update wallet
        if game == 4:
            result = games.roulette
            self.wallet += result
            print('After the last game, you now have {0} in your account wallet.'.format(self.wallet))
                

print('Welcome to Tim\'s Roayle Casino!')

name = input('Please enter your name: ')
while type(name) == None:
    name = int(input('Please enter a valid name: '))

money = int(input('Please enter the amount of money you would like to deposit into your account wallet: '))

name = User(money)

print('You now have {0} in your wallet.'.format(name.wallet))

name.play_a_game()
