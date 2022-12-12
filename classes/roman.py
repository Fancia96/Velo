

def roman(number):
    num = [1]
    sym = ["I"]
    i = 0

    return_number = ""

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            return_number += sym[i]
            div -= 1
        i -= 1

    return return_number
