

def hourglassSum(arr):
    sums = []
    for row in range(4):
        for column in range(4):
            # print(row, column)
            subArray = [a[column:column+3] for a in arr[row:row+3]]
            # print(f"sub: {subArray}")
            sums.append(sum(sum(subArray, [])) - subArray[1][0] - subArray[1][2])
    # print(sums)
    return max(sums)


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
arr2 = [
    [1, 1, 1, 0 ,0, 0],
    [0, 1, 0, 0 ,0, 0],
    [1, 1, 1, 0 ,0, 0],
    [0, 9, 2, -4, -4, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, -1, -2, -4, 0]
]

arr3 = [
    [-9, -9, -9,  1, 1, 1], 
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0 , 0 , 1 , 2 ,4 ,0],
]

print(f"max: {hourglassSum(arr)}")
print(f"max: {hourglassSum(arr2)}")
print(f"max: {hourglassSum(arr3)}")