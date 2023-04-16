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
        elif('+' in val):
            loopFlag=True
            ind=val.index('+')
            res=val[ind-1]+val[ind+1]
        elif('-' in val):
            loopFlag=True
            ind=val.index('-')
            res=val[ind-1]-val[ind+1]
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
