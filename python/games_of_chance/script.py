#Project Goal (supplied by Codecademy): You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

#imported libraries: Games created by Tim Bohmert
import games

#user input to enter the games

def play_a_game(game):
    if game == 1:

        print('Welcome to Tim\'s Silver Coin Flip! All bets are final. Good luck!')        
        call = input('''Select the number of your call:
        1) Heads; 2) Tails: ''')
        call_int = int(call)
        while call_int not in [1, 2]:
                print('Please choose 1 or 2 to continue the story: ')
        if call_int == 1:
            call = 'Heads'
            bet = input('Please enter your bet: ')
            bet_int = int(bet)
            games.coin_flip(call, bet_int)
        elif call_int == 2:
            call = 'Tails'
            bet = input('Please enter your bet: ')
            bet_int = int(bet)
            games.coin_flip(call, bet_int)
                

name = input('Please enter your name: ')

money = input('Please enter the amount of money you would like to deposit into your account: ')

name = games.Games(money)

print('You now have {0} in your wallet.'.format(name.money))

game_to_play = input("""Select the number of the game you want to play: 
1) Coin Flip; 2) Cho-Han; 3) High Card; 4) Roulette: """)

play_a_game(int(game_to_play))