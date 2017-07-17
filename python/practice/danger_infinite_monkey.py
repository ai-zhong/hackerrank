import random

def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(len(alphabet))]

    return res

def score(goal, test_str):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == test_str[i]:
            numSame = numSame + 1
    return numSame/len(goal)

def main():
    goal = 'hi u'
    goal_length = len(goal)
    newstr = generateOne(goal_length)
    best = 0
    newscore = score(goal, newstr)
    while newscore < 1:
        if newscore > best:
            print(newstr)
            best = newscore
        newstr = generateOne(goal_length)
        newscore = score(goal, newstr)

    print(newstr)

main()