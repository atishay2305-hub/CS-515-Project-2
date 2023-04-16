def parse_evluate(string):
    # this is a dummy function which should be later replaced by orginal low level parsing function
    return 1.0


def parse_braces(string):
    """

    >>> parse_braces('(a+b-(c/d)+e)*f')
    (a+b-(c/d)+e)*f
    (a+b-1.0+e)*f
    1.0*f
    >>> parse_braces('a+b*c')
    a+b*c
    >>> parse_braces('(((a+b)-c)+d-(g*(e+f)))')
    (((a+b)-c)+d-(g*(e+f)))
    (((a+b)-c)+d-(g*1.0))
    (((a+b)-c)+d-1.0)
    ((1.0-c)+d-1.0)
    (1.0+d-1.0)
    1.0
    
    """
    res = string
    while "(" in res:
        print(res)
        # this loop is repeated till every brace is solved
        start = res.rindex("(")
        end = res.index(")", start)
        # here we get the subpart of the expression which is inside the lowest braces level
        res = res[:start] + str(parse_evluate(res[start + 1 : end])) + res[end + 1 :]
    print(res)


if _name_ == "_main_":
    import doctest

    doctest.testmod()
