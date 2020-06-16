#https://www.runoob.com/python/python-func-zip.html
test_list = [['float','flight','flow'],
             ['float','fixxfs','floatxxxxxx'],
             ['c','c'],
             ['aa','ab']]

def longest_prefix(strs):
    ans = ''
    for i in zip(*strs):
        print(i)
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans

print(longest_prefix(test_list[0]))
print(longest_prefix(test_list[1]))
print(longest_prefix(test_list[2]))


