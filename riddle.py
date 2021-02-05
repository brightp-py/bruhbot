import json

riddles = []
answers = []

with open("solved.json", 'r') as f:
    solved = json.load(f)

def getRiddles():

    global riddles
    global answers

    riddles = []
    answers = []

    with open("riddles.txt", 'r') as f:
        text = f.read()

    for i in text.split('\n\n'):
        r, a = i.split('\nAnswer: ')
        riddles.append(r)
        answers.append(a)
    
    return riddles, answers

def saveSolved():

    with open("solved.json", 'w') as f:
        json.dump(solved, f)

def printRiddle(msg):

    getRiddles()

    if ' ' not in msg:
        return None
    if msg.split(' ')[0] != 'riddle':
        return None
    if any(c not in '1234567890' for c in msg.split(' ')[1]):
        return None

    num = int(msg.split(' ')[1])
    if num >= 0 and num < len(riddles):
        return "Riddle " + str(num) + '\n' + riddles[num]
    return None

def checkSolution(response, user):
    if response in answers:
        if user not in solved:
            solved[user] = []
        if response not in solved[user]:
            solved[user].append(response)
            i = answers.index(response)
            saveSolved()
            return user.split('#')[0] + " has solved Riddle " + str(i) + "!"
    return None

getRiddles()