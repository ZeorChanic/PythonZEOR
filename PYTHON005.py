import queue

def match(l1,l2):
    return True if l1+l2 in ['()', '[]', '{}'] else False

def validBraces(string):
    q = queue.LifoQueue()
    for letter in string:
        if letter in '([{':
             q.put(letter)
        elif letter in ')]}':
            if q.empty():
                return False
            print(letter)
            if not match(q.get(), letter):
                return False
    return q.empty()

# def validBraces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0