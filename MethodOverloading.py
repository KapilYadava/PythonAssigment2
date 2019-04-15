def __gt__(a, b):
    if len(a) > len(b):
        return True
    else:
        return False


print(__gt__('Hello', 'Hell'))


def __add__(T):
    return [T[0][0] + T[1][0], T[0][1] + T[1][1]]


T = [[1, 2], [3, 4]]
print(__add__(T))
