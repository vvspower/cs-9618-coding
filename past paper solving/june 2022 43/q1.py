global PlayerNames
global PlayerScores

PlayerNames = ["", "", "", "", "", "", "", "", "", "", ""]
PlayerScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def ReadHighScores():
    HighScoreFile = open("HighScore.txt", 'r')
    for x in range(0, 10):
        Name = HighScoreFile.readline()
        Score = HighScoreFile.readline()
        PlayerNames[x] = Name
        PlayerScores[x] = int(Score)
    HighScoreFile.close()


def OutputHighScores():
    for x in range(0, 10):
        print(PlayerNames[x].strip() + " " + str(PlayerScores[x]))


def CreateTopTenList(Name, Score):
    global PlayerNames
    global PlayerScores

    print(PlayerNames, PlayerScores)

    PlayerNames[10] = Name
    PlayerScores[10] = Score

    print(PlayerNames, PlayerScores)

    for x in range(0, 10):
        for y in range(0, 10):
            if PlayerScores[y] < PlayerScores[y + 1]:
                TempName, TempScore = PlayerNames[y + 1], PlayerScores[y + 1]
                PlayerNames[y + 1], PlayerScores[y +
                                                 1] = PlayerNames[y], PlayerScores[y]
                PlayerNames[y], PlayerScores[y] = TempName, TempScore
    PlayerNames = PlayerNames[:10]
    PlayerScores = PlayerScores[:10]


def WriteTopTen():
    global PlayerNames, PlayerScores
    NewFile = open('NewHighScore.txt', 'w')
    for x in range(0, 10):
        NewFile.write(str(PlayerNames[x] + "\n"))
        NewFile.write(str(str(PlayerScores[x]) + "\n"))
    NewFile.close()


    # main
ReadHighScores()
OutputHighScores()

NewPlayerName = input("Enter 3 Character Player Name:  ")
NewPlayerScore = int(input("Enter Score Between 1 and 100000:  "))

CreateTopTenList(NewPlayerName, NewPlayerScore)
OutputHighScores()
