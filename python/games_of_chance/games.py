#Project Goal (supplied by Codecademy): You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

#imported libraries supplied by Codecademy
import random

money = 100


##GAME OF CHANCE FUNCTIONS##


#coin flip
def coin_flip():
    print('Welcome to Tim\'s Silver Coin Flip! All bets are final. Good luck!')
    
    #taking in user selection of call (1 = Heads, 2 = Tails) and the quantity of their bet
    call_int = int(input('''Select the number of your call:
    1)Heads | 2)Tails: '''))
    while call_int not in [1, 2]:
            call_int = int(input('Please choose 1 for Heads or 2 for Tails: '))
    bet = int(input('Please enter your bet: '))
    while type(bet) != int:
        print('Please enter in whole number for a bet: ')
    if call_int == 1:
        call = 'Heads'
    else:
        call = 'Tails'

    #generating random number of 0 or 1, and assigning that to 'tails' (0) or 'heads' (1)
    num = random.randint(1,2)
    if num == 1:
        face = 'Heads'
        print('It landed Heads.')
    else:
        face = 'Tails'
        print('It landed tails.')

    #determines if user won and returns winnings/losings
    if call == face:
        print('Winner! Winner! You won {0}.'.format(bet))
        return bet
    else:
        print('Better luck next time. You owe the house {0}.'.format(bet))
        return 0 - bet


#cho-han
def cho_han():
    print('Welcome to on Tim\'s Cho-Han Rumble! All bets are final. Good luck!')

    #taking in user selection of call (1 = Even, 2 = Odd) and the quantity of their bet
    call_int = int(input('''Select the number of your call:
    1)Even | 2)Odd: '''))
    while call_int not in [1, 2]:
            call_int = int(input('Please choose 1 for Even or 2 for Odd: '))
    bet = int(input('Please enter your bet: '))
    while type(bet) != int:
        bet = int(input('Please enter in whole number for a bet: '))
    if call_int == 1:
        call = 'Even'
    else:
        call = 'Tails'

    #generating two random numbers, each ranging from 1 to 6, and determining if sum is odd or even
    dice = [random.randint(1, 6) for i in range(0,2)]
    total = sum(dice)
    if total % 2 == 0:
        result = 'Even'
        print('{0} and {1} equal {2}. That is even.'.format(dice[0], dice[1], total))
    else:
        result = 'Odd'
        print('{0} and {1} equal {2}. That is odd.'.format(dice[0], dice[1], total))

    #determines if user won and returns winnings/losings
    if call == result:
        print('Winner! Winner! You won {0}.'.format(bet))
        return bet
    else:
        print('Better luck next time. You owe the house {0}.'.format(bet))
        return 0 - bet


#high card
def high_card():
    print('Welcome to Tim\'s High Card Shenanigans! Aces are high and all bets are final. Good luck!')

    #taking in user the quantity of their bet
    bet = int(input('Please enter your bet: '))
    while type(bet) != int:
        bet = int(input('Please enter in whole number for a bet: '))

    #generating two cards, player and house, assigning to face value if face card
    deck = []
    for i in range(2, 15):
        deck.append(i)
        deck.append(i)
        deck.append(i)
        deck.append(i)

    #converts card number into string of name or number
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


from workshop import wheel_dict, american_wheel, type_selection, split_selection, split_selection_string, street_selection, street_selection_string, trio_selection


