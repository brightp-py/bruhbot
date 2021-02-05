alpha = "abcdefghijklmnopqrstuvwxyz"

def makeNormal(word):

    toret = ""
    word = word.lower()
    for c in word:
        if c in alpha:
            toret += c
    
    return toret

with open("creeper.txt", 'r') as f:
    words = []
    sp = ' '.join(f.read().split('\n')).split(' ')
    for w in sp:
        a = makeNormal(w)
        if len(words) == 0 or words[-1] != a:
            words.append(a)
