class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number  # private
        self.__Colour = Colour  # private

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.Cards = []  # of type Card
        self.FirstCard = 0
        self.NumberCards = 5

        self.Cards.append(Card1)
        self.Cards.append(Card2)
        self.Cards.append(Card3)
        self.Cards.append(Card4)
        self.Cards.append(Card5)

    def GetCard(self, index):
        return self.Cards[index]


def CalculateValue(Hand):
    TotalScore = 0
    for x in range(0, 5):
        Card = Hand.GetCard(x)
        TotalScore = TotalScore + Card.GetNumber()
        if Card.GetColour() == "red":
            TotalScore = TotalScore + 5
        if Card.GetColour() == "blue":
            TotalScore = TotalScore + 10
        if Card.GetColour() == "yellow":
            TotalScore = TotalScore + 15
    return TotalScore


Player1 = Hand(Card(1, "red"), Card(3, "red"), Card(
    3, "red"), Card(4, "red"), Card(5, "yellow"))
Player2 = Hand(Card(2, "yellow"), Card(3, "yellow"), Card(
    4, "yellow"), Card(5, "yellow"), Card(1, "blue"))

PLayer1Score = CalculateValue(Player1)
Player2Score = CalculateValue(Player2)

print(PLayer1Score, Player2Score)

if PLayer1Score > Player2Score:
    print("Player 1 Wins!")
elif PLayer1Score == Player2Score:
    print("It is a Draw!")
else:
    print("Player 2 Wins!")


# Card = Card(1, "red")
# Card = Card(2, "red")
# Card = Card(3, "red")
# Card = Card(4, "red")
# Card = Card(5, "red")
# Card = Card(1, "blue")
# Card = Card(2, "blue")
# Card = Card(3, "blue")
# Card = Card(4, "blue")
# Card = Card(5, "blue")
# Card = Card(1, "yellow")
# Card = Card(2, "yellow")
# Card = Card(3, " yellow")
# Card = Card(4, "yellow")
# Card = Card(5, "yellow")
