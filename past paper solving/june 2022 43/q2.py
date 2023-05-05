class Balloon:
    def __init__(self, DefenceItem, Colour):
        self.__DefenceItem = DefenceItem  # Private
        self.__Colour = Colour  # Private
        self.__Health = 100

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, Health):
        self.__Health = self.__Health + Health

    def CheckHealth(self):
        return self.__Health <= 0


def Defend(Balloon):
    Strength = int(input("Enter Opponent Strength"))
    Balloon1.ChangeHealth(-Strength)
    print(Balloon1.GetDefenceItem())
    if Balloon1.CheckHealth():
        print("No Health Remaining")
    else:
        print("Health Remaining")
    return Balloon


# main
DefenceItem = input("Enter Defence Item")
Colour = input("Enter Colour")

Balloon1 = Balloon(DefenceItem, Colour)
Balloon1 = Defend(Balloon1)
