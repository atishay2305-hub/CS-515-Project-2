import re
import copy
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_valid_expression(string,operators,variables,values):
    l=re.split('(\+\+|--|\^|%|/|\*|\+|-|==|!=|>=|<=|>|<|&&|\|\||!)',string)
    i=0
    for i in range(0,len(l)):
        l[i]=l[i].strip()
    i=0
    while(i<len(l)):
        if(l[i] in operators):
            if(l[i] in ['++','--']):
                if(l[i]=='--' and i-1>=0 and i+1<len(l) and l[i+1].strip()!='' and l[i-1].strip()!=''):
                    i+=2
                    continue
                if(i-1>=0 and i+1<len(l) and l[i-1].strip()=='' and l[i+1].strip()!='' and not isfloat(l[i+1])):
                    if(l[i+1] not in variables):
                        variables.append(l[i+1])
                        values.append(0.0)
                elif(i-1>=0 and i+1<len(l) and l[i+1]=='' and l[i-1]!='' and not isfloat(l[i-1])):
                    if(l[i-1] not in variables):
                        variables.append(l[i-1])
                        values.append(0.0)
                else:
                    return False
                i+=2
            elif(l[i]!='-' and l[i]!='!'):
                if(i-1>=0 and i+1<len(l) and l[i-1]!='' and l[i+1] not in operators and l[i-1] not in operators):
                    if(l[i+1].strip()=='' and i+2<len(l) and l[i+2]=='-'):
                        i+=2
                        continue
                    elif(l[i+1].strip==''):
                        return False
                    if(not isfloat(l[i+1]) and l[i+1] not in variables):
                        variables.append(l[i+1])
                        values.append(0.0)
                    if(not isfloat(l[i-1]) and l[i-1] not in variables):
                        variables.append(l[i-1])
                        values.append(0.0)
                        
                elif(i+2<len(l) and l[i+1]=='' and (l[i+2]=='-' or l[i+2]=='!')):
                    if(not isfloat(l[i-1]) and l[i-1] not in variables):
                        variables.append(l[i-1])
                        values.append(0.0)
                else:
                    return False
                i+=2
            elif(l[i]=='!' ):
                if(i-1>=0 and i+1<len(l) and l[i-1]=='' and l[i+1] not in operators):
                    if(not isfloat(l[i+1]) and l[i+1] not in variables and l[i+1]!=''):
                        variables.append(l[i+1])
                        values.append(0.0)
                    i+=2
                else:
                    return False
            else:
                if(i-1>=0 and i+1<len(l) and l[i+1] not in operators and l[i-1] not in operators):
                    if(l[i+1].strip()=='' and i+2<len(l) and l[i+2]=='-'):
                        i+=2
                        continue
                    elif(l[i+1].strip==''):
                        return False
                    if(not isfloat(l[i+1]) and l[i+1] not in variables and l[i+1]!=''):
                        variables.append(l[i+1])
                        values.append(0.0)
                    if(not isfloat(l[i-1]) and l[i-1] not in variables and l[i-1]!=''):
                        variables.append(l[i-1])
                        values.append(0.0)
                else:
                    return False
                i+=2
        else:
            if(not isfloat(l[i]) and l[i] not in variables):
                if(l[i].strip()==''):
                    i+=1
                    continue
                if(not bool(re.match("^[A-Za-z0-9_]+$", l[i].strip())) or l[i]=='print'):
                    return False
                
                variables.append(l[i].strip())
                values.append(0.0)
            i+=1
    return True
def is_valid_braces(string,operators,variables,values):
    res = string
    while('(' in res):
        start=res.rindex('(')
        if(')' not in res[start:]):
            return False
        end=res.index(')',start)
        if(not is_valid_expression(res[start+1:end],operators,variables,values)):
            return False
        res=res[:start]+'1.0'+res[end+1:]
    return is_valid_expression(res,operators,variables,values)
