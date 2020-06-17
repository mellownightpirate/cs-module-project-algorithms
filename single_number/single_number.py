'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    singleInts = set()
    for num in arr:
        if num in singleInts:
            # remove duplicate of any number
            singleInts.remove(num)
        else:
            # add the number to the array
            singleInts.add(num)
    return singleInts.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")