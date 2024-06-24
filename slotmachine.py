import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMS = 3

symbols_count= {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value= {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}




def check_winnings(columns , lines , bet , values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = columns[lines]
            if symbol != symbol_to_check:
                break
            else:
                winning_lines.append(lines)

    return winnings , winning_lines






def slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

    columns.append(column)
    return columns


# -------------------------------------------------------
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
              print(column[row], end=" ")
        print()

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
        else:
            print(column[row], end="")

        print()



# ---------------------------------------------------------

def desposit():
    while True:
        amount = input("what you would like to seposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0 to play')
        else:
            print('please enter a number: ')

    return amount


# -------------------------------------------------------------
def get_nmber_of_lines():
    while True:
        Lines = input(f"How many lines would ypu like to bet on (1-{MAX_LINES})? ")
        if Lines.isdigit():
            Lines = int(Lines)
            if 1 <= Lines <= MAX_LINES:
                break
            elif Lines <= 0:
                print('Lines should be more than 0 to play')
            elif Lines >= MAX_LINES:
                print('you cant choose more than 3 lines')
        else:
            print('please enter a number: ')
    return Lines


# -----------------------------------------------------------
def get_bet():
    while True:
        amount = input("what you would like to bet On each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            elif amount <= MIN_BET:
                print('your amount to bet must be greater than 0$')
            elif amount >= MAX_BET:
                print('you cant bet more than 100$ on each line')
        else:
            print('please enter a number: ')

    return amount


# ----------------------------------------------------------
def spin():
    balance = desposit()
    line = get_nmber_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * line
        if total_bet > balance:
            print(
                f'you dont have enough money to bet,youre current balnce is {balance}$,you should charge your wallet ')
        else:
            break
    print(f'you are betting {bet}$ on {line}line and you are betting {total_bet} in general from your wallet')
    print(balance, line, bet)
    slots = slot_machine_spin(ROWS, COLUMS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, line, bet, symbol_value)
    print(f'you won {winnings}')
    print(f'you won on', *winning_lines)
    return winnings - total_bet

def main():
    balance = desposit()
    while True:
        print(f"current balance is {balance}$")
        amswer =input('press enter to spin (q to quit):')
        if amswer == 'q':
            break

        balance += spin()
    print(f'you left with {balance}$')






main()
