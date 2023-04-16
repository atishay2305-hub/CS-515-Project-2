def is_valid_expression(string, operators, variables, values):
    l = re.split("(\+\+|--|\^|%|/|\*|\+|-|==|!=|>=|<=|>|<|&&|\|\||!)", string)
    i = 0
    for i in range(0, len(l)):
        l[i] = l[i].strip()
    i = 0
    while i < len(l):
        if l[i] in operators:
            if l[i] in ["++", "--"]:
                if (
                    i - 1 >= 0
                    and i + 1 < len(l)
                    and l[i - 1] == ""
                    and l[i + 1] != ""
                    and not isfloat(l[i + 1])
                ):
                    if l[i + 1] not in variables:
                        variables.append(l[i + 1])
                        values.append(0.0)
                elif (
                    i - 1 >= 0
                    and i + 1 < len(l)
                    and l[i + 1] == ""
                    and l[i - 1] != ""
                    and not isfloat(l[i - 1])
                ):
                    if l[i - 1] not in variables:
                        variables.append(l[i - 1])
                        values.append(0.0)
                else:
                    return False
                i += 2
            elif l[i] != "-" and l[i] != "!":
                if (
                    i - 1 >= 0
                    and i + 1 < len(l)
                    and l[i - 1] != ""
                    and l[i + 1] != ""
                    and l[i + 1] not in operators
                    and l[i - 1] not in operators
                ):
                    if not isfloat(l[i + 1]) and l[i + 1] not in variables:
                        variables.append(l[i + 1])
                        values.append(0.0)
                    if not isfloat(l[i - 1]) and l[i - 1] not in variables:
                        variables.append(l[i - 1])
                        values.append(0.0)
                elif (
                    i + 2 < len(l)
                    and l[i + 1] == ""
                    and (l[i + 2] == "-" or l[i + 2] == "!")
                ):
                    if not isfloat(l[i - 1]) and l[i - 1] not in variables:
                        variables.append(l[i - 1])
                        values.append(0.0)
                else:
                    return False
                i += 2
            elif l[i] == "!":
                if (
                    i - 1 >= 0
                    and i + 1 < len(l)
                    and l[i - 1] == ""
                    and l[i + 1] not in operators
                ):
                    if (
                        not isfloat(l[i + 1])
                        and l[i + 1] not in variables
                        and l[i + 1] != ""
                    ):
                        variables.append(l[i + 1])
                        values.append(0.0)
                    i += 2
                else:
                    return False
            else:
                if (
                    i - 1 >= 0
                    and i + 1 < len(l)
                    and l[i + 1] not in operators
                    and l[i - 1] not in operators
                    and l[i + 1] != ""
                ):
                    if (
                        not isfloat(l[i + 1])
                        and l[i + 1] not in variables
                        and l[i + 1] != ""
                    ):
                        variables.append(l[i + 1])
                        values.append(0.0)
                    if (
                        not isfloat(l[i - 1])
                        and l[i - 1] not in variables
                        and l[i - 1] != ""
                    ):
                        variables.append(l[i - 1])
                        values.append(0.0)
                else:
                    return False
                i += 2
        else:
            if not isfloat(l[i]) and l[i] not in variables:
                variables.append(l[i])
                values.append(0.0)
            i += 1
    return True


def is_valid_braces(string, operators, variables, values):
    res = string
    while "(" in res:
        start = res.rindex("(")
        if ")" not in res[start:]:
            return False
        end = res.index(")", start)
        if not is_valid_expression(res[start + 1 : end], operators, variables, values):
            return False
        res = res[:start] + "1.0" + res[end + 1 :]
    return is_valid_expression(res, operators, variables, values)


def is_valid_statement(string, operators, variables, values):
    string = string.strip()
    if string == "":
        return True
    if string[-1] == "\n":
        string = string[:-1]
    if string.startswith("print "):
        objs = string[6:].split(",")
        for elem in objs:
            elem = elem.strip()
            if not is_valid_braces(elem, operators, variables, values):
                return False
    elif re.search(
        "([a-zA-Z0-9]| )(=|\+=|-=|\*=|\/=|\^=|%=)([a-zA-Z0-9]| |\()", string
    ):
        l = re.split("(=|\+=|-=|\*=|\/=|\^=|%=)", string, maxsplit=1)
        if len(l) != 3:
            return False
        if not (
            is_valid_braces(l[0], operators, variables, values)
            and is_valid_braces(l[2], operators, variables, values)
        ):
            return False
    else:
        if not is_valid_braces(string, operators, variables, values):
            return False
    return True
