import os
import sys
import time
from dataclasses import dataclass
from random import choice as choose_from
from typing import Optional

from colorama import Fore, init

from prize import Prize
from state import State


class Game(State):

    def __init__(self):
        init()
        super(Game, self).__init__()

    def greet(self):
        name = os.getenv("USER", default="friend")
        if self.games_played == 0:
            print(f"Hey {name}, welcome to the Lucky Unicorn Game!")
        else:
            print(f"Hey {name}, welcome back!")

    def show_prizes(self):
        for prize in self.prizes:
            if prize != None:
                prize.print_contents_entry()

    def wait(self, interval=0.5):
        """Builds suspense...."""

        def inc(i, t):
            print("." * i)
            time.sleep(t)

        [inc(i, interval) for i in range(1, 4)]

    def load_prize(self) -> Optional[Prize]:
        """Loads a prize from the prize pool."""
        self.wait()
        prize: Optional[Prize] = choose_from(self.prizes)
        return prize

    def pay_round_fee(self):
        if self.current_credits >= 1.0:
            color = Fore.LIGHTRED_EX
            print(f"{color} - $1.0 round fee" + Fore.RESET)
            self.current_credits -= 1.0
            print(f" (${round(self.current_credits, 2)} remaining)")
            self.games_played += 1
        else:
            print(f"Round fee is $1.0. Your balance is {self.current_credits}")
            sys.exit()

    def start_round(self):
        prize: Optional[Prize] = self.load_prize()

        if isinstance(prize, Prize) is not True:
            print("Sorry, you did not win anything.\n")
        else:
            self.prizes_won.append(prize.name)
            self.current_credits += prize.value
            print(prize.artwork())
            print(f"Congratulations! You got a {prize.name} worth ${prize.value}.\n")

    def end_round(self):
        if input("Play again? [n,Y*] > ").lower() not in ["y", ""]:
            self.dump(path="local.json")
            sys.exit("See you next time!")

    def play(self):
        while True:
            self.wipe_screen()
            self.pay_round_fee()
            self.start_round()
            self.end_round()

    @staticmethod
    def wipe_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
