# def disemvowel(string):
#     vowels = "aeiouAEIOU"
#     removed = string
#     for c in string:
#         if c in vowels:
#             removed = removed.replace(c,'')
#             #start = removed
#             print(removed)
#     return removed


def disemvowel(string):
    vowels = 'a''e''i''o''u''A''E''I''O''U'
    result = ''
    for letter in string:
        if letter not in vowels:
            result += letter
        print(result)
    return result


disemvowel("This website is for losers LOL!")



