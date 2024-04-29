# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################


def group_anagrams(strings):
    anagrams = dict()

    for word in strings:
        sorted_word = ''.join(sorted(word))

        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)

    anagrams_list = []
    for word_list in anagrams.values():
        anagrams_list.append(word_list)

    return anagrams_list



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""