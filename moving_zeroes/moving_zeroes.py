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

arr = [0, 3, 1, 0, -2]
print(moving_zeroes(arr))

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")