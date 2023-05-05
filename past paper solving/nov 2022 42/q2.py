class Character:
    def __init__(self, Name, XCoordinate, YCoordinate):
        self.__Name = Name  # string #private
        self.__XCoordinate = XCoordinate  # integer # private
        self.__YCoordinate = YCoordinate  # integer # private

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange


# main

CharacterArray = ["", "", "", "", "", "", "", "", "", ""]  # Character

File = open("Characters.txt", 'r')
for x in range(0, 10):
    try:
        character = File.readline()
        Xcord = int(File.readline())
        Ycord = int(File.readline())
        CharacterArray[x] = Character(character, Xcord, Ycord)
    except IOError:
        print("File not found")

print(CharacterArray)


Position = -1
CharacterName = ""
while Position == -1:
    CharacterName = input("Enter Character Name: ").lower().strip()
    for x in range(0, 10):
        if CharacterArray[x].GetName().strip().lower() == CharacterName:
            Position = x


Letter = input("Enter Letter: ")
if Letter == "A":
    CharacterArray[Position].ChangePosition(-1, 0)
if Letter == "W":
    CharacterArray[Position].ChangePosition(0, 1)
if Letter == "S":
    CharacterArray[Position].ChangePosition(0, -1)
if Letter == "D":
    CharacterArray[Position].ChangePosition(1, 0)

print(CharacterArray[Position].GetName().strip() + " has changed coordinates to X = " +
      str(CharacterArray[Position].GetX()) + " and Y = " + str(CharacterArray[Position].GetY()))
