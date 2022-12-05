
#only works for 2 test cases
def makeAnagram1(a, b):
    diff = (len(a) - len(set(a))) + (len(b)-len(set(b)))
    return len(set(a) ^ set(b)) + diff

def makeAnagram2(a,b):
    a = sorted(list(a))
    b = sorted(list(b))

    return sum(aElement != bElement for aElement, bElement in zip(a, b) ) + abs(len(a)-len(b))

print(makeAnagram1("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))

    