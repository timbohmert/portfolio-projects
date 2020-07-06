#Project Goal (supplied by Codecademy): You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

#imported libraries supplied by Codecademy
import random
##GAME OF CHANCE FUNCTIONS##


#coin flip
def coin_flip(wallet):
    print('\nWelcome to Tim\'s Silver Coin Flip! All bets are final. Good luck!')
    
    #taking in user selection of call (1 = Heads, 2 = Tails) and the quantity of their bet
    call_int = int(input('''Select the number of your call:
    1)Heads | 2)Tails: '''))
    while call_int not in [1, 2]:
            call_int = int(input('Please choose 1 for Heads or 2 for Tails: '))
    if call_int == 1:
        call = 'Heads'
    else:
        call = 'Tails'
    while True:
        bet = int(input('Please enter your bet: '))
        if type(bet) != int:
            print('Please enter in whole number for a bet: ')
            continue
        if bet > wallet:
            print('You don\'t have enough in your wallet. Please decrease the amount of your bet: ')
            continue
        break

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
def cho_han(wallet):
    print('\nWelcome to on Tim\'s Cho-Han Rumble! All bets are final. Good luck!')

    #taking in user selection of call (1 = Even, 2 = Odd) and the quantity of their bet
    call_int = int(input('''Select the number of your call:
    1)Even | 2)Odd: '''))
    while call_int not in [1, 2]:
            call_int = int(input('Please choose 1 for Even or 2 for Odd: '))
    bet = int(input('Please enter your bet: '))
    if call_int == 1:
        call = 'Even'
    else:
        call = 'Odd'
    while True:
        bet = int(input('Please enter your bet: '))
        if type(bet) != int:
            print('Please enter in whole number for a bet: ')
            continue
        if bet > wallet:
            print('You don\'t have enough in your wallet. Please decrease the amount of your bet: ')
            continue
        break

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
def high_card(wallet):
    print('\nWelcome to Tim\'s High Card Shenanigans! Aces are high and all bets are final. Good luck!')

    #taking in user the quantity of their bet
    while True:
        bet = int(input('Please enter your bet: '))
        if type(bet) != int:
            print('Please enter in whole number for a bet: ')
            continue
        if bet > wallet:
            print('You don\'t have enough in your wallet. Please decrease the amount of your bet: ')
            continue
        break

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


from workshop import wheel_dict, american_wheel, type_selection, split_selection, split_selection_string, street_selection, street_selection_string, trio_selection, corner_selection, corner_selection_string, double_street_selection, double_street_selection_string, low_or_high_selection, low_or_high_selection_string, dozen_selection, dozen_selection_string, column_selection, column_selection_string


