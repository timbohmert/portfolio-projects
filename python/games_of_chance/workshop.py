#routlette workshop to create tools uesed in function


#code to create template for each number of the roulette wheel, and adjust it from there (I don't know the sequential patter for red and black)
french_wheel = [i for i in range(0, 37)]
american_wheel = ['00'] + [str(x) for x in french_wheel]

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



#type selection string with all of the type options
type_selection = """1)Red or Black: bet on red or black
    2)Even or Odd: bet on even or odd number
    3)Straight: bet on a single number
    4)Split: bet on two vertically/horizontally adjacent numbers
    5)Row: bet on 0 and 00
    6)Street: bet on three consecutive numbers in a horizontal line
    7)Trio: bet on three-numbers that involves 0 or 00
    8)Corner: bet on four numbers that meet at one corner
    9)Double Street: bet on six numbers from two adjacent rows
    10)Basket: bet on 0-00-1-2-3
    11)Low or High: bet on 1-18 or 19-36
    12)Dozen: bet on 1-12, 13-14, or 25-36
    13)Column: bet on a vertical column of 12 numbers
    14)Snake: bet on 1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, and 34"""



#split selections
#horizontal split selections
num1 = 0
split_selection_horizontal_1 = {str(x + num1): [str(x), str(x + 1)] for x in range(1, 3)}
num1 -= 1
split_selection_horizontal_4 = {str(x + num1): [str(x), str(x + 1)] for x in range(4, 6)}
num1 -= 1
split_selection_horizontal_7 = {str(x + num1): [str(x), str(x + 1)] for x in range(7, 9)}
num1 -= 1
split_selection_horizontal_10 = {str(x + num1): [str(x), str(x + 1)] for x in range(10, 12)}
num1 -= 1
split_selection_horizontal_13 = {str(x + num1): [str(x), str(x + 1)] for x in range(13, 15)}
num1 -= 1
split_selection_horizontal_16 = {str(x + num1): [str(x), str(x + 1)] for x in range(16, 18)}
num1 -= 1
split_selection_horizontal_19 = {str(x + num1): [str(x), str(x + 1)] for x in range(19, 21)}
num1 -= 1
split_selection_horizontal_22 = {str(x + num1): [str(x), str(x + 1)] for x in range(22, 24)}
num1 -= 1
split_selection_horizontal_25 = {str(x + num1): [str(x), str(x + 1)] for x in range(25, 27)}
num1 -= 1
split_selection_horizontal_28 = {str(x + num1): [str(x), str(x + 1)] for x in range(28, 30)}
num1 -= 1
split_selection_horizontal_31 = {str(x + num1): [str(x), str(x + 1)] for x in range(31, 33)}
num1 -= 1
split_selection_horizontal_34 = {str(x + num1): [x, x + 1] for x in range(34, 36)}

split_selection_horizontal = {}

split_selection_horizontal.update(split_selection_horizontal_1)
split_selection_horizontal.update(split_selection_horizontal_4)
split_selection_horizontal.update(split_selection_horizontal_7)
split_selection_horizontal.update(split_selection_horizontal_10)
split_selection_horizontal.update(split_selection_horizontal_13)
split_selection_horizontal.update(split_selection_horizontal_16)
split_selection_horizontal.update(split_selection_horizontal_19)
split_selection_horizontal.update(split_selection_horizontal_22)
split_selection_horizontal.update(split_selection_horizontal_25)
split_selection_horizontal.update(split_selection_horizontal_28)
split_selection_horizontal.update(split_selection_horizontal_31)
split_selection_horizontal.update(split_selection_horizontal_34)



