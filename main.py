import random       # to generate slot machine values randomly

'''
Build a text based slot machine
How it work: The user will deposit a certain amount of money. We then allow
them to bet on either one, two or three line of the slot machine just to
keep it pretty simple (whereas real slot machines have lot more lines than that)
And then we are going to determine if they want. So if they got any lines,
we are going to multiply their bet by the value of the line, add that to their
balance, and then allow them to keep playing untill they want to cash out or
untill they run out of money.
This is actually a fairly complex project because we need to do a lot of things
We need to;
    > collect the users deposit
    > add that to their balance
    > allow them to bet on a line or mutiple lines
    > see if they actually got any of those lines
    > spin the slot machine
    > generate the different items that are going to be in the slot machine on the different reels
    > add what ever they won back to their balance
'''

MAX_LINES = 3       # Global constant value
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    # this functions checks if the each row values are equals and for the number of lines the user bet on
    # also assumes that if user bets on 1 line, then it would be the 1st line (0 element) and user cannot choose the line.
    winnings = 0
    winning_lines = []
    for line in range(lines):       # loop through each row
        symbol = columns[0][line]   # the symbol requires to be check would be the symbol in the 1st column of the current row
        for column in columns:      # loop through every single column
            symbol_to_check = column[line]      # matching the symbol to the current symbol at the current row that we are looking at
            if symbol != symbol_to_check:       # check if the symbols are not the same
                break                           # if not the same move to the next line
        else:
            # this is for else statement. This gets executed if the loop didn't 'break'
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    '''
    :param rows:
    :param cols:
    :param symbols:
    :return:

    these would be 3 parameters that would be passed to this function.
    And inside, we use these parameters.
    Inside of this function, what we need to do is to generate
    what symbols are going to be in each column based on the frequency
    of symbols that we have here. So we essentially need to randomly pick the number
    of rows inside of each column. So if we have 3 rows, need to pick 3 symbols
    that go inside of each of the columns that we have. And for each column we are
    doing kind of a new random pick r new random generation of symbols.
    '''
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    '''
    What is gonna happen in the above is we are going to loop through this dictionary
    Let's imagine we are on the 1st key value pair, our symbol going to be 'A' and our
    symbol count going to be 2. Then we have another for loop inside of here where we are 
    looping through the symbol count. So the symbol count is 2 and what we doing is, doing this 2 times.
    So we going to add this symbol twice into our all symbols list.
    
    Now that we have the all symbols list, we need to select what value are going to go
    into every single column.
    '''

    # columns = [[], [], []]      # this is a nested list
    columns = []      # this is a nested list
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]        # this is how you copy a list. This is operator here is referred to as
                                                # the operator. If this operator is not specified any changes to
                                                # all_symbols would be applied to current_sybols as well (reference)
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machines(columns):
    '''
    :param columns:
    :return:
    this function would print the slot machine by transposing the columns
    We loop through every single row that we have for every single row we loop through
    every column and for every column we only print the current row that we are on.
    So in row 0, all of the elements in row 0/1 then row then row two. This essentially
    transposes or flips out columns from being horizontal to be vertical.
    '''
    for row in range(len(columns[0])):
        # columns[0] is specified to ensure we always have one column, this avoid crashing
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                # print(column[row], "|")
                # by default print() would add a \n (new line) at the end of each statement
                # printed. To override this we can use 'end=" | "' or end="".
                print(column[row], end=" | ")
            else:
                print((column[row]), end="")

        print()     # prints the new line char


def deposit():
    while True:
        # loop while user enters a valid amount
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        # lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        # loop while user enters a valid amount
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")  # the 'f' function is only available in Python 3.6 and above
                # print ("Bet must be between $" + str(MIN_BET) + " - $" + str(MAX_BET) + ".")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    # Check if total bet is within available deposit balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            # print("You do not have enough to bet that amount, you current balance is: $" + str(balance))
            print(f"You do not have enough to bet that amount, you current balance is: ${balance}")
        else:
            break
    # print(f"You are betting $ " + str(bet) + " on " + str(lines) + " lines. Total bet is equal to: $" + str(total_bet))
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    # print("You won $" + str(winnings) + ".")
    # print("You won on lines: " + str(winning_lines))

    if winnings > 0:
        print(f"You won ${winnings}.")
        if winning_lines:
            print(f"You won on ", *winning_lines)     # the '*' is called the splat/ unpack operator. It's gonna pass evey
                                                        # single line from this list to the print() function. What it means is
                                                        # if we hav elnies like one and tow, it's going to pass both one and two.
                                                        # So this gives you one on and then one, two
    else:
        print("Oh, you weren't successful! Give another go.")

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        # print("Current balance is $ " + str(balance))
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    # print("You left with $ " + str(balance))
    print(f"You left with ${balance}")


main()