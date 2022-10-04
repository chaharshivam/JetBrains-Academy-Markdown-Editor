def f1(x):
    return float(x * x + 1)


def f2(x):
    return float(1 / (x * x))


def f3(x):
    return float((x * x) - 1)


def f(x):
    if x <= 0:
        return f1(x)
    elif 0 < x < 1:
        return f2(x)
    else:
        return f3(x)

