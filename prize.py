import os
from dataclasses import dataclass


@dataclass
class Prize:
    name: str
    value: float

    def get_artwork_file(self):
        return os.path.join("animals", (self.name + ".txt"))

    def artwork(self):
        path = self.get_artwork_file()
        descriptor = open(path, "r")
        contents = descriptor.read()
        descriptor.close()
        print(contents)

    def print_contents_entry(self):
        """Print table of contents specific price"""
        length = len(self.name)
        distance = 11 - length
        dots = "." * distance
        value = f"{self.name} {dots} ${self.value}"
        print(value)
