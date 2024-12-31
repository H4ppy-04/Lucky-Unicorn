import collections
import decimal
import random
import time

import colorama

# Statistics
local = {
    "games_played": 0,
    "prizes_won": [],
    "highest_currency": 0,
    "goodbye_quit": "Sorry to see you go. Here's some of your final statistics:",
    "goodbye_lost": "You have run out of money. Here's some statistics:",
    "max_value": 50,
    "step_val": 0.1,
}

# Init display
colorama.init()

float_range_list = []
balance = 0.0
tokens = {
    "donkey": {"value": 0.0, "art": r""""""},
    "zebra": {
        "value": 0.5,
        "art": r"""
	  \\/),
	   ,'.' /,
	  (_)- / /,
		 /\_/ |__..--,  *
		(\___/\ \ \ / ).'
		 \____/ / (_ //
		  \\_ ,'--'\_(
		  )_)_/ )_/ )_)
		 (_(_.'(_.'(_.'
	 """,
    },
    "horse": {
        "value": 1.0,
        "art": r"""
				,--,
		  _ ___/ /\|
		 ;( )__, )
		; //   '--;
		  \     |
		   ^    ^
   """,
    },
    "unicorn": {
        "value": 2.0,
        "art": r"""
			   _ ____
			 /( ) _   \
			/ //   /\` \,  ||--||--||-
			  \|   |/  \|  ||--||--||-
		~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^
	""",
    },
}
print(
    """Welcome to the Lucky Unicorn Game!
  Donkey ..... $0.00
  Zebra ...... $0.50
  Horse ...... $1.00
  Unicorn .... $2.00
	  
How much money would you like to play with? (max $50)"""
)


def build_up_suspense() -> None:
    """Builds up suspense. Fairly self-explanatory"""
    print(".")
    time.sleep(0.6)
    print("..")
    time.sleep(0.6)
    print("...")
    time.sleep(0.6)
    print("....")


def float_range(start=0, stop=local["max_value"] + 1, step=local["step_val"]) -> None:
    """Generator function for yield_range"""
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)


def yield_range() -> None:
    """Uses generator to return total value when called upon by float_range"""
    global float_range_list
    float_range_list = [i for i in list(float_range())]


def get_token(arr=tokens) -> str:
    """Returns a random key from tokens"""
    token = random.choice([i for i in tokens])
    local["prizes_won"].append(token)
    if token == "donkey":
        token = None
    return token


def balance_regulator(x) -> bool:
    """input conditional regulation which returns a boolean datatype"""
    global balance
    try:
        if x in float_range_list:
            print(
                f"You've selected a value of: {colorama.Fore.LIGHTGREEN_EX}${str(int(x))}{colorama.Fore.WHITE}\n"
            )
            balance = x
            local["highest_currency"] = x
            return True
        else:
            print(
                f"{colorama.Fore.LIGHTRED_EX}{str(int(x))} not in range;{colorama.Fore.WHITE} Please input a number between {colorama.Fore.LIGHTYELLOW_EX}1 - 50{colorama.Fore.WHITE}"
            )
            return False
    except TypeError:
        print(
            f"{colorama.Fore.LIGHTRED_EX}Please enter an operable datatype; {colorama.Fore.WHITE}exclusively an integer"
        )
        return False
    except ValueError:
        print(
            f"{colorama.Fore.LIGHTRED_EX}Invalid value operation between range;{colorama.Fore.WHITE} please enter a correct ranged integer"
        )
        return False


# Add value to placeholder variables
yield_range()

while balance == 0.0:
    balance_regulator(float(input(" $ ")))

input("Great! Press enter to start playing.")

while balance >= 1.0:
    token = get_token()
    try:
        build_up_suspense()
        if not token:
            print("Sorry, you did not win anything.\n")
            continue
        else:
            balance += tokens[token]["value"]
            print(tokens[token]["art"])
            print(f"You got a ${str(tokens[token]['value'])} {token.capitalize()}! \n ")
            print(
                f"{colorama.Fore.LIGHTGREEN_EX} + ${str(tokens[token]['value'])}{colorama.Fore.WHITE}"
            )
            continue
    finally:
        balance -= 1.0
        print(
            f"{colorama.Fore.LIGHTRED_EX} - $1.0 round fee{colorama.Fore.WHITE}\n (${str(int(balance))} remaining)\n"
        )
        local["games_played"] += 1
        if input("[y | n] Would you like to play again? > ").lower() == "y":
            continue
        else:
            print(f"\n{local['goodbye_quit']}")
            print("-" * len(local["goodbye_quit"]))
            break

if balance < 1:
    print(local["goodbye_lost"])
    print("-" * len(local["goodbye_lost"]))

print(
    f"""You played {str(local['games_played'])} round(s)
Your highest currency was ${str(local['highest_currency'])}
Your average prize was a {str(collections.Counter(local['prizes_won']).most_common(1)[0][0]).capitalize()}
"""
)
