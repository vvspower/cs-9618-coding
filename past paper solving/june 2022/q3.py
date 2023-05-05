import pickle


class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number  # Private
        self.__Colour = Colour  # Private

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


CardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

try:
    CardFile = open('CardValues.txt', 'rw')
    for x in range(0, 30):
        number = CardFile.readline()
        colour = CardFile.readline()
        CardArray[x] = Card(number, colour)
except IOError:
    print("could not find file")

global selected
selected = []


def ChooseCard():
    global selected
    card_selected = False
    while not card_selected:
        Number = int(input("Select Card"))
        if Number >= 1 and Number <= 30:
            if Number not in selected:
                card_selected = True
                selected.append(Number)
                return Number
            else:
                print("Card already selected, Choose another")
        else:
            print("Enter number between 1 and 30")


Player1 = []
for x in range(0, 4):
    number = ChooseCard()
    Player1.append(CardArray[number])

for x in range(0, 4):
    print(Player1[x].GetColour())
    print(Player1[x].GetNumber())
