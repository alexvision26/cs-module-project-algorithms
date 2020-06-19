'''
Input: a List of integers
Returns: a List of integers
'''

from functools import reduce

# def product_of_all_other_numbers(arr):
#     # Your code here
#     # array needs to multiply the value of all other numbers except the current index during iteration
#     res = []
#     q = [x for x in arr]
#     count = 0

#     while count < len(q):
#         prod = 1
#         curr = q.pop(count) # remove current element to avoid being multiplied, store it in variable
#         for i in q: 
#             prod = prod * i # loop through remaining numbers and get product
#         res.append(prod) #append that product to the answers list
#         q.insert(count, curr) # re add the number removed to keep list
#         count += 1 #increment counter to iterate over each element
#     return res

def product_of_all_other_numbers(arr):
    if 0 in arr:
        arr_prod = reduce((lambda x,y: x=y=1 if x == 0 or y == 0), arr)
    else:
        arr_prod = reduce((lambda x, y: x * y), arr)
    res = []

    for x in range(len(arr)):
        if arr[x] == 0:
            arr[x] = 1
            new_prod = reduce((lambda x, y: x * y), arr)
        else:
            arr[x] = int(arr_prod / arr[x])


    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 0]
# 864
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
