# There is a new mobile game that starts with consecutively numbered clouds. 
# Some of the clouds are thunderheads and others are cumulus. The player can jump 
# on any cumulus cloud having a number that is equal to the number of the current cloud 
# plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it 
# will take to jump from the starting postion to the last cloud. It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

# Example
# c = [0, 1, 0, 0, 0, 1, 0]  -> 3




def jumpingOnClouds(c):
    indexOfZeros = [i for i in range(len(c)) if c[i] == 0]

    dif = [indexOfZeros[i+1] - indexOfZeros[i] for i in range(len(indexOfZeros)-1)]
    # print(f"dif: {dif}")
    count = 0
    jump = 0
    for i in range(len(dif)):
        jump += dif[i]

        # print(f"jump: {jump}")
       
        if jump == 1:
            count += 1
            
        if jump == 2:
            if dif[i] == 2:
                count += 1
                        
            jump = 0
        if jump == 3:
            count += 1
            jump = 0

        # print(count)

    return count

print(jumpingOnClouds([])) #0
print(jumpingOnClouds([0])) #0
print(jumpingOnClouds([1, 0])) #0
print(jumpingOnClouds([1, 0, 0])) #1
print(jumpingOnClouds([1, 0, 0, 1, 0, 0, 0, 0])) #4
print(jumpingOnClouds([1])) #0
print(jumpingOnClouds([1, 1, 1])) #0
print(jumpingOnClouds([0, 0, 0, 0, 0, 0, 0])) #3
print(jumpingOnClouds([0, 0, 0, 1, 0, 0])) #3
