test_list = [['float','flight','flow'],
             ['float','fixxfs','floatxxxxxx'],
             ['c','c'],
             ['aa','ab']]

def longest_prefix(strs):
    min_str = min(strs)
    max_str = max(strs)
    print(min_str,max_str)
    for x,y in enumerate(min_str):
        #print((x,y))
        if not y in max_str[x]:
            return min_str[:x]
    return min_str

print(longest_prefix(test_list[0]))
print(longest_prefix(test_list[1]))
print(longest_prefix(test_list[2]))


