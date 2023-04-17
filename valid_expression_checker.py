import re
import copy
import sys

variables=[]
values=[]

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def is_valid_expression(string,operators,variables,values):
    l = re.split(r'(\b\w+\b|[^\w\s])', string)
    i=0
    for i in range(0,len(l)):
        l[i]=l[i].strip()
    i=0
    # this is a test implementation for adding variables
    def add_variables(l, variables, values):
        i = 0
        while i < len(l):
            token = l[i]
            operators=['++','--','^','%','/','*','-','+','==','!=','>=','<=','>','<','&&','||','!']
            if token in operators:
                if token in ['++', '--']:
                    if i-1 >= 0 and i+1 < len(l):
                        if l[i-1] == '' and l[i+1] != '' and not isfloat(l[i+1]):
                            if l[i+1] not in variables:
                                variables.append(l[i+1])
                                values.append(0.0)
                        elif l[i+1] == '' and l[i-1] != '' and not isfloat(l[i-1]):
                            if l[i-1] not in variables:
                                variables.append(l[i-1])
                                values.append(0.0)
                        else:
                            return False
                        i += 2
                    else:
                        return False
                elif token not in ['-', '!']:
                    if i-1 >= 0 and i+1 < len(l):
                        if l[i-1] != '' and l[i+1] != '' and l[i+1] not in operators and l[i-1] not in operators:
                            if not isfloat(l[i+1]) and l[i+1] not in variables:
                                variables.append(l[i+1])
                                values.append(0.0)
                            if not isfloat(l[i-1]) and l[i-1] not in variables:
                                variables.append(l[i-1])
                                values.append(0.0)
                        elif i+2 < len(l) and l[i+1] == '' and (l[i+2] == '-' or l[i+2] == '!'):
                            if not isfloat(l[i-1]) and l[i-1] not in variables:
                                variables.append(l[i-1])
                                values.append(0.0)
                        else:
                            return False
                        i += 2
                    else:
                        return False
                elif token == '!':
                    if i-1 >= 0 and i+1 < len(l):
                        if l[i-1] == '' and l[i+1] not in operators:
                            if not isfloat(l[i+1]) and l[i+1] not in variables and l[i+1] != '':
                                variables.append(l[i+1])
                                values.append(0.0)
                            i += 2
                        else:
                            return False
                else:
                    if i-1 >= 0 and i+1 < len(l):
                        if l[i+1] not in operators and l[i-1] not in operators and l[i+1] != '':
                            if not isfloat(l[i+1]) and l[i+1] not in variables and l[i+1] != '':
                                variables.append(l[i+1])
                                values.append(0.0)
                            if not isfloat(l[i-1]) and l[i-1] not in variables and l[i-1] != '':
                                variables.append(l[i-1])
                                values.append(0.0)
                        else:
                            return False
                        i += 2
                    else:
                        return False
            else:
                if not isfloat(token) and token not in variables and token != '':
                    variables.append(token)
                    values.append(0.0)
                i += 1
        return True
    return 



def main():
    code=sys.stdin.read()
if __name__ == '__main__':
    main()