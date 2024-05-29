'''  2. Given an array A[] of n numbers and another number x, the task is to check whether
or not there exist two elements in A[] whose sum is exactly x.
Input: arr[] = {0, -1, 2, -3, 1}, x= -2
Output: Yes
Explanation: If we calculate the sum of the output,1 + (-3) = -2
Input: arr[] = {1, -2, 1, 0, 5}, x = 0
Output: No    '''

def has_pair_with_sum(arr, x):
    # Set to store the complements
    complements = set()
    
    for num in arr:
        complement = x - num
        if complement in complements:
            return "Yes"
        complements.add(num)
    
    return "No"
