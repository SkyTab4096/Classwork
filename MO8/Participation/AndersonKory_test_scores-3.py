#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scoreList = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            scoreList.sort()
            return  scoreList
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scoreList.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scoreList):
    # calculate average score
    length = len(scoreList)
    scoreTotal = 0
    medianScores = []
    for i in scoreList:
        scoreTotal += i
    averageScore = round(scoreTotal / length, 0)
    minScore = min(scoreList)
    maxScore = max(scoreList)
    medianIndex = length / 2
    if medianIndex % 2 != 0:
        medianIndex = int(medianIndex - .5)
        medianScore = scoreList[medianIndex]
    else:
        medianIndex1 = int(medianIndex - .5)
        medianIndex2 = int(medianIndex + .5)
        medianScores.append(scoreList[medianIndex1])
        medianScores.append(scoreList[medianIndex2])

    # format and display the result
    print()
    print(f"Score total:\t\t{scoreTotal}")
    print(f"Number of Scores:\t{length}")
    print(f"Average Score:\t\t{averageScore}")
    print(f"Minimum Score:\t\t{minScore}")
    print(f"Maximum Score:\t\t{maxScore}")
    if len(medianScores) == 0:
        print(f"Median Score:\t\t{medianScore}")
    else:
        intialString = str(medianScores)
        partialString = intialString.replace("[", "")
        medianScoresString = partialString.replace("]", "")
        print(f"Median Scores:\t\t{medianScoresString}")


def main():
    display_welcome()
    scoreList = get_scores()
    process_scores(scoreList)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


