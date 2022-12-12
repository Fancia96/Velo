
def distance(s1, s2):

    value = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
    print()
    return value
