
def distance(s1, s2):

    if len(s1) != len(s2):
        raise ValueError("test message")
    else:
        value = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
        return value