def is_valid_statement(string,operators,variables,values):
    string=string.strip()
    if(string==''):
        return True
    if(string[-1]=='\n'):
        string=string[:-1]
    if(string.startswith('print ')):
        objs = string[6:].split(',')
        for elem in objs:
            elem = elem.strip()
            if(not is_valid_braces(elem,operators,variables,values)):
                return False
    elif(re.search('([a-zA-Z0-9]| )(=|\+=|-=|\*=|\/=|\^=|%=|&&=|\|\=)([a-zA-Z0-9]| |\()',string)):
        l=re.split('(=|\+=|-=|\*=|\/=|\^=|%=|&&=|\|\|=)',string,maxsplit=1)
        if(len(l)!=3):
            return False
        if(re.search('([a-zA-Z0-9]| )(=|\+=|-=|\*=|\/=|\^=|%=|&&=|\|\=)([a-zA-Z0-9]| |\()',l[2])):
            return False
        if(isfloat(l[0])):
            return False
        if(not bool(re.match("^[A-Za-z0-9_]+$", l[0].strip()))):
            return False
        if(not (is_valid_braces(l[0],operators,variables,values) and is_valid_braces(l[2],operators,variables,values))):
            return False
    else:
        if(not is_valid_braces(string,operators,variables,values)):
            return False
    return True
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
            elif(val1.strip()!='' and val2.strip()!='' and l[i]=='--'):
                raw.append(val1)
                raw.append('-')
                raw.append('')
                l[i]='-'
                i-=2
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
                        values.append(0.0)
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

    for element in raw:
        element=element.strip()
        if(element in operators):
            val.append(element)
        elif(isfloat(element)):
            val.append(float(element))
        else:
            if(element.strip()==''):
                val.append(element)
                continue
            if(element not in variables):
                variables.append(element)
                values[variables.index(element)]=0
            val.append(float(values[variables.index(element)]))
    while(True):
        if(len(val)==1):
            break
        loopFlag=False
        ind=0
        res=0
        if('^' in val):
            loopFlag=True
            li2 = copy.deepcopy(val)
            li2 = li2[::-1]
            r_ind=li2.index('^')
            ind=len(val)-r_ind-1
            res=val[ind-1]**val[ind+1]
        elif('%' in val):
            loopFlag=True
            ind=val.index('%')
            if(val[ind+1]==0):
                errorFlag=True
                break
            res=val[ind-1]%val[ind+1]
        elif('/' in val):
            loopFlag=True
            ind=val.index('/')
            if(val[ind+1]==0):
                errorFlag=True
                break
            res=val[ind-1]/val[ind+1]
        elif('*' in val):
            loopFlag=True
            ind=val.index('*')
            res=val[ind-1]*val[ind+1]
        elif('-' in val):
            loopFlag=True
            ind=val.index('-')
            res=val[ind-1]-val[ind+1]
        elif('+' in val):
            loopFlag=True
            ind=val.index('+')
            res=val[ind-1]+val[ind+1]
        elif("==" in val):
            loopFlag=True
            ind=val.index('==')
            res=0
            if(val[ind-1]==val[ind+1]):
                res=1
        elif("!=" in val):
            loopFlag=True
            ind=val.index('!=')
            res=1
            if(val[ind-1]==val[ind+1]):
                res=0
        elif("<=" in val):
            loopFlag=True
            ind=val.index('<=')
            res=0
            if(val[ind-1]<=val[ind+1]):
                res=1
        elif(">=" in val):
            loopFlag=True
            ind=val.index('>=')
            res=0
            if(val[ind - 1] >= val[ind + 1] ):
                res=1
        elif("<" in val):
            loopFlag=True
            ind=val.index('<')
            res=0.0
            if(val[ind-1]<val[ind+1]):
                res=1.0
        elif(">" in val):
            loopFlag=True
            ind=val.index('>')
            res=0.0
            if(val[ind-1]>val[ind+1]):
                res=1.0
        elif("&&" in val):
            loopFlag=True
            ind=val.index('&&')
            res=0
            if(val[ind-1]!=0 and val[ind+1]!=0):
                res=1
        elif("||" in val):
            loopFlag=True
            ind=val.index('||')
            res=1
            if(val[ind-1]==0 and val[ind+1]==0):
                res=0.0
        elif("!" in val):
            ind=val.index('!')
            res=0
            if(val[ind+1]==0):
                res=1
            if(val[ind-1].strip()==''):
                loopFlag=True
        if(loopFlag):
            ind=ind-1
            val.pop(ind)
            val.pop(ind)
            val.pop(ind)
            val.insert(ind,res)
            continue
            
    return val[0],errorFlag
def parse_braces(string,operators,variables,values):
    res=string
    while('(' in res):
        start=res.rindex('(')
        end=res.index(')',start)
        evl,flag=parse_low(res[start+1:end],operators,variables,values)
        if(flag==True):
            return evl,flag
        res=res[:start]+str(evl)+res[end+1:]
    return parse_low(res,operators,variables,values)
