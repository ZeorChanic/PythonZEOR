def valid_parenthesis(string):
    parenthesis = {"(": ")"}
    array = []
    for character in string:
        if character not in '()':
            continue
        elif character in parenthesis.keys():
            array.append(character)
        else:
            if len(array) == 0 or parenthesis[array.pop()] != character:
                return False
    return len(array) == 0


print(valid_parenthesis("  ("))
print(valid_parenthesis(")test"))
print(valid_parenthesis(""))
print(valid_parenthesis("hi())("))
print(valid_parenthesis("hi(hi)()"))