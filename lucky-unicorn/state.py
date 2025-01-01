import json

from prize import Prize


class State(object):

    def __init__(self):
        self.json_local = self.deserialize("data/local.json")
        self.json_prizes = self.deserialize("data/prizes.json")
        self.current_credits = self.json_local["credits"]["current"]
        self.starting_credits = self.json_local["credits"]["starting"]
        self.games_played = self.json_local["games_played"]
        self.step = self.json_local["step"]
        self.prizes_won = self.json_local["prizes_won"]
        self.prizes = [None, None]

        for prize in self.json_prizes:
            name = prize
            value = self.json_prizes[name]["value"]
            self.prizes.append(Prize(name, value))

    @staticmethod
    def deserialize(path):
        descriptor = open(path, "r")
        data = json.load(descriptor)
        descriptor.close()
        return data

    def serialize(self):
        return {
            "games_played": self.games_played,
            "prizes_won": self.prizes_won,
            "step": self.step,
            "credits": {
                "current": self.current_credits,
                "starting": self.starting_credits,
            },
        }

    def dump(self, path="data/local.json"):
        data = self.serialize()
        with open(path, "w") as fp:
            json.dump(data, fp, indent=4, sort_keys=True)
            fp.close()
