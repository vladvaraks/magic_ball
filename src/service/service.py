def plural(value):
    value = abs(int(value))
    if value in (11, 12, 13, 14):
        variant = 'раз'
    elif value % 10 in (2, 3, 4):
        variant = 'раза'
    else:
        variant = 'раз'

    return variant