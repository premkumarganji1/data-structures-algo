# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################


def first_non_repeating_char(x):
    characters = dict()
    for i in x:
        if i not in characters.keys():
            characters[i] = True
        else:
            characters[i] = False

    for i in x:
        if characters[i] is True:
            return i
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""