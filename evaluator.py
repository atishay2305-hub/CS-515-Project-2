#this is a basic function which is used to evluate the operators which are only floats and operators
  
def eval(val):
    """

    >>> eval([1.0,'+',2.0])
    3.0
    >>> eval([1.0,'+',2.0,'*',3.0,'-',5.0,'%',4.0])
    6.0
    >>> eval([2.0,'+',4.0,'^',3.0])
    66.0
    """
    while(True):
        if(len(val)==1):
            break
        loopFlag=False
        ind=0
        res=0
        if('^' in val):
            loopFlag=True
            ind=val.index('^')
            res=val[ind-1]**val[ind+1]
        elif('%' in val):
            loopFlag=True
            ind=val.index('%')
            res=val[ind-1]%val[ind+1]
        elif('/' in val):
            loopFlag=True
            ind=val.index('/')
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
        if(loopFlag):
            ind=ind-1
            val.pop(ind)
            val.pop(ind)
            val.pop(ind)
            val.insert(ind,res)
            continue
            
    return val[0]
    
if _name_ == "_main_":
    
    import doctest
    doctest.testmod()
