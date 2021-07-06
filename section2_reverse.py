# reverse the string
# 1st method using slice

'''
def string_reverse(string1):
    return string1[::-1]
print string_reverse('hello')
'''


# https://github.com/eunki7/Python-Programs/blob/master/reverse.py
# 2nd method through list

def reverse(list):
    rlist = []
    i = len(list) - 1
    print(i)

    while i >= 0:
        rlist.append(list[i])
        i = i - 1
    return rlist


print(reverse("anum"))
print(reverse("anum"))
print(reverse("anum"))
