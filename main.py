import sys

from game import Game


def main():
    game = Game()

    if "--reset" in sys.argv:
        with open("local.json", "w") as local, open("spec.json", "r") as spec:
            local.write(spec.read())

    game.greet()
    game.show_prizes()

    input("Press enter to start playing. Good luck!")
    game.play()


if __name__ == "__main__":
    main()
