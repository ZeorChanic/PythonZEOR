def unique_in_order(iterable):
    anterior = ''
    array = []
    for letra in iterable:
        if letra != anterior:
            array.append(letra)
            anterior = letra
    print(array)


unique_in_order('XXXNNNGGDDDFFF')