# WRITE ITEM_IN_COMMON FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################


def item_in_common(list1, list2):
    list1 = {val: True for val in list1}

    for i in list2:
        if i in list1.keys():
            return True
    return False



list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""