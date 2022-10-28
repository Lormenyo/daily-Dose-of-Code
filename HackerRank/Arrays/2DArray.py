

def hourglassSum(arr):
    sums = []
    for row in range(4):
        for column in range(4):
            # print(row, column)
            subArray = [a[column:column+3] for a in arr[row:row+3]]
            # print(subArray)
            sums.append(sum(sum(subArray, [])))
    
    return max(sums)


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print()

print(f"max: {hourglassSum(arr)}")