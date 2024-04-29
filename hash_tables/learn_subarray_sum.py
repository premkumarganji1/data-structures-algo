# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################


def subarray_sum(nums, target):
    # We create a dictionary called 'sum_index' to store
    # running sums (as keys) and their corresponding
    # indices in the array (as values).
    #
    # Why start with {0: -1}?
    # - '0' will serve as the default sum when looking for subarrays.
    # - '-1' indicates there's no subarray yet.
    # This setup helps handle special cases, such as when the
    # first element itself is equal to the target.
    sum_index = {0: -1}

    # Initialize a variable 'current_sum' to keep track of the
    # running sum as we iterate through the array.
    current_sum = 0

    # The enumerate function allows us to loop through 'nums'
    # while keeping track of both the index 'i' and the value 'num'.
    for i, num in enumerate(nums):
        # Update 'current_sum' by adding the current element 'num'.
        current_sum += num
        print(current_sum, current_sum - target, sum_index)

        # We check if a subarray exists with a sum that equals the target.
        # Specifically, we check if 'current_sum - target' is already
        # a key in our 'sum_index' dictionary.
        if current_sum - target in sum_index:
            # If it is, then we have found the subarray we are looking for.
            # We return its start and end indices as a list.
            #
            # sum_index[current_sum - target] + 1 is the start index.
            # We add 1 to move past the element before the subarray starts.
            #
            # 'i' is the end index, where the subarray ends.
            return [sum_index[current_sum - target] + 1, i]

        # If we haven't yet found a subarray with the sum that matches
        # the target, we add the 'current_sum' and its index 'i' to
        # our 'sum_index' dictionary for future checks.
        sum_index[current_sum] = i

    # If we've gone through the entire list and didn't find any
    # subarray with a sum equal to the target, we return an empty list.
    return []


# nums = [1, 2, 3, 4, 5]
# target = 9
# print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

# nums = [2, 3, 4, 5, 6]
# target = 3
# print ( subarray_sum(nums, target) )
#
# nums = []
# target = 0
# print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