#vertical split selection
num2 = 24
split_selection_vertical_1 = {str(x + num2): [str(x), str(x + 3)] for x in range(1, 4)}
split_selection_vertical_4 = {str(x + num2): [str(x), str(x + 3)] for x in range(4, 7)}
split_selection_vertical_7 = {str(x + num2): [str(x), str(x + 3)] for x in range(7, 10)}
split_selection_vertical_10 = {str(x + num2): [str(x), str(x + 3)] for x in range(10, 13)}
split_selection_vertical_13 = {str(x + num2): [str(x), str(x + 3)] for x in range(13, 16)}
split_selection_vertical_16 = {str(x + num2): [str(x), str(x + 3)] for x in range(16, 19)}
split_selection_vertical_19 = {str(x + num2): [str(x), str(x + 3)] for x in range(19, 22)}
split_selection_vertical_22 = {str(x + num2): [str(x), str(x + 3)] for x in range(22, 25)}
split_selection_vertical_25 = {str(x + num2): [str(x), str(x + 3)] for x in range(25, 28)}
split_selection_vertical_28 = {str(x + num2): [str(x), str(x + 3)] for x in range(28, 31)}
split_selection_vertical_31 = {str(x + num2): [str(x), str(x + 3)] for x in range(31, 34)}

split_selection_vertical = {}

split_selection_vertical.update(split_selection_vertical_1)
split_selection_vertical.update(split_selection_vertical_4)
split_selection_vertical.update(split_selection_vertical_7)
split_selection_vertical.update(split_selection_vertical_10)
split_selection_vertical.update(split_selection_vertical_13)
split_selection_vertical.update(split_selection_vertical_16)
split_selection_vertical.update(split_selection_vertical_19)
split_selection_vertical.update(split_selection_vertical_22)
split_selection_vertical.update(split_selection_vertical_25)
split_selection_vertical.update(split_selection_vertical_28)
split_selection_vertical.update(split_selection_vertical_31)

split_selection = {}
split_selection.update(split_selection_horizontal)
split_selection.update(split_selection_vertical)

split_selection_string = '''Horizontal Splits:
1) [1, 2] | 2) [2, 3] | 3) [4, 5] | 4) [5, 6] | 5) [7, 8] | 6) [8, 9] | 7) [10, 11] | 8) [11, 12] | 9) [13, 14] | 10) [14, 15] | 11) [16, 17] | 12) [17, 18] | 13) [19, 20] | 14) [20, 21] | 15) [22, 23] | 16) [23, 24] | 17) [25, 26] | 18) [26, 27] | 19) [28, 29] | 20) [29, 30] | 21) [31, 32] | 22) [32, 33] | 23) [34, 35] | 24) [35, 36]
Vertical Split
25) [1, 4] | 26) [2, 5] | 27) [3, 6] | 28) [4, 7] | 29) [5, 8] | 30) [6, 9] | 31) [7, 10] | 32) [8, 11] | 33) [9, 12] | 34) [10, 13] | 35) [11, 14] | 36) [12, 15] | 37) [13, 16] | 38) [14, 17] | 39) [15, 18] | 40) [16, 19] | 41) [17, 20] | 42) [18, 21] | 43) [19, 22] | 44) [20, 23] | 45) [21, 24] | 46) [22, 25] | 47) [23, 26] | 48) [24, 27] | 49) [25, 28] | 50) [26, 29] | 51) [27, 30] | 52) [28, 31] | 53) [29, 32] | 54) [30, 33] | 55) [31, 34] | 56) [32, 35] | 57) [33, 36]:'''



#street selection
street_selection = {str(x): [y, y + 1, y + 2] for x, y in zip(range(1, 13), range(1, 35, 3))}

street_selection_string = '1) [1, 2, 3] | 2) [4, 5, 6] | 3) [7, 8, 9] | 4) [10, 11, 12] | 5) [13, 14, 15] | 6) [16, 17, 18] | 7) [19, 20, 21] | 8) [22, 23, 24] | 9) [25, 26, 27] | 10) [28, 29, 30] | 11) [31, 32, 33] | 12) [34, 35, 36]'


#trio selection
trio_selection = {'1': ['0', '1', '2'], '2': ['00', '2', '3']}


