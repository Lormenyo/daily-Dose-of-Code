

def minimumSwaps(arr):
    numberOfSwaps = 0
    for i in range(len(arr)):
        if i != arr[i]-1:
            swapValue = arr[i]
            swapIndex = arr.index(i+1)
            arr[i] = i+1
            arr[swapIndex] = swapValue
            
            numberOfSwaps += 1
    return numberOfSwaps

arr1 =  [7, 1, 3, 2, 4, 5, 6]
arr2 = [4,3,1,2]