def toJadenCase(string):
    temp = string.split(' ')
    result = ''
    for palabra in temp:
        avanzando = palabra.capitalize()
        result = result + ' ' + avanzando
    print(result[1:])

# return " ".join(word.capitalize() for word in string.split(' '))

toJadenCase('and send simple email messages')