#corner selection
num1 = 0
corner_selection_1 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(1, 3)}
num1 -= 1
corner_selection_4 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(4, 6)}
num1 -= 1
corner_selection_7 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(7, 9)}
num1 -= 1
corner_selection_10 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(10, 12)}
num1 -= 1
corner_selection_13 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(13, 15)}
num1 -= 1
corner_selection_16 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(16, 18)}
num1 -= 1
corner_selection_19 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(19, 21)}
num1 -= 1
corner_selection_22 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(22, 24)}
num1 -= 1
corner_selection_25 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(25, 27)}
num1 -= 1
corner_selection_28 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(28, 30)}
num1 -= 1
corner_selection_31 = {str(x + num1): [str(x), str(x + 1), str(x + 3), str(x + 4)] for x in range(31, 33)}

corner_selection = {}

corner_selection.update(corner_selection_1)
corner_selection.update(corner_selection_4)
corner_selection.update(corner_selection_7)
corner_selection.update(corner_selection_10)
corner_selection.update(corner_selection_13)
corner_selection.update(corner_selection_16)
corner_selection.update(corner_selection_19)
corner_selection.update(corner_selection_22)
corner_selection.update(corner_selection_25)
corner_selection.update(corner_selection_28)
corner_selection.update(corner_selection_31)

corner_selection_string ='1) [1, 2, 4, 5] | 2) [2, 3, 5, 6] | 3) [4, 5, 7, 8] | 4) [5, 6, 8, 9] | 5) [7, 8, 10, 11] | 6) [8, 9, 11, 12] | 7) [10, 11, 13, 14] | 8) [11, 12, 14, 15] | 9) [13, 14, 16, 17] | 10) [14, 15, 17, 18] | 11) [16, 17, 19, 20] | 12) [17, 18, 20, 21] | 13) [19, 20, 22, 23] | 14) [20, 21, 23, 24] | 15) [22, 23, 25, 26] | 16) [23, 24, 26, 27] | 17) [25, 26, 28, 29] | 18) [26, 27, 29, 30] | 19) [28, 29, 31, 32] | 20) [29, 30, 32, 33] | 21) [31, 32, 34, 35] | 22) [32, 33, 35, 36]'



#double street selection
double_street_selection = {str(x): [str(y), str(y + 1), str(y + 2), str(y + 3), str(y + 4), str(y + 5)] for x, y in zip(range(1, 12), range(1, 35, 3))}

double_street_selection_string = '1) [1, 2, 3, 4, 5, 6] | 2) [4, 5, 6, 7, 8, 9] | 3) [7, 8, 9, 10, 11, 12] | 4) [10, 11, 12, 13, 14, 15] | 5) [13, 14, 15, 16, 17, 18] | 6) [16, 17, 18, 19, 20, 21] | 7) [19, 20, 21, 22, 23, 24] | 8) [22, 23, 24, 25, 26, 27] | 9) [25, 26, 27, 28, 29, 30] | 10) [28, 29, 30, 31, 32, 33] | 11) [31, 32, 33, 34, 35, 36]'



#low or high selection
low_or_high_selection = {str(x): [str(y), str(y + 1), str(y + 2), str(y + 3), str(y + 4), str(y + 5), str(y + 6), str(y + 7), str(y + 8), str(y + 9),  str(y + 10), str(y + 11), str(y + 12), str(y + 13), str(y + 14), str(y + 15), str(y + 16), str(y + 17)] for x, y in zip(range(1, 3), range(1, 37, 18))}



low_or_high_selection_string = '''1) ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '16', '18']
'2) ['19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '34', '36']'''



#dozen selection
dozen_selection = {str(x): [str(y), str(y + 1), str(y + 2), str(y + 3), str(y + 4), str(y + 5), str(y + 6), str(y + 7), str(y + 8), str(y + 9),  str(y + 10), str(y + 11)] for x, y in zip(range(1, 4), range(1, 37, 12))}


dozen_selection_string = '''1) ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
2) ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
3) ['25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']'''



#column selection
column_selection = {str(x): [str(x), str(x + 3), str(x + 6), str(x + 9),  str(x + 12), str(x + 15), str(x + 18), str(x + 21), str(x + 24), str(x + 27), str(x + 30), str(x + 33)] for x in range(1, 4)}

print(column_selection)


column_selection_string = '''1) ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28', '31', '34'] | 2) ['2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35'] | 3) ['3', '6', '9', '12', '15', '18', '21', '24', '27', '30', '33', '36']'''
