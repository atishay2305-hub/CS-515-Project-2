def comment_parser(program):
    lines = program.split("\n")
    res = ""
    commandFlag = False
    for line in lines:
        if line.strip() == "":
            continue
        if line[-1] == "\n":
            line = line[:-1]
        if not commandFlag:
            if "#" in line:
                l = line.split("#", 2)
                if l[0].strip() != "":
                    res += l[0] + "\n"
            elif "/*" in line:
                commandFlag = True
                l = line.split("/*", 2)
                if l[0].strip() != "":
                    res += l[0] + "\n"
            else:
                res += line + "\n"
        else:
            if "*/" in line:
                commandFlag = False
                l = line.split("*/", 2)
                if l[1].strip() != "":
                    res += l[1] + "\n"
    return res
