'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):
    # Your code here
    check = [x for x in arr] # create a new array to compare to the original
    res = [] #single values go here
    
    for x in range(len(arr)):
        count = 0 #loop through original array and keep count of how many times a value appears
        for j in check: #compare the 2 arrays
            if x == j:
                count += 1
        if count == 1: # if no duplicates, or count is 1 after the loop, it is appended to the results array
            res.append(x)
    return res[0]



# def single_number(arr):
#     #keep track # of times item occurs in input
#     count = {}

#     # loop through input list
#     for i in arr:
#         # if item in count, remove item, if not add item
#         if i in count:
#             del count[i]
#         else:
#             count[i] = 1

#     # return count[count.keys()[0]]
#     for k, v in count.items(): # O(1)
#         if v == 1:
#             return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

