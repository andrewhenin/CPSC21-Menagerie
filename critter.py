"""
This program define a Critter class that will be used in other programs.
Name: Andrew Henin
Date: April 2022
"""

class Critter:
    def __init__(self, name, status, personal, posessive, food):
        """
        Constructor; parameters are initial values for:
          name (string), type (string), prepron (string), pospron  (string),
          food (string), fedCount (integer), pettedCount (integer),
          playedCount (integer)
          personal = personal pronoun; posseesive = posessive pronoun
        """
        self.name = name
        self.status = status
        self.personal = personal
        self.posessive = posessive
        self.food = food
        self.fedCount = 0
        self.pettedCount = 0
        self.playedCount = 0

    def get_name(self):
        return self.name


    def __str__(self):

        if self.fedCount == 0:
            fedstatus = "hungry"
        elif self.fedCount == 1:
            fedstatus = "well fed"
        elif self.fedCount == 2:
            fedstatus = "full"
        elif self.fedCount > 2:
            fedstatus = "overfull"

        if self.pettedCount == 0:
            pettedstatus = "sad"
        elif self.pettedCount > 0:
            pettedstatus = "happy"

        if self.playedCount == 0:
            playedstatus = "bored"
        elif self.playedCount > 0:
            playedstatus = "playful"

        str1 = self.name + " is " + self.status + "; "
        str2 = self.personal + " looks " + fedstatus + ", " + \
        pettedstatus + ", and " + playedstatus + "."

        return str1 + str2


    def pet(self):
        self.pettedCount += 1
        return self.name + " is " + self.status + ", and " + self.personal + \
        " enjoys " + self.posessive + " pets!"


    def feed(self):
        if self.fedCount <= 2:
            self.fedCount += 1
            return self.name + " is " + self.status + ", and " + self.personal\
            + " enjoys " + self.posessive + " " + self.food + "!"
        elif self.fedCount > 2:
            return self.name + " is overfull" + ", and " + \
            self.personal + "doesn't want to eat more " + self.food + "."


    def play(self):
        self.playedCount += 1
        return self.name + " is " + self.status + ", and " + self.personal + \
        " enjoys playing!"


    def sleep(self):
        if self.fedCount > 0:
            self.fedCount -= 1
        if self.pettedCount > 0:
            self.pettedCount -= 1
        if self.playedCount > 0:
            self.playedCount -= 1
        return self.name + " is going to sleep."


def main():
    """playedstatus
    main function for testing the class
    """

    print("Running tests for Critter class...")

    print("Testing constructor...")
    zibby = Critter("Zibby", "fluffy", "he", "his", "food", \
    0, 0, 0)

    print("Testing to-string...")
    print(zibby)

    print("Testing getter methods...")
    print(zibby.get_name())

    print("testing other methods...")
    print(zibby.__str__())
    print(zibby.pet())
    print(zibby.feed())
    print(zibby.play())
    print(zibby.sleep())


if (__name__ == "__main__"):
  main()
