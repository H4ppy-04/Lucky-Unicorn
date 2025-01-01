"""
Lucky Unicorn Game.
Copyright (c) 2022-2025 Joshua Rose
"""

import os

from game import Game


def main():
    if not os.path.isfile("data/local.json"):
        with open("data/local.json", "w") as local, open("data/spec.json", "r") as spec:
            local.write(spec.read())
            local.close()

    game = Game()
    game.greet()
    game.show_prizes()
    input("Press enter to start playing. Good luck!")
    game.play()


if __name__ == "__main__":
    main()
