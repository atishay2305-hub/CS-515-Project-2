# def parse_braces(string,operators,variables,values):
#     res=string
#     while('(' in res):
#         start=res.rindex('(')
#         end=res.index(')',start)
#         evl,flag=parse_low(res[start+1:end],operators,variables,values)
#         if(flag==True):
#             return evl,flag
#         res=res[:start]+str(evl)+res[end+1:]
#     return parse_low(res,operators,variables,values)

import re
import copy
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def parse_low(string,operators,variables,values):
    errorFlag=False
    l=re.split('(\+\+|--|\^|%|/|\*|\+|-|==|!=|>=|<=|>|<|&&|\|\||!)',string)
    raw=[]
    val=[]
    i=0
    while(i<len(l)):
        element=l[i].strip()
        if(element in ['++','--']):
            val1=raw.pop()
            val2=l[i+1]
            if(val2.strip()==''):
                if(val1 not in variables):
                    variables.append(val1)
                    values[variables.index(val1)]=0
                raw.append(str(values[variables.index(val1)]))
                if(element=='++'):
                    values[variables.index(val1)]+=1
                else:
                    values[variables.index(val1)]-=1
                
            elif(val1.strip()==''):
                if(val2 not in variables):
                    variables.append(val2)
                    values[variables.index(val2)]=0
                if(element=='++'):
                   values[variables.index(val2)]+=1
                else:
                    values[variables.index(val2)]-=1
                raw.append(str(values[variables.index(val2)]))
            i+=2
            continue
        elif(element=='-'):
            val1=raw.pop()
            if(val1.strip()==''):
                val2=l[i+1]
                if(isfloat(val2)):
                    raw.append(str(-1*float(val2)))
                else:
                    if(val2 not in variables):
                        variables.append(val2)
                        values[variables.index(val2)]=0
                    raw.append(str(-1*values[variables.index(val2)]))
                i+=2
            else:
                raw.append(val1)
                raw.append('-')
                i+=1
            continue
        else:
            raw.append(element)
            i+=1
            continue

def parse_braces(string, operators, variables, values):
    res = string
    while '(' in res:
        start = res.rindex('(')
        end = res.index(')', start)
        evl, flag = parse_low(res[start + 1:end], operators, variables, values)
        if flag:
            return evl, flag
        res = res[:start] + str(evl) + res[end + 1:]
    return parse_low(res, operators, variables, values)


# def parse_statement(inputLines,operators,variables,values):
#     lines=inputLines.split("\n")
#     flag=True
#     for string in lines:
#         flag=is_valid_statement(string,operators,variables,values)
#         if(flag==False or 'print' in variables):
#             print('parse error')
#             return
#     for string in lines:
#         string=string.strip()
#         if(string==''):
#             continue
#         if(string[-1]=='\n'):
#             string=string[:-1]
#         if(string.startswith('print ')):
#             objs = string[6:].split(',')
#             printString=""
#             for elem in objs:
#                 elem=elem.strip()
#                 if(elem in variables):
#                     printString+=str(values[variables.index(elem)])
#                     printString+=" "
#                 else:
#                     evl,flg=parse_braces(elem,operators,variables,values)
#                     if(flg):
#                        printString+='divide by zero'
#                        print(printString.strip())
#                        return
#                     printString+=str(evl)
#                     printString+=" "
#             print(printString.strip())
#         elif(re.search('([a-zA-Z0-9]| )=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('=',1)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]=res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         elif(re.search('([a-zA-Z0-9]| )\+=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('+=',1)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]+=res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         elif(re.search('([a-zA-Z0-9]| )-=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('-=',2)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]-=res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         elif(re.search('([a-zA-Z0-9]| )\*=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('*=',2)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]-=res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         elif(re.search('([a-zA-Z0-9]| )\/=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('/=',2)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(res==0):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]/=res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         elif(re.search('([a-zA-Z0-9]| )\^=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('^=',2)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]=(values[variables.index(exps[0].strip())])**res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         elif(re.search('([a-zA-Z0-9]| )%=([a-zA-Z0-9]| |\()',string)):
#             exps=string.split('%=',2)
#             res,flg=parse_braces(exps[1],operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return
#             if(res==0):
#                 print('divide by zero')
#                 return
#             if(exps[0].strip() in variables):
#                 values[variables.index(exps[0].strip())]%=res
#             else:
#                 variables.append(exps[0].strip())
#                 values.append(res)
#         else:
#             res,flg=parse_braces(string,operators,variables,values)
#             if(flg):
#                 print('divide by zero')
#                 return