#function for roulette game
def roulette(wallet):
    print('\nWelcome to Tim\'s Spin-to-Win Roulette! All bets are final. Good luck!')

    #taking in user selection for type of bet and tracks the bet total to see if enough in wallet
    bet_dict = {}
    total_bet = 0
    while True:
        type_int = int(input('''Select the number for the type of bet you would like to make for the next spin: 
    {0}
    : '''.format(type_selection)))
        while type_int not in list(range(1,15)):
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
            name_key = input(
            '''Select the number for the split you would like to select as your call(numbers in brackets are split selection): 
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
            name_key = input(
            '''Select the number for the street you would like to select as your call(numbers in brackets are street selection):
            {0}'''.format(street_selection_string))
            while name_key not in list(street_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection (numbers in brackets are street selection):
                {0}'''.format(street_selection_string))
            name = street_selection[name_key]

        #trio selection
        if type_int == 7:
            name_key = int(input(
            '''Select the number for the trio you would like to select as your call(numbers in brackets are street selection):
            1) [0, 1, 2] | 2) [00, 2, 3]'''))
            while name_key not in [1, 2]:
                name_key = input('''Invalid entry. Please choose from the following selection: 1) [0, 1, 2] | 2) [00, 2, 3]''')
            name = trio_selection[name_key]

        #corner selection
        if type_int == 8:
            name_key = input(
            '''Select the number for the corner you would like to select as your call(numbers in brackets are corner selection):
            {0}'''.format(corner_selection_string))
            while name_key not in list(corner_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection (numbers in brackets are street selection):
                {0}'''.format(corner_selection_string))
            name = corner_selection[name_key]

        #double street selection
        if type_int == 9:
            name_key = input(
            '''Select the number for the double street you would like to select as your call(numbers in brackets are double street selection):
            {0}'''.format(double_street_selection_string))
            while name_key not in list(double_street_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection (numbers in brackets are double street selection):
                {0}'''.format(double_street_selection_string))
            name = double_street_selection[name_key]

        #basket selection
        if type_int == 10:
            print('Your call is on [0, 00, 1, 2, 3].')
            name = ['0', '00', '1', '2', '3']

        # low or high selection
        if type_int == 11:
            name_key = input(
            '''Select the number for your call:
            {0}'''.format(low_or_high_selection_string))
            while name_key not in list(low_or_high_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection:
                {0}'''.format(low_or_high_selection_string))
            name = low_or_high_selection[name_key]

        #dozen selection
        if type_int == 12:
            name_key = input(
            '''Select the number for your call:
            {0}'''.format(dozen_selection_string))
            while name_key not in list(dozen_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection:
                {0}'''.format(dozen_selection_string))
            name = dozen_selection[name_key]

        #column selection
        if type_int == 13:
            name_key = input(
            '''Select the number for your call:
            {0}'''.format(column_selection_string))
            while name_key not in list(column_selection.keys()):
                name_key = input('''Invalid entry. Please choose from the following selection:
                {0}'''.format(column_selection_string))
            name = column_selection[name_key]

        #snake selection
        if type_int == 14:
            print('Your call is on [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34].')
            name = ['1', '5', '9', '12', '14', '16', '19', '23', '27', '30', '32', '34']

        
        while True:
            bet = int(input('Please enter your bet: '))
            total_bet += bet
            if type(bet) != int:
                print('Please enter in whole number for a bet: ')
                continue
            if total_bet > wallet:
                print('You don\'t have enough in your wallet. Please decrease the amount of your bet: ')
                total_bet -= bet
                continue
            break
        
        #adding the single bet into the dictionary
        if type_int not in bet_dict.keys():
            bet_dict[type_int] = {'names': [name], 'bets': [bet]}
        else:
            bet_dict[type_int]['names'] += [name]
            bet_dict[type_int]['bets'] += [bet]

        #option to add additional bets
        add_bet = int(input('''Would you like to make an additional bet?
        1)Yes | 2)No: '''))
        while add_bet not in [1, 2]:
            int(input('''Please enter 1 if you would like to make an additional bet or 2 if you don't want to make any additional bets.'''))
        if add_bet == 2:
            break

    #bets statement
    bets_string = 'Your bets for the round are '
    for value in bet_dict.values():
        bets_string += str(value['names'])
    print(bets_string)


    #generating the roulette wheel and the number the ball landed on
    winning_number = random.choice(american_wheel)
    winning_color = wheel_dict[winning_number]['color']
    print('The round goes to {0} {1}.'.format(winning_color, winning_number))

    #determine winners and losers and total winning

    total_winning = 0

    #red-or-black type
    if 1 in bet_dict.keys():
        for i in range(len(bet_dict[1]['names'])): 
            if winning_color == bet_dict[1]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[1]['bets'][i]))
                total_winning += bet_dict[1]['bets'][i]
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[1]['bets'][i]))
                total_winning -= bet_dict[1]['bets'][i]

    #even_orodd type
    if 2 in bet_dict.keys():
        for i in range(len(bet_dict[2]['names'])): 
            if wheel_dict[winning_number]['even_odd'] == bet_dict[2]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[2]['bets'][i]))
                total_winning += bet_dict[2]['bets'][i]
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[2]['bets'][i]))
                total_winning -= bet_dict[2]['bets'][i]
    
    #straight type
    if 3 in bet_dict.keys():
        for i in range(len(bet_dict[3]['names'])): 
            if winning_number == bet_dict[3]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[3]['bets'][i] * 35))
                total_winning += bet_dict[3]['bets'][i] * 35
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[3]['bets'][i]))
                total_winning -= bet_dict[3]['bets'][i]
    
    #split type
    if 4 in bet_dict.keys():
        for i in range(len(bet_dict[4]['names'])): 
            if winning_number == bet_dict[4]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[4]['bets'][i] * 17))
                total_winning += bet_dict[4]['bets'][i] * 17
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[4]['bets'][i]))
                total_winning -= bet_dict[4]['bets'][i]
    
    #row type
    if 5 in bet_dict.keys():
        for i in range(len(bet_dict[5]['names'])): 
            if winning_number == bet_dict[5]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[5]['bets'][i] * 17))
                total_winning += bet_dict[5]['bets'][i] * 17
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[4]['bets'][i]))
                total_winning -= bet_dict[4]['bets'][i]

    #street or trio type
    if 6 in bet_dict.keys():
        for i in range(len(bet_dict[6]['names'])): 
            if winning_number == bet_dict[6]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[6]['bets'][i] * 11))
                total_winning += bet_dict[6]['bets'][i] * 11
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[6]['bets'][i]))
                total_winning -= bet_dict[6]['bets'][i]

    #trio type
    if 7 in bet_dict.keys():
        for i in range(len(bet_dict[7]['names'])): 
            if winning_number == bet_dict[7]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[7]['bets'][i] * 11))
                total_winning += bet_dict[7]['bets'][i] * 11
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[7]['bets'][i]))
                total_winning -= bet_dict[7]['bets'][i]

    #corner type
    if 8 in bet_dict.keys():
        for i in range(len(bet_dict[8]['names'])): 
            if winning_number == bet_dict[8]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[8]['bets'][i] * 8))
                total_winning += bet_dict[8]['bets'][i] * 8
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[8]['bets'][i]))
                total_winning -= bet_dict[8]['bets'][i]
        
    #double street type
    if 9 in bet_dict.keys():
        for i in range(len(bet_dict[9]['names'])): 
            if winning_number == bet_dict[9]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[9]['bets'][i] * 5))
                total_winning += bet_dict[9]['bets'][i] * 5
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[9]['bets'][i]))
                total_winning -= bet_dict[9]['bets'][i]

    #basket type
    if 10 in bet_dict.keys():
        for i in range(len(bet_dict[10]['names'])): 
            if winning_number == bet_dict[10]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[10]['bets'][i] * 6))
                total_winning += bet_dict[10]['bets'][i] * 6
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[10]['bets'][i]))
                total_winning -= bet_dict[10]['bets'][i]

    #low-or-high type
    if 11 in bet_dict.keys():
        for i in range(len(bet_dict[11]['names'])): 
            if winning_number == bet_dict[11]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[11]['bets'][i]))
                total_winning += bet_dict[11]['bets'][i]
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[11]['bets'][i]))
                total_winning -= bet_dict[11]['bets'][i]

    #dozen type
    if 12 in bet_dict.keys():
        for i in range(len(bet_dict[12]['names'])): 
            if winning_number == bet_dict[12]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[12]['bets'][i] * 2))
                total_winning += bet_dict[12]['bets'][i] * 2
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[12]['bets'][i]))
                total_winning -= bet_dict[12]['bets'][i]

    #column type
    if 13 in bet_dict.keys():
        for i in range(len(bet_dict[13]['names'])): 
            if winning_number == bet_dict[13]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[13]['bets'][i] * 2))
                total_winning += bet_dict[13]['bets'][i] * 2
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[13]['bets'][i]))
                total_winning -= bet_dict[13]['bets'][i]

    #snake type
    if 14 in bet_dict.keys():
        for i in range(len(bet_dict[14]['names'])): 
            if winning_number == bet_dict[14]['names'][i]:
                print('Winner! Winner! You won {0}.'.format(bet_dict[14]['bets'][i] * 2))
                total_winning += bet_dict[14]['bets'][i] * 2
            else:
                print('Better luck next time. You owe the house {0}.'.format(bet_dict[14]['bets'][i]))
                total_winning -= bet_dict[14]['bets'][i]

    #total winnings
    if total_winning >= 0:
        print('Your total winnings are {0} for the round.'.format(total_winning))
    else:
        print('Your losses for the round are {0}'.format(total_winning))
    return total_winning

