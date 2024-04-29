# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################


def two_sum(nums, x):
    indexes = dict()
    for i in range(len(nums)):
        if nums[i] in indexes.keys():
            return [indexes[nums[i]], i]
        else:
            indexes[x - nums[i]] = i
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


