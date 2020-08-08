from random import randint
import sqlite3

# this connects our script to database
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS card (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0);''')
conn.commit()


def close():
    print("\nBye!\n")
    exit(0)


def card_generator(length):
    number = ''
    while len(number) != length:
        random_number = randint(0, 9)
        number = number + str(random_number)
    return number


class Luhn:
    def checksum_generator(self, card_number):
        total = self.luhn(card_number)
        checksum = 0
        while (total + checksum) % 10 != 0:
            checksum += 1
        return checksum

    def checksum_validation(self, card_number):
        total = self.luhn(card_number[0:len(card_number) - 1])
        total += int(card_number[-1])
        if total % 10 == 0:
            return True
        return False

    def luhn(self, card_number):
        summation = 0
        card_number = list(card_number)
        for i in range(0, len(card_number), 2):
            card_number[i] = int(card_number[i]) * 2
        for i in range(len(card_number)):
            if int(card_number[i]) > 9:
                card_number[i] = int(card_number[i]) - 9
        for i in range(len(card_number)):
            summation += int(card_number[i])
        return summation


class BankAccount:
    def __init__(self):
        self.logged = False
        self.card_storage = list()
        self.current_card = ''

    def new_card_entry(self, card_number, pin_number):
        items = card_number, pin_number
        cur.execute('INSERT INTO card (number, pin) VALUES (?,?)', items)
        conn.commit()

    def check_card(self, card_number):
        cur.execute('SELECT number FROM card')
        card = cur.fetchall()
        for number in card:
            if card_number == number[0]:
                return True
        return False

    def fetch_card_pin(self):
        cur.execute('SELECT number, pin FROM card')
        data = cur.fetchall()
        return data

    def new_account(self):
        print("\nYour card has been created")
        print("Your card number:")
        while True:
            new_card_number = '400000' + card_generator(9)
            checksum = Luhn().checksum_generator(new_card_number)
            new_card_number += str(checksum)
            if not self.check_card(new_card_number):
                break
        print(new_card_number)
        card_pin = card_generator(4)
        print("Your card PIN:")
        print(card_pin + "\n")
        self.new_card_entry(new_card_number, card_pin)
        self.card_storage.append(new_card_number)

    def log_in(self):
        print("\nEnter your card number:")
        card_input = input()
        print("Enter your PIN")
        pin_input = input()
        checksum_validation = Luhn().checksum_validation(card_input)
        pin_validation = False
        data = self.fetch_card_pin()
        for card, pin in data:
            if card_input == card and pin_input == pin:
                pin_validation = True
                break
        if pin_validation and checksum_validation:
            print("\nYou have successfully logged in!\n")
            self.logged = True
            self.current_card = card_input
        else:
            print("\nWrong card number or PIN!\n")

    def log_out(self):
        self.logged = False
        print("\nYou have successfully logged out!\n")

    def check_balance(self, only_check=True):
        cur.execute('SELECT number, balance FROM card')
        data = cur.fetchall()
        balance = 0
        for card, balances in data:
            if self.current_card == card:
                balance = balances
                break
        if not only_check:
            return balance
        print("\nBalance: {}\n".format(balance))

    def add_income(self):
        print("Enter income:")
        income = int(input())
        items = income, self.current_card
        cur.execute('UPDATE card SET balance = balance + ? WHERE number = ? ', items)
        conn.commit()
        print("Income was added!")

    def do_transfer(self):
        print("\nTransfer")
        print("Enter card number:")
        card = input()
        if Luhn().checksum_validation(card):
            if self.check_card(card):
                if self.current_card != card:
                    print("Enter how much money you want to transfer:")
                    transfer_money = int(input())
                    current_balance = self.check_balance(False)
                    if transfer_money < current_balance:
                        current_account = -transfer_money, self.current_card
                        cur.execute('UPDATE card SET balance = balance + ? WHERE number = ? ', current_account)
                        transfer_account = transfer_money, card
                        cur.execute('UPDATE card SET balance = balance + ? WHERE number = ? ', transfer_account)
                        conn.commit()
                        print("Success!\n")
                    else:
                        print("Not enough money!\n")
                else:
                    print("You can't transfer money to the same account!\n")
            else:
                print("Such a card does not exist.\n")
        else:
            print("Probably you made mistake in the card number. Please try again!\n")

    def close_account(self):
        items = self.current_card,
        cur.execute('DELETE FROM card WHERE number = ? ', items)
        conn.commit()
        print("The account has been closed!")

    def main(self):
        while True:
            first = "Create account" if not self.logged else "Balance"
            second = "Log into account" if not self.logged else "Add income"
            print("1. {}".format(first))
            print('2. {}'.format(second))
            if self.logged:
                print("3. Do transfer")
                print('4. Close account')
                print("5. Log out")
            print('0. Exit')
            user_input = int(input())
            if user_input == 1:
                self.new_account() if not self.logged else self.check_balance()
            elif user_input == 2:
                self.log_in() if not self.logged else self.add_income()
            elif user_input == 3 and self.logged:
                self.do_transfer()
            elif user_input == 4 and self.logged:
                self.close_account()
            elif user_input == 5 and self.logged:
                self.log_out()
            elif user_input == 0:
                close()
            else:
                print("Wrong Input")


banking = BankAccount()
banking.main()
# print(Luhn().checksum_generator('400000493832089'))
# print(Luhn().checksum_validation('4000004938320896'))
