

def minimumBribes(q):
    numberOfBribes = 0
    isTooChaotic = False
    
    for index, number in enumerate(q):
        if index < number - 1:
            bribesTaken = (number - 1 - index) 
            
            if bribesTaken > 2:
                isTooChaotic = True
            
            else:
                numberOfBribes += bribesTaken
            
    
    if isTooChaotic:
        print("Too chaotic")
    else:
        print(numberOfBribes)
    
    return "----------------------"

print(minimumBribes([2, 5, 1, 3, 4]))
print(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))
print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))