def parse_statement(inputLines,operators,variables,values):
    lines=inputLines.split("\n")
    flag=True
    for string in lines:
        flag=is_valid_statement(string,operators,variables,values)
        if(flag==False or 'print' in variables):
            print(f'parse error')
            return
    for variable in variables:
        if(variable=='print' or not bool(re.match("^[A-Za-z0-9_]+$", variable))):
            print(f'parse error')
            return
    for string in lines:
        string=string.strip()
        if(string==''):
            continue
        if(string[-1]=='\n'):
            string=string[:-1]
        if(string.startswith('print ')):
            objs = string[6:].split(',')
            printString=""
            for elem in objs:
                elem=elem.strip()
                if(elem in variables):
                    printString+=str(values[variables.index(elem)])
                    printString+=" "
                else:
                    evl,flg=parse_braces(elem,operators,variables,values)
                    if(flg):
                       printString+='divide by zero'
                       print(printString.strip())
                       return
                    printString+=str(evl)
                    printString+=" "
            print(printString.strip())
        elif(re.search('([a-zA-Z0-9]| )=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('=',1)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print(f'divide by zero')
                return
            values[variables.index(exps[0].strip())]=res
        elif(re.search('([a-zA-Z0-9]| )\+=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('+=',1)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print(f'divide by zero')
                return
            values[variables.index(exps[0].strip())]+=res
        elif(re.search('([a-zA-Z0-9]| )-=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('-=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print(f'divide by zero')
                return
            values[variables.index(exps[0].strip())]-=res
        elif(re.search('([a-zA-Z0-9]| )\*=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('*=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print(f'divide by zero')
                return
            values[variables.index(exps[0].strip())]-=res
        elif(re.search('([a-zA-Z0-9]| )\/=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('/=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print(f'divide by zero')
                return
            if(res==0):
                print(f'divide by zero')
                return
            values[variables.index(exps[0].strip())]/=res
        elif(re.search('([a-zA-Z0-9]| )\^=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('^=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print('divide by zero')
                return
            values[variables.index(exps[0].strip())]=(values[variables.index(exps[0].strip())])**res
        elif(re.search('([a-zA-Z0-9]| )%=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('%=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print('divide by zero')
                return
            if(res==0):
                print('divide by zero')
                return
            values[variables.index(exps[0].strip())]%=res
        elif(re.search('([a-zA-Z0-9]| )&&=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('&&=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print('divide by zero')
                return
            if(values[variables.index(exps[0].strip())]!=0 and res!=0):
                values[variables.index(exps[0].strip())]%=1
            else:
                values[variables.index(exps[0].strip())]%=0
        elif(re.search('([a-zA-Z0-9]| )\|\|=([a-zA-Z0-9]| |\()',string)):
            exps=string.split('||=',2)
            res,flg=parse_braces(exps[1],operators,variables,values)
            if(flg):
                print('divide by zero')
                return
            if(values[variables.index(exps[0].strip())]!=0 or res!=0):
                values[variables.index(exps[0].strip())]%=1
            else:
                values[variables.index(exps[0].strip())]%=0
        else:
            res,flg=parse_braces(string,operators,variables,values)
            if(flg):
                print('divide by zero')
                return 
def comment_parser(program):
    lines=program.split("\n");
    res=""
    commandFlag=False
    for line in lines:
        if(line.strip()==''):
            continue
        if(line[-1]=="\n"):
                line=line[:-1]
        if(not commandFlag):
            if('#' in line):
                l=line.split('#',2)
                if(l[0].strip()!=''):
                    res+=(l[0]+"\n")
            elif("/*" in line):
                commandFlag=True
                l=line.split('/*',2)
                if(l[0].strip()!=''):
                    res+=(l[0]+"\n")
            else:
                res+=(line+"\n")
        else:
            if("*/" in line):
                commandFlag=False
                l=line.split('*/',2)
                if(l[1].strip()!=''):
                    res+=(l[1]+"\n")
    return res
def main():
    variables=[]
    values=[]
    operators=['++','--','^','%','/','*','-','+','==','!=','>=','<=','>','<','&&','||','!']
    code=sys.stdin.read()
    parse_statement(comment_parser(code),operators,variables,values)
if __name__ == '__main__':
    main()
