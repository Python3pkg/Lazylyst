import numpy as np

# Convert a string into easy to read text, assumes no lists
def dict2Text(aDict):  
    # Get all values first as strings
    keys=np.array([key for key,val in aDict.iteritems()])
    vals=np.array([str(val) for key,val in aDict.iteritems()])
    # Sort them alphabetically (better than random atleast)
    argSort=np.argsort(keys)
    vals=vals[argSort]
    keys=keys[argSort]
    # Put them all into one larger string   
    string=''
    for i in range(len(vals)):
        string+=keys[i]+'='+vals[i]+',' 
    if len(string)>0: 
        string=string[:-1]
    return string
    
# Convert text into a dictionary,assumes no lists
def text2Dict(text):
    if '=' not in text:
        return {}
    aDict=dict(x.split('=') for x in text.split(','))
    # Check if any of the values represent type other than string
    for key,val in aDict.iteritems():
        # Do not convert numbers to bool
        if val in ['True','False']:
            aDict[key]=bool(val)
        # Otherwise see if it is a number
        try:
            if '.' in val:
                aDict[key]=float(val)
            else:
                aDict[key]=int(val)
        # If none of the above, leave as a string
        except:
            continue
    return aDict