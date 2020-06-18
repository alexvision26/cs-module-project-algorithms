'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # each iteration, k values are added to array
    # of the three values added, append the highest value to a results list
    lp = 0
    rp = k - 1
    res = []

    while rp <= len(nums) - 1:
        window = []
        for x in range(k):
            window.append(nums[x + lp])
        max_val = max(window)
        res.append(max_val)
        lp += 1
        rp += 1

    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
