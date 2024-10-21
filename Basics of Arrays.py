## Program to find the sum of an array
def sumOfArr(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]

    return total

##Linear search
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

##Swap neighbors
def swapNeighbors(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

##Unique number
def findUniqueNumber(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key, value in freq.items():
        if value == 1:
            return key
    return None

##Find duplicates
def findDuplicate(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key, value in freq.items():
        if value > 1:
            return key
    return None




if __name__ == "__main__":
    arr = [5, 10, 15, 20, 50]
    arr2 = [1,1,2,2,3,3,4,4,5]
    arr3 = [1,2,3,4,5,5,6]
    # print(f"The total sum of the given array is {sumOfArr(arr)}")

    # print(linearSearch(arr, 15))
    # print(swapNeighbors(arr))
    # print(findUniqueNumber(arr2))
    # print(findDuplicate(arr3))

