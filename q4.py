def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("6800923757255865070000705685527573290086"))
print(palindrome("9847255590886266818998186626880955527489"))
print(palindrome("1414884937242655719669145562427394884141"))
print(palindrome("6892149109325320763773670235239019412986"))