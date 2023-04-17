import re

variables = []
values = [0.0] * 26


def low_parse(string):
    # doctests
    """
    >>> low_parse('a+b')
    ['a', '+', 'b']
    >>> low_parse('a++-b* c')
    ['0.0', '-', 'b', '*', 'c']
    >>> low_parse('++x+y* z')
    ['1.0', '+', 'y', '*', 'z']
    >>> low_parse('e--')
    ['0.0']
    >>> low_parse('--f')
    ['-1.0']
    """
    # this function is used to parse and evulate a simple or finite expression which dont have braces prints anything but expressions
    # string is split into list
    l = re.split('(\+\+|--|\^|%|/|\*|\+|-)', string)
    raw = []
    i = 0

    # this loop is used for parsing and evluate at same time,highest precedence ++,-- should be dealt fisrt

    while (i < len(l)):
        element = l[i].strip()
        # this if is used toi evluate ++,--
        if (element in ['++', '--']):
            val1 = raw.pop()
            val2 = l[i+1]
            if (val2.strip() == ''):
                if (val1 not in variables):
                    variables.append(val1)
                    values.append(0.0)
                raw.append(str(values[variables.index(val1)]))
                if (element == '++'):
                    values[variables.index(val1)] += 1
                else:
                    values[variables.index(val1)] -= 1

            elif (val1.strip() == ''):
                if (val2 not in variables):
                    variables.append(val2)
                    values.append(0.0)
                if (element == '++'):
                    values[variables.index(val2)] += 1
                else:
                    values[variables.index(val2)] -= 1
                raw.append(str(values[variables.index(val2)]))
            i += 2
            continue
        else:
            raw.append(element)
            i += 1
            continue

    return raw


if __name__ == "__main__":
    import doctest
    doctest.testmod()
