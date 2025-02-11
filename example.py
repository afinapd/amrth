def isSymmetrical(str):
    midIndex = 0
    length = len(str)
    if length%2 == 0:
        midIndex = length//2
    else:
        midIndex = length//2 + 1
    pointer1 = 0
    pointer2 = midIndex
    while pointer1 < midIndex and pointer2 < length:
        if (str[pointer1] == str[pointer2]):
            pointer1 += 1
            pointer2 += 1
        else:
            return False
    return True

def reverse_array(arr):
    temp = []
    for i in arr:
        temp.insert(0,i)
    return temp

def reverse_array2(arr):
    i = 0  # first item
    j = len(arr) - 1  # last item
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

def sort2(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    array = [9,1,2,5,8,3,2]
    print(reverse_array(array))
    print(reverse_array2(array))
    print(sort2(array))