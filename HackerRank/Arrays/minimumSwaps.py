import random
import time


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

for i in range(5):
    randArr = list(range(10**(i+1)))

    randArr.remove(0)

    random.shuffle(randArr)
    start = time.time()
    minSwap = minimumSwaps(randArr)
    end = time.time()

    print(f"Length of Array:{10**(i+1)}, Minimum swaps:{minSwap}, execution time: {end - start}")

# Length of Array:10, Minimum swaps:5, execution time: 4.0531158447265625e-06
# Length of Array:100, Minimum swaps:96, execution time: 7.009506225585938e-05
# Length of Array:1000, Minimum swaps:995, execution time: 0.005898952484130859
# Length of Array:10000, Minimum swaps:9992, execution time: 0.44358396530151367
# Length of Array:100000, Minimum swaps:99985, execution time: 44.5762038230896