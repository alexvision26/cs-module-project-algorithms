'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # array needs to multiply the value of all other numbers except the current index during iteration
    res = []
    q = [x for x in arr]
    count = 0

    while count < len(q):
        prod = 1
        curr = q.pop(count) # remove current element to avoid being multiplied, store it in variable
        for i in q: 
            prod = prod * i # loop through remaining numbers and get product
        res.append(prod) #append that product to the answers list
        q.insert(count, curr) # re add the number removed to keep list
        count += 1 #increment counter to iterate over each element
    return res



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
