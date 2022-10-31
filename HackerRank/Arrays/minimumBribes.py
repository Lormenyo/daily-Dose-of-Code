

def minimumBribes(q):
    numberOfBribes = 0
    
    for index, number in enumerate(q):
        # print(index, number)
        if index < number - 1:
            numberOfBribes += (number - 1 - index)
            # print(f"number of bribes: {numberOfBribes}")
        if index > number -1:
            numberOfBribes += (index - number)
            # print(f"number of bribes: {numberOfBribes}")
      

            
    if numberOfBribes > 2:
        print(numberOfBribes)
        print("Too chaotic")
    else:
        print(numberOfBribes)

print(minimumBribes([2, 5, 1, 3, 4]))