from itertools import permutations

'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # if n == 0 or 1:
    #     return 1
    if int(n) == 2:
        return 2
    elif int(n) == 0 or int(n) == 1:
        return 1
    else:
        n1 = n//1
        n2 = n//2
        n3 = n//3

        nums = [1 for x in range(n1)] + [2 for y in range(n2)] + [3 for z in range(n3)]

        res = [x for i in range(len(nums)) for x in permutations(nums, i) if sum(x) == n]

        new_res = set(list(res))

        # new_list = permutations([1 for x in range(n//1)] + [2 for y in range(n//2) + [3 for z in range(n//3)]])

        return len(new_res)

# eating_cookies(2)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")