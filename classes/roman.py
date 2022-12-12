

def roman(number):
    num = [1, 4]
    sym = ["I", "IV"]
    i = 1

    return_number = ""

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            return_number += sym[i]
            div -= 1
        i -= 1

    return return_number
