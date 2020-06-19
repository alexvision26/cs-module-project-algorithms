from itertools import permutations

'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # # Your code here
    # if n == 0: #didn't find a way to eat cookies
    #     return 1
    # if n < 0: # found a way to eat cookies
    #     return 0

    # #check if cache exists
    # #check if n is in cache
    # if cache is None:
    #     cache = {}

    # if n in cache:
    #     return cache[n]
    
    # cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    # return cache[n]

    # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

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
        return len(new_res)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")