#function for roulette game
def roulette():
    print('Welcome to Tim\'s Spin-to-Win Roulette! All bets are final. Good luck!')

    #taking in user selection for type of bet
    bet_dict = {}
    while True:
        type_int = int(input('''Select the number for the type of bet you would like to make for the next spin: 
    {0}
    : '''.format(type_selection)))
        while type_int not in list(range(1,11)):
            type_int = int(input('''Invalid Entry. Please choose a number from the following selection: {0}: '''.format(type_selection)))
        
        #red or black selection (1 = red, 2 = black)
        if type_int == 1:
            name_int = int(input('''Select the number of your call:
            1)Red | 2)Black: '''))
            while name_int not in [1, 2]:
                    name_int = int(input('Invalid entry. Please choose 1 for Even or 2 for Odd: '))
            if name_int == 1:
                name = 'Red'
            else:
                name = 'Black'

        #even or odd selection (1 = even, 2 = odd)
        if type_int == 2:
            name_int = int(input('''Select the number of your call:
            1)Even | 2)Odd: '''))
            while name_int not in [1, 2]:
                name_int = int(input('Invalid entry. Please choose 1 for Even or 2 for Odd: '))
            if name_int == 1:
                name = 'Even'
            else:
                name = 'Odd'

        #straight selection (any single number)
        if type_int == 3:
            name = input('''Select the number of your call (0, 00, or any number between 1 through 36)''')
            while name not in list(wheel_dict.keys()):
                name = input('''Invalid entry. Select the number of your call (0, 00, or any number between 1 through 36)''')
            
        #split selection
        if type_int == 4:
            name_key = input('''Select the number for the split you would like to select as your call(numbers in brackets are split selection): 
            {0}'''.format(split_selection_string))
            while name_key not in list(split_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection (numbers in brackets are split selection): 
                {0}'''.format(split_selection_string))
            name = split_selection[name_key]

        #row selection
        if type_int == 5:
            print('Your call is on 0 and 00')
            name = ['0', '00']

        #street selection
        if type_int == 6:
            name_key = input('''Select the number for the street you would like to select as your call(numbers in brackets are street selection):
            {0}'''.format(street_selection_string))
            while name_key not in list(street_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection (numbers in brackets are street selection):
                {0}'''.format(street_selection_string))
            name = street_selection[name_key]

        #trio selection
        if type_int == 7:
            name_key = input('''Select the number for the trio you would like to select as your call(numbers in brackets are street selection):
            1) [0, 1, 2] | 2) [00, 2, 3]''')
            while name_key not in [1, 2]:
                name_key = input('''Invalid entry. Please choose from the following selection: 1) [0, 1, 2] | 2) [00, 2, 3]''')
            name = trio_selection[name_key]

        bet = int(input('Please enter your bet: '))
        
        while type(bet) != int:
            bet = int(input('Please enter in whole number for a bet: '))
        add_bet = int(input('''Would you like to make an additional bet?
        1)Yes | 2)No: '''))
        if add_bet == 2:
            break

    #generating the roulette wheel and the number the ball landed on
    winning_number = random.choice(american_wheel)
    winning_color = wheel_dict[winning_number]['color']
    print('The round goes to {0} {1}.'.format(winning_color, winning_number))

    #determine winners and losers

    #red-or-black type
    if type_int == 1:
        if winning_color == name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #even_orodd type
    if type_int == 2:
        if wheel_dict[winning_number]['even_odd'] == name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet
    
    #straight type
    if type_int == 3:
        if name == winning_number:
            print('Winner! Winner! You won {0}.'.format(bet * 35))
            return bet * 35
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet
    
    #split or row type
    if type_int == 4 or type_int == 5:
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 17))
            return bet * 17
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #street or trio type
    if type_int == 6 or type_int == 7:
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 11))
            return bet * 11
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #corner type
    if type_int == 8:
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 8))
            return bet * 8
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet
        
    #double street type
    if type_int == 9:
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet * 5))
            return bet * 5
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #basket type
    if type_int == 10:
        if winning_number in ['00', '0', '1', '2', '3']:
            print('Winner! Winner! You won {0}.'.format(bet * 6))
            return bet * 6
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #low-or-high type
    if type_int == 11:
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

    #dozen, column, or snake type
    if type_int == 12 or type_int == 13 or type_int == 14:
        if winning_number in name:
            print('Winner! Winner! You won {0}.'.format(bet))
            return bet * 2
        else:
            print('Better luck next time. You owe the house {0}.'.format(bet))
            return 0 - bet

