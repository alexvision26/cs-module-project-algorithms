'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    res = []
    zeros = []

    for i in range(len(arr)):
        if arr[i] != 0:
            res.append(arr[i])
        else:
            zeros.append(arr[i])
    res.extend(zeros)
    return res


def moving_zeroes_optimized(arr):
    left = 0
    right = len(arr) - 1

    # loop until left and right pointers meet
    while left < right:
        if arr[left] == 0 and arr[right] !=0:
            arr[left] = arr[right]
            arr[right] = 0
            left += 1
            right -= 1
        elif arr[left] != 0:
            left += 1
        if arr[right] == 0:
            right -= 1
        # swap situation:
        # left sees zero, right see non-zero
            # swap the items
            #increment left
            #decrement right
        # non swap situation
            #if left sees non zero
                #increment left
            # if right sees zero
                #decrement right

    return arr

# arr = [0, 3, 1, 0, -2]
# print(moving_zeroes_optimized(arr))

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2, 5, 0, -3, 2, 1, 25, 37, 0, 55, -27]

    print(f"The resulting of moving_zeroes is: {moving_zeroes_optimized(arr)}")