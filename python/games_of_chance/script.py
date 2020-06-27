#Project Goal (supplied by Codecademy): You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

#imported libraries (supplied by Codecademy)
import random

money = 100


##GAME OF CHANCE FUNCTIONS##

#coin flip
def coin_flip(call, bet):
    print('Welcome to Tim\'s Silver Coin Flip! All bets are final. Good luck!')
    

    #generating random number of 0 or 1, and assigning that to 'tails' (0) or 'heads' (1)
    num = random.randint(0,1)
    if num == 0:
        face = 'Tails'
        print('It landed tails.')
    else:
        face = 'Heads'
        print('It landed heads.')

    if call == face:
        print('Winner! Winner! You won {0}.'.format(bet))
        return bet
    else:
        print('Better luck next time. You owe the house {0}.'.format(bet))
        return 0 - bet


#cho-han
def cho_han(call, bet):
    print('Welcome to on Tim\'s Cho-Han Rumble! All bets are final. Good luck!')

    #generating two random numbers, each ranging from 1 to 6, and determining if sum is odd or even
    dice = [random.randint(1, 6) for i in range(0,2)]
    total = sum(dice)
    if total % 2 == 0:
        result = 'Even'
        print('{0} and {1} equal {2}. That is even.'.format(dice[0], dice[1], total))
    else:
        result = 'Odd'
        print('{0} and {1} equal {2}. That is odd.'.format(dice[0], dice[1], total))

    if call == result:
        print('Winner! Winner! You won {0}.'.format(bet))
        return bet
    else:
        print('Better luck next time. You owe the house {0}.'.format(bet))
        return 0 - bet


#high card
def high_card(bet):
    print('Welcome to Tim\'s High Card Shenanigans! Aces are high and all bets are final. Good luck!')

    #generating two cards, player and house, assigning to face value if face card
    deck = []
    for i in range(2, 15):
        deck.append(i)
        deck.append(i)
        deck.append(i)
        deck.append(i)

    cards =[deck.pop(random.randrange(len(deck))) for i in range(2)]
    card_name = []
    for card in cards:
        if card == 11:
            card_name.append('Jack')
        elif card == 12:
            card_name.append('Queen')
        elif card == 13:
            card_name.append('King')
        elif card == 14:
            card_name.append('Ace')
        else:
            card_name.append(str(card))
    print('You drew a {0} and the house drew a {1}.'.format(card_name[0], card_name[1]))

    #determining if user or the house won
    if cards[0] > cards[1]:
        print('Winner! Winner! You won {0}.'.format(bet))
        return bet
    elif cards[0] < cards[1]:
        print('Better luck next time. You owe the house {0}.'.format(bet))
        return 0 - bet
    else:
        print('Push. Almost like kissing your sister.')
        return 0


#roulette

#code to create template for each number of the roulette wheel, and adjust it from there (I don't know the sequential patter for red and black)
french_wheel = [i for i in range(0, 37)]
american_wheel = ['00'] + [str(x) for x in french_wheel]

dict_keys = ['number','color', 'odd_even']
dict_values = ['black/red', 'odd/even']

#wheel_dict = {key: {'number': key, 'color': 'black/red', 'odd_even': int(key) % == 0} for key in american_wheel}

def num_even_odd(num):
    if num == '0' or num == '00':
        return None
    elif int(num) % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def num_color(num):
    if num == '0' or num == '00':
        return 'Green'
    if int(num) in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return 'Red'
    else:
        return 'Black'

wheel_dict = {}

for num in american_wheel:
    wheel_dict[num] = {'Number': num, 'even_odd': num_even_odd(num), 'color': num_color(num)}


def roulette(type, name, bet):
    print('Welcome to Tim\'s Spin-to-Win Roulette! All bets are final. Good luck!')

    #generating the roulette wheel and the number the ball landed on
    winning_number = random.choice(american_wheel)
    winning_color = wheel_dict[winning_number]['color']
    print('The round goes to {0} {1}.'.format(winning_color, winning_number))

    #determine winners and losers

    print(winning_color)
    #red-or-black type
    if type == 'Red or Black':
        if winning_color == name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet
    
    #straight type
    if type == 'Straight':
        if name == winning_number:
            print('Winner! Winner! You won {0}.'.format(bet * 35))
            return bet * 35
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #split or row type
    if type == 'Split' or type == 'Row':
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 17))
            return bet * 17
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #street or trio type
    if type == 'Street' or type == 'Trio':
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 11))
            return bet * 11
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #corner type
    if type == 'Corner':
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 8))
            return bet * 8
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet
        
    #double street type
    if type == 'Double Street':
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 5))
            return bet * 5
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #basket type
    if type == 'Basket':
        if winning_number in ['00', '0', '1', '2', '3']:
            print('Winner! Winner! You won {0}.'.format(bet * 6))
            return bet * 6
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #low-or-high type
    if type == 'Low or High':
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #dozen type
    if type == 'Dozen' or type == 'Column' or type == 'Snake':
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet * 2
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #even_orodd type
    if type == 'Even or Odd':
        if wheel_dict[winning_number]['even_odd'] == name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet








        

    
    




##FUNCTION CALLS##



print(money)

#money += roulette('low_or_high', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'], 30)
#money += roulette('red_or_black', 'Red', 30)

money += roulette('basket', ['00', '0', '1', '2', '3'], 30)

print(money)